"""
AI Assistant service using Groq API for travel recommendations and planning.
"""
from groq import Groq
from django.conf import settings


class TravelAIAssistant:
    """AI Assistant for travel planning using Groq"""
    
    def __init__(self, model_name='llama-3.3-70b-versatile'):
        """
        Initialize the AI assistant with Groq.
        
        Args:
            model_name: Name of the Groq model to use (default: llama-3.3-70b-versatile)
        """
        self.model_name = model_name
        # Initialize Groq client
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        
    def get_destination_recommendations(self, user_query):
        """
        Get destination recommendations based on user query.
        
        Args:
            user_query: User's travel preferences or query
            
        Returns:
            dict: AI recommendations with destinations and reasons
        """
        try:
            prompt = f"""You are a travel expert assistant. A user wants travel recommendations.

User Query: {user_query}

Based on this query, suggest 3-5 travel destinations with brief descriptions. Format your response as:

DESTINATION: [Name, Country]
REASON: [Why this destination fits their query]
BEST_TIME: [Best season to visit]
BUDGET: [Rough budget range in INR]

Keep each recommendation concise and focused."""

            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=1024
            )
            
            return {
                'success': True,
                'recommendations': response.choices[0].message.content,
                'query': user_query
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f'AI service error: {str(e)}',
                'recommendations': None
            }
    
    def generate_itinerary_plan(self, destination, days, interests):
        """
        Generate a detailed day-by-day itinerary plan.
        
        Args:
            destination: Destination name
            days: Number of days
            interests: User interests/preferences
            
        Returns:
            dict: Day-wise itinerary suggestions
        """
        try:
            prompt = f"""You are a travel planning expert. Create a detailed {days}-day itinerary for {destination}.

User Interests: {interests}

Create a day-by-day plan with:
- Morning, afternoon, and evening activities
- Must-visit attractions
- Local food recommendations
- Travel tips

Format as:
DAY 1:
Morning: [Activity]
Afternoon: [Activity]
Evening: [Activity]

DAY 2:
[Continue...]

Be specific and practical."""

            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=2048
            )
            
            return {
                'success': True,
                'itinerary': response.choices[0].message.content,
                'destination': destination,
                'days': days
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f'AI service error: {str(e)}',
                'itinerary': None
            }
    
    def enhance_destination_description(self, destination_name, current_description):
        """
        Enhance destination description with AI-generated insights.
        
        Args:
            destination_name: Name of the destination
            current_description: Current description
            
        Returns:
            dict: Enhanced description
        """
        try:
            prompt = f"""You are a travel writer. Enhance this destination description with interesting facts and tips.

Destination: {destination_name}
Current Description: {current_description}

Add 2-3 unique insights or travel tips that tourists should know. Keep it under 100 words."""

            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=512
            )
            
            return {
                'success': True,
                'enhanced_description': response.choices[0].message.content
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f'AI service error: {str(e)}',
                'enhanced_description': None
            }
    
    def get_travel_tips(self, destination, season):
        """
        Get AI-generated travel tips for a destination.
        
        Args:
            destination: Destination name
            season: Travel season
            
        Returns:
            dict: Travel tips and advice
        """
        try:
            prompt = f"""You are a travel advisor. Provide 5 practical travel tips for visiting {destination} during {season}.

Include tips about:
- What to pack
- Local customs
- Safety considerations
- Money-saving advice
- Must-try experiences

Keep each tip brief and actionable."""

            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=1024
            )
            
            return {
                'success': True,
                'tips': response.choices[0].message.content,
                'destination': destination
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f'AI service error: {str(e)}',
                'tips': None
            }
    
    def answer_travel_question(self, question, context=''):
        """
        Answer general travel-related questions.
        
        Args:
            question: User's question
            context: Optional context (e.g., specific destination)
            
        Returns:
            dict: AI-generated answer
        """
        try:
            context_text = f"\nContext: {context}" if context else ""
            
            prompt = f"""You are a helpful travel assistant. Answer this travel question clearly and concisely.

Question: {question}{context_text}

Provide a helpful, accurate response in 2-3 paragraphs."""

            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=1024
            )
            
            return {
                'success': True,
                'answer': response.choices[0].message.content,
                'question': question
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f'AI service error: {str(e)}',
                'answer': None
            }
    
    @staticmethod
    def check_groq_status():
        """
        Check if Groq API is configured and accessible.
        
        Returns:
            dict: Status information
        """
        try:
            api_key = settings.GROQ_API_KEY
            if api_key and api_key != '':
                return {
                    'available': True,
                    'models': ['llama-3.3-70b-versatile'],
                    'message': 'Groq API is configured'
                }
            else:
                return {
                    'available': False,
                    'models': [],
                    'message': 'Groq API key not configured'
                }
        except Exception as e:
            return {
                'available': False,
                'models': [],
                'message': f'Groq API error: {str(e)}'
            }


# Initialize default AI assistant
ai_assistant = TravelAIAssistant()
