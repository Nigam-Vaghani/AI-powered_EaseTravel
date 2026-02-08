"""
AI-powered views for travel recommendations and planning.
"""
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ai_assistant import ai_assistant
from destinations.models import Destination


def ai_travel_assistant(request):
    """AI-powered travel assistant page"""
    result = None
    
    if request.method == 'POST':
        query = request.POST.get('query', '').strip()
        action = request.POST.get('action', 'recommend')
        
        if query:
            if action == 'recommend':
                result = ai_assistant.get_destination_recommendations(query)
            elif action == 'question':
                result = ai_assistant.answer_travel_question(query)
            
            if result and not result.get('success'):
                messages.error(request, result.get('error', 'AI service unavailable'))
        else:
            messages.warning(request, 'Please enter your travel query.')
    
    # Check if Groq API is available
    groq_status = ai_assistant.check_groq_status()
    
    context = {
        'result': result,
        'groq_status': groq_status,
        'page_title': 'AI Travel Assistant'
    }
    return render(request, 'ai/ai_assistant.html', context)


@login_required
def ai_itinerary_planner(request):
    """AI-powered itinerary planning"""
    result = None
    destinations = Destination.objects.all()
    
    if request.method == 'POST':
        destination = request.POST.get('destination', '').strip()
        days = request.POST.get('days', '').strip()
        interests = request.POST.get('interests', '').strip()
        
        if destination and days and interests:
            try:
                days_int = int(days)
                result = ai_assistant.generate_itinerary_plan(
                    destination, 
                    days_int, 
                    interests
                )
                
                if result and not result.get('success'):
                    messages.error(request, result.get('error', 'AI service unavailable'))
                elif result and result.get('success'):
                    messages.success(request, 'AI itinerary generated! You can use this to create your trip.')
            except ValueError:
                messages.error(request, 'Please enter a valid number of days.')
        else:
            messages.warning(request, 'Please fill in all fields.')
    
    context = {
        'result': result,
        'destinations': destinations,
        'page_title': 'AI Itinerary Planner'
    }
    return render(request, 'ai/ai_itinerary_planner.html', context)


def ai_destination_insights(request, destination_id):
    """Get AI-generated insights for a specific destination"""
    destination = Destination.objects.get(pk=destination_id)
    
    # Generate travel tips
    tips_result = ai_assistant.get_travel_tips(
        destination.name, 
        destination.best_season
    )
    
    context = {
        'destination': destination,
        'ai_tips': tips_result,
        'page_title': f'AI Insights - {destination.name}'
    }
    return render(request, 'ai/ai_insights.html', context)
