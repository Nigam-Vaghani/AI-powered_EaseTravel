from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets, permissions
from .models import Itinerary, DayPlan
from .serializers import ItinerarySerializer, DayPlanSerializer
from .forms import ItineraryForm, DayPlanForm


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow owners to edit their itineraries"""
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class ItineraryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing itineraries.
    Users can only view and edit their own itineraries.
    """
    serializer_class = ItinerarySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        """Return itineraries for the current user only"""
        return Itinerary.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Set the user when creating an itinerary"""
        serializer.save(user=self.request.user)


@login_required
def itinerary_list(request):
    """Display list of user's itineraries"""
    itineraries = Itinerary.objects.filter(user=request.user)
    context = {
        'itineraries': itineraries,
        'page_title': 'My Itineraries'
    }
    return render(request, 'itineraries/itinerary_list.html', context)


@login_required
def itinerary_create(request):
    """Create a new itinerary"""
    if request.method == 'POST':
        form = ItineraryForm(request.POST)
        if form.is_valid():
            itinerary = form.save(commit=False)
            itinerary.user = request.user
            itinerary.save()
            messages.success(request, 'Itinerary created successfully!')
            return redirect('itineraries:detail', pk=itinerary.pk)
    else:
        form = ItineraryForm()
    
    context = {
        'form': form,
        'page_title': 'Create Itinerary'
    }
    return render(request, 'itineraries/itinerary_form.html', context)


@login_required
def itinerary_detail(request, pk):
    """Display details of a specific itinerary"""
    itinerary = get_object_or_404(Itinerary, pk=pk, user=request.user)
    day_plans = itinerary.day_plans.all()
    
    context = {
        'itinerary': itinerary,
        'day_plans': day_plans,
        'page_title': itinerary.title
    }
    return render(request, 'itineraries/itinerary_detail.html', context)


@login_required
def itinerary_edit(request, pk):
    """Edit an existing itinerary"""
    itinerary = get_object_or_404(Itinerary, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = ItineraryForm(request.POST, instance=itinerary)
        if form.is_valid():
            form.save()
            messages.success(request, 'Itinerary updated successfully!')
            return redirect('itineraries:detail', pk=itinerary.pk)
    else:
        form = ItineraryForm(instance=itinerary)
    
    context = {
        'form': form,
        'itinerary': itinerary,
        'page_title': 'Edit Itinerary'
    }
    return render(request, 'itineraries/itinerary_form.html', context)


@login_required
def itinerary_delete(request, pk):
    """Delete an itinerary"""
    itinerary = get_object_or_404(Itinerary, pk=pk, user=request.user)
    
    if request.method == 'POST':
        itinerary.delete()
        messages.success(request, 'Itinerary deleted successfully!')
        return redirect('itineraries:list')
    
    context = {
        'itinerary': itinerary,
        'page_title': 'Delete Itinerary'
    }
    return render(request, 'itineraries/itinerary_confirm_delete.html', context)


@login_required
def dayplan_create(request, itinerary_pk):
    """Add a day plan to an itinerary"""
    itinerary = get_object_or_404(Itinerary, pk=itinerary_pk, user=request.user)
    
    if request.method == 'POST':
        form = DayPlanForm(request.POST)
        if form.is_valid():
            day_plan = form.save(commit=False)
            day_plan.itinerary = itinerary
            
            # Validate day number doesn't exceed itinerary days
            if day_plan.day_number > itinerary.days:
                messages.error(request, f'Day number cannot exceed {itinerary.days} days.')
            else:
                day_plan.save()
                messages.success(request, f'Day {day_plan.day_number} plan added!')
                return redirect('itineraries:detail', pk=itinerary.pk)
    else:
        # Pre-fill day_number with next available day
        existing_days = itinerary.day_plans.values_list('day_number', flat=True)
        next_day = 1
        for i in range(1, itinerary.days + 1):
            if i not in existing_days:
                next_day = i
                break
        form = DayPlanForm(initial={'day_number': next_day})
    
    context = {
        'form': form,
        'itinerary': itinerary,
        'page_title': f'Add Day Plan - {itinerary.title}'
    }
    return render(request, 'itineraries/dayplan_form.html', context)


@login_required
def dayplan_edit(request, pk):
    """Edit a day plan"""
    day_plan = get_object_or_404(DayPlan, pk=pk, itinerary__user=request.user)
    
    if request.method == 'POST':
        form = DayPlanForm(request.POST, instance=day_plan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Day plan updated successfully!')
            return redirect('itineraries:detail', pk=day_plan.itinerary.pk)
    else:
        form = DayPlanForm(instance=day_plan)
    
    context = {
        'form': form,
        'day_plan': day_plan,
        'itinerary': day_plan.itinerary,
        'page_title': f'Edit Day {day_plan.day_number}'
    }
    return render(request, 'itineraries/dayplan_form.html', context)


@login_required
def dayplan_delete(request, pk):
    """Delete a day plan"""
    day_plan = get_object_or_404(DayPlan, pk=pk, itinerary__user=request.user)
    itinerary = day_plan.itinerary
    
    if request.method == 'POST':
        day_plan.delete()
        messages.success(request, 'Day plan deleted successfully!')
        return redirect('itineraries:detail', pk=itinerary.pk)
    
    context = {
        'day_plan': day_plan,
        'itinerary': itinerary,
        'page_title': 'Delete Day Plan'
    }
    return render(request, 'itineraries/dayplan_confirm_delete.html', context)
