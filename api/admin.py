from django.contrib import admin
from api.models import Company,Employee

class CompanyAdmin(admin.ModelAdmin):
    # company_id, company_name, company_location, about, company_type, is_active
    list_display=['company_id','company_name','company_location','about','company_type','is_active',]

class EmployeeAdmin(admin.ModelAdmin):
     # company name email address phone about position
    list_display=['name','email','address','phone','about','position',]

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
