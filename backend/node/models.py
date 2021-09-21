from django.db import models

# Create your models here.

class Node(models.Model):
    nid = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    read_only = models.BooleanField()
    parent = models.IntegerField(default=0)
    def __str__(self):
        return f'[nid: {self.nid},name: {self.name},parent: {self.parent}]'

