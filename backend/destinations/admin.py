from django.contrib import admin
from .models import Destination


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    """Admin interface for Destination model"""
    list_display = ('name', 'country', 'avg_budget', 'best_season', 'created_at')
    list_filter = ('country', 'best_season', 'created_at')
    search_fields = ('name', 'country', 'description')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'country', 'description')
        }),
        ('Travel Details', {
            'fields': ('avg_budget', 'best_season')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
