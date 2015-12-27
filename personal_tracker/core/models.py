from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Goal(models.Model):
    short_name = models.CharField(max_length=120)
    long_desc = models.CharField(max_length=2000)
    # pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, 
                        on_delete=models.CASCADE, 
                        related_name='goals')
    is_private = models.BooleanField(default=False)

class Entry(models.Model):
    int_entry = models.IntegerField(default=0)
    float_entry = models.FloatField(blank=True,null=True)
    text_entry = models.CharField(blank=True,null=True,max_length=1500)
    pub_date = models.DateTimeField('date published')
    goal = models.ForeignKey(Goal, 
                        on_delete=models.CASCADE, 
                        related_name='entries')



# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

