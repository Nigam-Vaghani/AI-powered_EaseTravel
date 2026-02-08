from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'itineraries'

# REST API Router
router = DefaultRouter()
router.register(r'api', views.ItineraryViewSet, basename='itinerary-api')

urlpatterns = [
    # Template views
    path('', views.itinerary_list, name='list'),
    path('create/', views.itinerary_create, name='create'),
    path('<int:pk>/', views.itinerary_detail, name='detail'),
    path('<int:pk>/edit/', views.itinerary_edit, name='edit'),
    path('<int:pk>/delete/', views.itinerary_delete, name='delete'),
    
    # Day plan management
    path('<int:itinerary_pk>/dayplan/create/', views.dayplan_create, name='dayplan-create'),
    path('dayplan/<int:pk>/edit/', views.dayplan_edit, name='dayplan-edit'),
    path('dayplan/<int:pk>/delete/', views.dayplan_delete, name='dayplan-delete'),
    
    # API endpoints
    path('', include(router.urls)),
]
