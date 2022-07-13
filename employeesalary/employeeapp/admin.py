from django.contrib import admin
from .models import Grade, Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_position', 'get_basic_salary', 'gross_salary')

    def get_position(self, obj):
        employee = Grade.objects.filter(id=obj.id)
        return list(employee)

    def get_basic_salary(self, obj):
        salary = Grade.objects.get(id=obj.id)
        return str(salary.basic_salary)

class GradeAdmin(admin.ModelAdmin):
    list_display = ('position', 'basic_salary')

admin.site.register(Grade, GradeAdmin)
admin.site.register(Employee, EmployeeAdmin)