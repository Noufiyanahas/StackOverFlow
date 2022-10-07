from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Questions(models.Model):
    description= models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)

class Answers(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=250)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="answer")
    upvote=models.ManyToManyField(User)
    posted_date=models.DateTimeField(auto_now_add=True)