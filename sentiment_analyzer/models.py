# sentiment_analyzer/models.py

from django.db import models
from django.contrib.auth.models import User

class UserInput(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    prediction = models.CharField(max_length=10)  # 'Positive' or 'Negative'

    def __str__(self):
        return f'{self.user.username} - {self.text}'
