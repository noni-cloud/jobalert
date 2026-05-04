from django.contrib import admin
from .models import Job, JobSeeker, JobAlert

admin.site.register(Job)
admin.site.register(JobSeeker)
admin.site.register(JobAlert)
