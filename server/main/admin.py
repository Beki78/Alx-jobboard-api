from django.contrib import admin
from .models import Job, Application


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "employmentType",
        "experienceLevel",
        "location",
        "posted_date",
    )
    search_fields = ("title", "description", "location")
    list_filter = ("employmentType", "experienceLevel", "location")


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("jobId","firstName","lastName","email", "appliedAt")
    search_fields = ("resume",)
    list_filter = ("appliedAt",)
