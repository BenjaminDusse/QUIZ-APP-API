from django.db import models
from shared.django.model import BaseModel, DeleteModel


from accounts.models import Profile

class Question(BaseModel):
    content = models.TextField(max_length=500)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.content

class Answer_single(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='question')
    content = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
    
    def __str__(self):
        return self.is_correct

class Answer_selection(models.Model):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, related_name='answer_selected', null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.is_correct

class User_Question_Answers(BaseModel):
    pass