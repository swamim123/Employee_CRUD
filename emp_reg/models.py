# from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Employee(models.Model):  #MODEL --> ITS A CLASS WHICH HOLDS PYTHONSTRUCTURE - DB TABLE MAPPING
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.CharField(max_length=30,unique=True)
    role = models.CharField(max_length=30,default='Guest')
    phone_num = models.BigIntegerField(unique=True)
    joiningDate = models.DateField()
    address = models.CharField(max_length=255,default='Y')
#Employee(name,age,email,role,phone_num,joiningDate,address)

    class Meta:
        db_table = 'EMPLOYEE_MASTER'
        ordering = ['role']        #select * from employee_master order by role desc