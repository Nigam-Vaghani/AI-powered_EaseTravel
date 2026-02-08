from rest_framework import serializers
from .models import Destination


class DestinationSerializer(serializers.ModelSerializer):
    """Serializer for Destination model"""
    
    class Meta:
        model = Destination
        fields = ['id', 'name', 'country', 'description', 'avg_budget', 
                 'best_season', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
