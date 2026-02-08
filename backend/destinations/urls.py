from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'destinations'

# REST API Router
router = DefaultRouter()
router.register(r'api', views.DestinationViewSet, basename='destination-api')

urlpatterns = [
    # Template views
    path('', views.destination_list, name='list'),
    path('<int:pk>/', views.destination_detail, name='detail'),
    
    # API endpoints
    path('', include(router.urls)),
]
