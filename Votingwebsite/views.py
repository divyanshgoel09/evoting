from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from Votingwebsite.models import *
from django.contrib.auth.models import User
# Create your views here.



def HomePage(request):
    return render (request,'home.html')
def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "username already exists")
            return render(request,'signup.html')

        user=User.objects.create(
            email=email,
            username=username,
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully")
        return redirect('/login')
    return  render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username")
            return render(request, 'login.html')

        else:
            user= authenticate(username=username,password=password)

            if user is None:
                messages.error(request, "Invalid password")
                return render(request, 'login.html')
            
            else:
                login(request,user)
                return redirect('/home')
    return  render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('/login')

@login_required(login_url="/login")
def VotePage(request):
    
    queryset=Candidate.objects.all()

    context={'Candidate':queryset}
    return render (request,'vote.html',context)
    # return render (request,'vote.html')

@login_required(login_url="/login")
def ResultPage(request):
    queryset=Candidate.objects.all()

    context={'Candidate':queryset}
    return render (request,'results.html',context)

def Candidate_reg(request):
    if request.method == "POST":
        data=request.POST
        Candidate_name=data.get('name')
        party=data.get('party')
        age=data.get('age')
        
        Candidate.objects.create(name=Candidate_name,party=party,age=age)
        return redirect('/home')
    
    return render(request,'candidate.html')


def vote(request, id):
    candidate = Candidate.objects.get(id=id)
    candidate.votes += 1
    candidate.save() 
    
    return redirect('/home')