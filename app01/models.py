from django.db import models
# from datetime import date

# Create your models here.
models.manager.Manager
class Department(models.Model):
    # name of department
    name = models.CharField(max_length=20)
    # created time of department
    create_date = models.DateField(null=True)
    def __str__(self):
        return self.name


class Employee(models.Model):
    # employee's name
    name = models.CharField(max_length=20)
    # employee's age
    age = models.IntegerField()
    # employee's gender
    sex = models.IntegerField()
    # employee's salary
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    # hired date of employee
    hire_date = models.DateField()
    # description of employee
    comment = models.CharField(max_length=200,null=True,blank=True)
    # employee's department
    department = models.ForeignKey("Department")

    def __str__(self):
        return self.name


class Employee01(models.Model):
    # employee's name
    name = models.CharField(max_length=20)
    # employee's created time
    create_time = models.DateTimeField(auto_now_add=True)
    # employee's altered time
    update_time = models.DateTimeField(auto_now=True)

