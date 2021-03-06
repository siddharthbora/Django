from django.db import models
from django.contrib.auth.models import User


class Questions(models.Model):
    question_level = models.CharField(max_length=225, blank=True)
    question = models.CharField(max_length=255, blank=True)
    option_A = models.CharField(max_length=255, blank=True)
    option_B = models.CharField(max_length=255, blank=True)
    option_C = models.CharField(max_length=255, blank=True)
    option_D = models.CharField(max_length=255, blank=True)
    correct_answer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.question


class Response(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=255, blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.selected_answer

class Register(models.Model):  # extended user model
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
    phone=models.IntegerField(default='')
    level = models.CharField(max_length=15)
    language = models.CharField(max_length=15)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.first_name