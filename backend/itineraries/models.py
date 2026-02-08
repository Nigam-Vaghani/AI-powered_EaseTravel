from django.db import models
from django.contrib.auth.models import User
from destinations.models import Destination


class Itinerary(models.Model):
    """Model representing a user's travel itinerary"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='itineraries')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='itineraries')
    title = models.CharField(max_length=200, help_text="Title of the itinerary")
    start_date = models.DateField(help_text="Start date of the trip")
    days = models.PositiveIntegerField(help_text="Number of days for the trip")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Itinerary'
        verbose_name_plural = 'Itineraries'

    def __str__(self):
        return f"{self.title} - {self.user.username}"

    @property
    def end_date(self):
        """Calculate end date based on start date and number of days"""
        from datetime import timedelta
        return self.start_date + timedelta(days=self.days - 1)


class DayPlan(models.Model):
    """Model representing a day-wise plan within an itinerary"""
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='day_plans')
    day_number = models.PositiveIntegerField(help_text="Day number in the itinerary")
    plan = models.TextField(help_text="Detailed plan for the day")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['day_number']
        unique_together = ['itinerary', 'day_number']
        verbose_name = 'Day Plan'
        verbose_name_plural = 'Day Plans'

    def __str__(self):
        return f"Day {self.day_number} - {self.itinerary.title}"
