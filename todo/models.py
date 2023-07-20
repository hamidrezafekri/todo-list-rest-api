from django.db import models


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    user = models.ForeignKey('user.Profile', on_delete=models.CASCADE)
    label = models.ForeignKey('Label' , on_delete=models.CASCADE , blank=True , null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Label(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField('user.Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
