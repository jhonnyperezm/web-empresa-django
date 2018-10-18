from django.contrib import admin
from .models import Service

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    #con esto decimo que esos campos solo sean de lectura
    readonly_fields =('created','update')
admin.site.register(Service,ServiceAdmin)