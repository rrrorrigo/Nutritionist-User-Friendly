from django.db import models


class Nutritionist(models.Model):
    """Nutritient model wich has its data to save in mysql server"""
    name = models.CharField(max_length=15)
    username = models.CharField(max_length=15)
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=33, null=False)

class Patient(models.Model):
    """Patient model wich has its data to save in mysql server"""
    name = models.CharField(max_length=15)
    username = models.CharField(max_length=15)
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=33, null=False)
    nutritionistId = models.ForeignKey(Nutritionist, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    objective = models.CharField(max_length=250)
    diet = models.CharField(max_length=250)
    nextConsultantion = models.DateField()
