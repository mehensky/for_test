from django.contrib import admin
from profiles.models import person,department,duties,company,attendance,attendance_data,attendance_standard,salary_standard,salary_cs


class CompanytAdmin(admin.ModelAdmin):
    list_display = ('company_name',  'company_loca')
    search_fields = ('company_name',)

class Salary_standardAdmin(admin.ModelAdmin):
    list_display = ('salary_lev_name',  'basic_salary')
    search_fields = ('salary_lev_name',)

class Attendance_dataAdmin(admin.ModelAdmin):
	list_display = ('attendance_day','employee_id')
	search_fields = ('attendance_day',)

# Register your models here.
admin.site.register(department)
admin.site.register(company,CompanytAdmin)
admin.site.register(person)
admin.site.register(duties)
admin.site.register(attendance)
admin.site.register(attendance_data,Attendance_dataAdmin)
admin.site.register(attendance_standard)
admin.site.register(salary_standard,Salary_standardAdmin)
admin.site.register(salary_cs)