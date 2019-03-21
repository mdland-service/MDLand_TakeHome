from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class mylist(models.Model):
    listname = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.listname

class Todo(models.Model):
    todoname = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    whichlist = models.ForeignKey(mylist, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.todoname
