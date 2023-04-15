from django.db import models

# Company Model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_location = models.CharField(max_length=100)
    about = models.CharField(max_length=250)
    company_type = models.CharField(max_length=100,choices=(('IT','IT'),
                                                            ('Business','Business'),
                                                            ('Phone','Phone')
                                                            ))
    
    added_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return self.company_name


class Employee(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=40,choices=(
        ('Manager','manager'),
        ('Director','director'),
        ('Sales Person','salesman'),
        ('IT','programmer')
    ))
   