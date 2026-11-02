from django.contrib import admin

# Register your models here.
from .models import Training,Enrollment
admin.site.register(Enrollment)
admin.site.register(Training)

