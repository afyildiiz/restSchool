from django.db import models

# Create your models here.


class Ogrenci(models.Model):
    name=models.CharField(max_length=150)
    surname=models.CharField(max_length=150)
    tel=models.CharField(max_length=150)
    mail=models.CharField(max_length=150)
    register_date=models.DateTimeField(auto_now_add=True)
    average=models.IntegerField()
    still_student=models.BooleanField(default=True)
    
    def __str__(self):
        return self.mail