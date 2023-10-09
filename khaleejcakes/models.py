from django.db import models

class table_user(models.Model):
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)

    class Meta:
        db_table='table_user'


# Create your models here.
