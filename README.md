# Travel Planner Application 🌍✈️

A Django-based web application for planning travel itineraries with **AI-powered recommendations** and weather information.

> 🤖 **NEW**: Now includes intelligent AI assistant powered by Ollama for personalized travel recommendations, smart itinerary planning, and expert destination insights!

## Features

### Core Features
- User Authentication (Signup, Login, Logout)
- Browse Destinations
- View Weather Information for Destinations
- Create and Manage Personal Itineraries
- Day-wise Travel Planning
- Admin Panel for Managing Content

### 🆕 AI-Powered Features
- **AI Travel Assistant**: Ask questions and get personalized destination recommendations
- **Smart Itinerary Planner**: AI-generated day-by-day travel plans based on your interests
- **Destination Insights**: Expert AI tips for best times to visit, attractions, and local culture
- **Natural Language Queries**: Chat with AI about travel plans in plain English

## Tech Stack

- **Backend**: Python 3.10+, Django 5.2, Django REST Framework
- **Frontend**: Django Templates, Bootstrap 5, HTML5, CSS3
- **Database**: SQLite
- **APIs**: OpenWeatherMap API
- **AI**: Ollama (Local LLM integration)
- **UI**: Modern gradient design with smooth animations

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux/Mac
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Ollama (For AI Features)

**Install Ollama**:
- Download from: https://ollama.ai/download
- Install and run: `ollama serve`

**Download a model**:
```bash
ollama pull llama2
```

**Test the model**:
```bash
ollama run llama2
```

*Note: AI features will gracefully degrade if Ollama is not available.*

### 4. Configure Environment Variables

Copy `.env.example` to `.env` and update with your values:

```bash
cp .env.example .env
```

Get your free OpenWeatherMap API key from: https://openweathermap.org/api

### 4. Run Migrations

```bash
cd backend
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to access the application.

## Admin Panel

Access the admin panel at http://127.0.0.1:8000/admin/

Use the superuser credentials you created to log in.

## Project Structure

```
travel_planner/
├── backend/                 # Django project
│   ├── backend/            # Project settings
│   ├── users/              # User authentication app
│   ├── destinations/       # Destinations management
│   ├── itineraries/        # Itinerary planning
│   ├── weather/            # Weather API integration
│   ├── ai_assistant.py     # 🤖 AI service class (Ollama integration)
│   ├── ai_views.py         # 🤖 AI-powered views
│   └── templates/          # HTML templates
│       ├── ai/             # 🤖 AI feature templates
│       ├── destinations/
│       ├── itineraries/
│       └── users/
├── requirements.txt
├── .env.example
├── README.md
├── SETUP_GUIDE.md
└── AI_FEATURES_GUIDE.md    # 🤖 Comprehensive AI features documentation
```

## Usage

### Standard Features
1. **Sign Up**: Create a new account
2. **Browse Destinations**: View available travel destinations
3. **Check Weather**: See current weather for each destination
4. **Create Itinerary**: Plan your trip with day-wise activities
5. **Manage Plans**: View and edit your itineraries

### 🤖 AI Features
1. **AI Assistant** (Navigation → AI Assistant)
   - Ask travel questions
   - Get destination recommendations
   - Receive personalized advice

2. **AI Itinerary Planner** (User Menu → AI Planner)
   - Select destination and trip duration
   - Enter your interests
   - Get AI-generated day-by-day plans

3. **AI Insights** (On any destination page)
   - Click "AI Insights" button
   - Get expert tips on best times to visit
   - Learn about local customs and attractions

📚 **For detailed AI features documentation, see [AI_FEATURES_GUIDE.md](AI_FEATURES_GUIDE.md)**

## API Integration

The application integrates with:
- **OpenWeatherMap API**: Real-time weather data (requires API key in `.env` file)
- **Ollama**: Local AI model for intelligent recommendations (requires local installation)
