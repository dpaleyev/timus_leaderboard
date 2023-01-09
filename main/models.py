from django.db import models
from django.contrib.auth.models import User

class Theme(models.Model):
    name = models.CharField(max_length=60)
    url = models.URLField()

class Task(models.Model):
    num = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    theme = models.ManyToManyField(Theme, blank=True)

class Note(models.Model):
    task = models.CharField(max_length=60)
    idea = models.TextField(max_length=1000)
    modified = models.DateField(auto_now=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    judge_id = models.CharField(max_length=30)
    completed_tasks = models.ManyToManyField(Task, related_name="compl+", blank=True)
    wa_tasks = models.ManyToManyField(Task, related_name="wa+", blank=True)
    todo_tasks = models.ManyToManyField(Task, related_name="todo+", blank=True)
    notes = models.ManyToManyField(Note, blank=True)

class Lesson(models.Model):
    title = models.CharField(max_length=60)
    theme = models.IntegerField()
    text = models.TextField()
    tasks = models.ManyToManyField(Task, blank=True)

