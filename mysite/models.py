from django.utils import timezone
from email import message
from statistics import mode
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=300)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.email
