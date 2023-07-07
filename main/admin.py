from django.contrib import admin

from .models.job import Job
from .models.customer import Customer


admin.site.register(Customer)
admin.site.register(Job)
