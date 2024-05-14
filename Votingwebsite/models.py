from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class Election(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    candidates = models.ManyToManyField('Candidate', related_name='elections')

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    age = models.IntegerField(default=25)
    votes=models.IntegerField(default=0)

class Result(models.Model):
    election = models.OneToOneField(Election, on_delete=models.CASCADE)
    winner = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    total_votes = models.IntegerField()

class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)