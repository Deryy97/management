from django.contrib import admin
from .models import Employer


class EmployerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'id_card', 'birthday', 'phone', 'email')


admin.site.register(Employer, EmployerAdmin)