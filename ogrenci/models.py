from django.db import models

# Create your models here.


class Ogrenci(models.Model):
    name=models.CharField(max_length=150)
    surname=models.CharField(max_length=150)
    tel=models.CharField(max_length=150)
    mail=models.CharField(max_length=150)
    register_date=models.DateTimeField(auto_now_add=True)
    average=models.IntegerField()
    status=models.CharField(max_length=20,default='')
    still_student=models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # average değeri 50'nin altındaysa "failed", aksi takdirde "success" olarak atanıyor.
        self.status = 'failed' if self.average < 50 else 'success'
        super().save(*args, **kwargs) 

    def __str__(self):
        return self.mail