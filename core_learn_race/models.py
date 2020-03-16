from django.db import models

class Race(models.Model):
    group = models.CharField(max_length=10)
    state = models.BooleanField(default=True)
    subjects = models.CharField(max_length=50)
    categories = models.CharField(max_length=100)
    total_score = models.IntegerField(default=100)

class Player(models.Model):
    name = models.CharField(max_length = 50)
    score = models.IntegerField(default = 0)
    active = models.BooleanField(default=True)
    winner = models.BooleanField(default=False)
    raseId = models.ForeignKey('Race', related_name='players', on_delete=models.CASCADE)

class Question(models.Model):
    description = models.CharField(max_length=50)
    value = models.IntegerField()
    category = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
