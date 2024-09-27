from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    start_date = models.DateTimeField('Start Date', default=datetime.now)
    end_date = models.DateTimeField('End Date', default=datetime.now)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
