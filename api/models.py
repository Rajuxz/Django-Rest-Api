from django.db import models

# Company Model
class Comapany(models.Model):
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
