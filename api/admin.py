from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'complete', 'created', 'updated')
    list_filter = ('complete', 'created', 'updated')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('complete', 'updated', 'created')
    date_hierarchy = 'created'
    list_display_links = ('title', 'description', 'created', 'updated')
    actions = ('make_complete', 'make_incomplete')

    @admin.action(description='Mark selected tasks as complete')
    def make_complete(self, request, queryset):
        queryset.update(complete=True)

    @admin.action(description='Mark selected tasks as incomplete')
    def make_incomplete(self, request, queryset):
        queryset.update(complete=False)
