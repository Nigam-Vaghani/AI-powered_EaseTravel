from django.db import models


class Destination(models.Model):
    """Model representing a travel destination"""
    name = models.CharField(max_length=200, help_text="Name of the destination")
    country = models.CharField(max_length=100, help_text="Country where the destination is located")
    description = models.TextField(help_text="Description of the destination")
    avg_budget = models.IntegerField(help_text="Average budget in INR")
    best_season = models.CharField(
        max_length=50,
        help_text="Best season to visit (e.g., Summer, Winter, Monsoon)",
        choices=[
            ('Spring', 'Spring (March-May)'),
            ('Summer', 'Summer (June-August)'),
            ('Autumn', 'Autumn (September-November)'),
            ('Winter', 'Winter (December-February)'),
            ('Year-round', 'Year-round'),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'

    def __str__(self):
        return f"{self.name}, {self.country}"
