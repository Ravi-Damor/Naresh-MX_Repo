from django.contrib import admin

from . models import RegisterEmployee

@admin.register(RegisterEmployee)
class RegisterEmpAdmin(admin.ModelAdmin):
    list_display = ('user', 'address','age')