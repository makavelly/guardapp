from django.contrib import admin

from .models import Employee
from .models import Chief
from .models import PageContent

admin.site.register(Employee)
admin.site.register(Chief)
admin.site.register(PageContent)
