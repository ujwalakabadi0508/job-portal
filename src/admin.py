from django.contrib import admin
from .models import *




admin.site.register(job_category)
admin.site.register(city)
admin.site.register(applied_job)

@admin.register(new_job)
class NewJobAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'salary', 'company', 'created_at')
    list_filter = ('city', 'salary', 'created_at')
    search_fields = ('title', 'company', 'category__name')


@admin.register(candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')


