"""
Weather API utility functions for fetching weather data from OpenWeatherMap API.
"""
import requests
from django.conf import settings


def get_weather_data(city_name):
    """
    Fetch current weather data for a given city from OpenWeatherMap API.
    
    Args:
        city_name (str): Name of the city to fetch weather for
        
    Returns:
        dict: Weather data containing temperature, description, icon, etc.
              Returns None if API key is not configured or request fails
    """
    api_key = settings.OPENWEATHER_API_KEY
    
    # Check if API key is configured
    if not api_key or api_key == '':
        return {
            'error': True,
            'message': 'Weather API key not configured. Please set OPENWEATHER_API_KEY in .env file.',
            'temp': 'N/A',
            'description': 'API key not configured',
            'icon': '01d'
        }
    
    try:
        # OpenWeatherMap API endpoint
        url = settings.OPENWEATHER_API_URL
        
        # Parameters for the API request
        params = {
            'q': city_name,
            'appid': api_key,
            'units': 'metric'  # Use metric units (Celsius)
        }
        
        # Make the API request
        response = requests.get(url, params=params, timeout=5)
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Extract relevant weather information
            weather_info = {
                'error': False,
                'temp': round(data['main']['temp']),
                'temp_min': round(data['main']['temp_min']),
                'temp_max': round(data['main']['temp_max']),
                'feels_like': round(data['main']['feels_like']),
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'].capitalize(),
                'icon': data['weather'][0]['icon'],
                'wind_speed': data['wind']['speed'],
                'city': data['name'],
                'country': data['sys']['country']
            }
            
            return weather_info
        
        elif response.status_code == 404:
            return {
                'error': True,
                'message': f'City "{city_name}" not found in weather database.',
                'temp': 'N/A',
                'description': 'City not found',
                'icon': '01d'
            }
        
        elif response.status_code == 401:
            return {
                'error': True,
                'message': 'Invalid API key. Please check OPENWEATHER_API_KEY in .env file.',
                'temp': 'N/A',
                'description': 'Invalid API key',
                'icon': '01d'
            }
        
        else:
            return {
                'error': True,
                'message': f'Weather service error (Status: {response.status_code})',
                'temp': 'N/A',
                'description': 'Service unavailable',
                'icon': '01d'
            }
    
    except requests.exceptions.Timeout:
        return {
            'error': True,
            'message': 'Weather service timeout. Please try again later.',
            'temp': 'N/A',
            'description': 'Request timeout',
            'icon': '01d'
        }
    
    except requests.exceptions.RequestException as e:
        return {
            'error': True,
            'message': f'Error fetching weather data: {str(e)}',
            'temp': 'N/A',
            'description': 'Connection error',
            'icon': '01d'
        }
    
    except Exception as e:
        return {
            'error': True,
            'message': f'Unexpected error: {str(e)}',
            'temp': 'N/A',
            'description': 'Error',
            'icon': '01d'
        }


def get_weather_icon_url(icon_code):
    """
    Generate the full URL for a weather icon from OpenWeatherMap.
    
    Args:
        icon_code (str): Icon code from OpenWeatherMap API
        
    Returns:
        str: Full URL to the weather icon image
    """
    return f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
