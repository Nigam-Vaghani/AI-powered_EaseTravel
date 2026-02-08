from rest_framework import serializers
from .models import Itinerary, DayPlan


class DayPlanSerializer(serializers.ModelSerializer):
    """Serializer for DayPlan model"""
    
    class Meta:
        model = DayPlan
        fields = ['id', 'day_number', 'plan', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class ItinerarySerializer(serializers.ModelSerializer):
    """Serializer for Itinerary model"""
    day_plans = DayPlanSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    destination_name = serializers.CharField(source='destination.name', read_only=True)
    end_date = serializers.DateField(read_only=True)
    
    class Meta:
        model = Itinerary
        fields = ['id', 'user', 'destination', 'destination_name', 'title', 
                 'start_date', 'days', 'end_date', 'day_plans', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']
