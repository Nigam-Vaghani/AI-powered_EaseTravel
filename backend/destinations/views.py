from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Destination
from .serializers import DestinationSerializer
from weather.utils import get_weather_data


class DestinationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for viewing destinations.
    Provides list and detail views via REST API.
    """
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


def destination_list(request):
    """Display list of all destinations"""
    destinations = Destination.objects.all()
    context = {
        'destinations': destinations,
        'page_title': 'Browse Destinations'
    }
    return render(request, 'destinations/destination_list.html', context)


def destination_detail(request, pk):
    """Display details of a specific destination with weather information"""
    destination = get_object_or_404(Destination, pk=pk)
    
    # Fetch weather data for the destination
    weather_data = get_weather_data(destination.name)
    
    context = {
        'destination': destination,
        'weather': weather_data,
        'page_title': destination.name
    }
    return render(request, 'destinations/destination_detail.html', context)
