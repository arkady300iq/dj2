from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Status(models.Model):
    status = models.CharField(max_length=30)
    
    def __str__(self):
        return self.status

class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name 
    

