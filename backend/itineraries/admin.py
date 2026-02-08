from django.contrib import admin
from .models import Itinerary, DayPlan


class DayPlanInline(admin.TabularInline):
    """Inline admin for DayPlan within Itinerary"""
    model = DayPlan
    extra = 1
    fields = ('day_number', 'plan')


@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    """Admin interface for Itinerary model"""
    list_display = ('title', 'user', 'destination', 'start_date', 'days', 'created_at')
    list_filter = ('destination', 'start_date', 'created_at')
    search_fields = ('title', 'user__username', 'destination__name')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [DayPlanInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'destination', 'title')
        }),
        ('Travel Dates', {
            'fields': ('start_date', 'days')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(DayPlan)
class DayPlanAdmin(admin.ModelAdmin):
    """Admin interface for DayPlan model"""
    list_display = ('itinerary', 'day_number', 'plan_preview', 'created_at')
    list_filter = ('itinerary__destination', 'created_at')
    search_fields = ('itinerary__title', 'plan')
    ordering = ('itinerary', 'day_number')
    
    def plan_preview(self, obj):
        """Show first 50 characters of the plan"""
        return obj.plan[:50] + '...' if len(obj.plan) > 50 else obj.plan
    plan_preview.short_description = 'Plan Preview'
