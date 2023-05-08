from django.db import models

# Create your models here., 
class Chat(models.Model):
    text=models.CharField(max_length=500)
    gpt=models.CharField(max_length=17000)
    date=models.DateField(auto_now_add=True, blank=True ,null=True)
