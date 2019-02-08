from django.db import models

class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    dob=models.DateField()
    doj=models.DateField()
    gender=models.CharField(max_length=10)
    designition=models.CharField(max_length=40)
    contact=models.IntegerField(default=10)
    email=models.EmailField()
    salery=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to="my_images",default=False)


