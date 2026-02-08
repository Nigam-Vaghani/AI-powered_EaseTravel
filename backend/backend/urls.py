"""
URL configuration for backend project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
import ai_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/', include('users.urls')),
    path('destinations/', include('destinations.urls')),
    path('itineraries/', include('itineraries.urls')),
    
    # AI-powered features
    path('ai-assistant/', ai_views.ai_travel_assistant, name='ai-assistant'),
    path('ai-planner/', ai_views.ai_itinerary_planner, name='ai-planner'),
    path('ai-insights/<int:destination_id>/', ai_views.ai_destination_insights, name='ai-insights'),
]

# Customize admin site headers
admin.site.site_header = "Travel Planner Administration"
admin.site.site_title = "Travel Planner Admin"
admin.site.index_title = "Welcome to Travel Planner Admin"
