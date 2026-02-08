# AI Features Guide - Travel Planner

## 🤖 Overview

Your Travel Planner application now includes intelligent AI-powered features using your locally installed Ollama model. The AI assistant can help you discover destinations, plan itineraries, get travel tips, and answer travel-related questions.

## 🎨 UI Enhancements

### Modern Design Elements
- **Gradient Color Scheme**: Beautiful purple-blue gradient (Primary: #667eea, Secondary: #764ba2)
- **Smooth Animations**: Card hover effects, pulsing AI badges, smooth transitions
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Enhanced Typography**: Improved readability with better spacing and font weights

### Navigation Updates
- **AI Assistant** link in main navigation with animated AI badge
- **AI Planner** link in user menu for authenticated users
- **AI Insights** buttons on destination detail pages

## 🚀 AI Features

### 1. AI Travel Assistant (`/ai-assistant/`)
**Purpose**: Your personal AI travel consultant

**Features**:
- Ask any travel-related questions
- Get personalized destination recommendations
- Receive travel tips and advice
- Natural language conversation interface

**How to Use**:
1. Navigate to AI Assistant from the main navigation
2. Check if Ollama is running (green badge = active, red badge = inactive)
3. Choose between:
   - **Destination Recommendations**: Get AI-suggested places to visit
   - **General Question**: Ask anything about travel
4. Type your query (e.g., "Suggest tropical beach destinations" or "What should I pack for winter hiking?")
5. Click "Get AI Response"

**Example Queries**:
- "Recommend destinations for adventure sports"
- "Best places to visit in summer?"
- "What are some budget-friendly family vacation spots?"
- "Tips for first-time solo travelers"

### 2. AI Itinerary Planner (`/ai-planner/`)
**Purpose**: Generate detailed day-by-day travel plans

**Features**:
- Select destination from your database
- Specify trip duration (number of days)
- Add interests and preferences
- Get AI-generated daily itineraries

**How to Use**:
1. Log in to your account (required)
2. Go to AI Planner from the user menu
3. Select a destination from the dropdown
4. Enter number of days (e.g., 5)
5. Add interests (e.g., "beaches, local food, museums, nightlife")
   - Use quick-add buttons: Culture, Adventure, Food, Relaxation, Nightlife, Shopping
6. Click "Generate AI Itinerary"
7. Review the AI-generated day-by-day plan

**What You'll Get**:
- Daily activity schedule
- Recommended places to visit
- Timing suggestions
- Activity descriptions
- Travel tips specific to your interests

### 3. AI Destination Insights (`/ai-insights/<destination_id>/`)
**Purpose**: Get expert AI tips for specific destinations

**Features**:
- Best time to visit
- Must-see attractions
- Local customs and etiquette
- Food recommendations
- Budget estimates
- Safety tips

**How to Access**:
1. Browse destinations at `/destinations/`
2. Click on any destination
3. Click the "AI Insights" button (gradient button with star icon)
4. View AI-generated travel tips and insights

## ⚙️ Ollama Configuration

### Prerequisites
- Ollama must be installed on your system
- At least one language model must be downloaded

### Checking Ollama Status
1. Open terminal/PowerShell
2. Run: `ollama list` (to see installed models)
3. Run: `ollama run llama2` (or your preferred model)

### Changing the AI Model
By default, the application uses the **llama2** model. To change it:

1. Open `backend/ai_assistant.py`
2. Find the `__init__` method (around line 18)
3. Change the model name:
   ```python
   def __init__(self, model_name: str = "llama3.2:latest"):  # Change here
       self.model_name = model_name
   ```

4. Save the file
5. Restart the Django server

### Supported Models
Any Ollama model works! Popular choices:
- `llama2` (default)
- `llama3.2:latest`
- `mistral`
- `codellama`
- `mixtral`
- `phi3`
- `gemma2`

### Installing New Models
```bash
# Install a specific model
ollama pull llama3.2

# Run the model to verify
ollama run llama3.2

# List all installed models
ollama list
```

## 🛠️ Troubleshooting

### AI Features Not Working
**Problem**: "Ollama service is not available" message
**Solutions**:
1. Start Ollama service: `ollama serve`
2. Verify model is installed: `ollama list`
3. Check Ollama is running on default port (11434)

### Slow AI Responses
**Problem**: AI takes a long time to respond
**Solutions**:
1. Use a smaller model (e.g., `phi3` instead of `llama2`)
2. Ensure Ollama has enough system resources (RAM)
3. Close other resource-intensive applications

### Model Not Found Error
**Problem**: "Model 'llama2' not found"
**Solutions**:
1. Install the model: `ollama pull llama2`
2. Or change to an installed model in `ai_assistant.py`

### Unicode Errors in Responses
**Problem**: Special characters display incorrectly
**Solution**: Already handled by the application (using UTF-8 encoding)

## 📱 Using the Features

### Quick Start Workflow
1. **Start Ollama**: `ollama serve` (in a separate terminal)
2. **Start Django**: `python manage.py runserver` (from backend directory)
3. **Browse to**: http://127.0.0.1:8000
4. **Log in** with your credentials
5. **Try AI Features**:
   - Click "AI Assistant" to ask questions
   - Click "AI Planner" to generate itineraries
   - View any destination and click "AI Insights"

### Best Practices
- **Be specific**: More detailed queries get better AI responses
- **Use context**: Mention preferences, budget, time of year
- **Iterate**: Refine your queries based on initial responses
- **Combine features**: Use AI Assistant → AI Planner → Create Itinerary workflow

## 🎯 Feature Integration

### With Existing Features
The AI features complement the existing functionality:

1. **Destinations**: View destinations → AI Insights → Manual itinerary creation
2. **Itineraries**: AI Planner suggestions → Create/edit itinerary → Add day plans
3. **Weather**: Check weather for AI-recommended destinations
4. **User Accounts**: AI features are personalized for logged-in users

### API Integration (Future)
The AI features are built on the same REST API foundation:
- Endpoints can be accessed via API (add `/api/` prefix)
- Perfect for future mobile app integration
- JSON responses available for all AI features

## 📊 Technical Details

### AI Service Architecture
- **Backend**: `ai_assistant.py` - Core AI service class
- **Views**: `ai_views.py` - Django views for AI features
- **Templates**: `templates/ai/` - User interface pages
- **Integration**: Ollama Python client library (v0.6.1)

### Performance Optimization
- Graceful error handling (continues working even if Ollama is down)
- Timeout protection (prevents hanging requests)
- Response streaming (for faster perceived performance)
- Efficient model management

### Security Considerations
- AI features require authentication for personalized responses
- No sensitive data sent to AI (only destination names and user interests)
- Local AI model (data never leaves your machine)
- CSRF protection on all forms

## 🌟 Tips for Best Results

### Query Optimization
✅ **Good Queries**:
- "Suggest beach destinations in Southeast Asia with good diving"
- "Plan a 7-day cultural trip to Europe with focus on architecture"
- "What are the best food markets in Tokyo?"

❌ **Poor Queries**:
- "trip"
- "help"
- "suggestions"

### Interest Keywords
For AI Planner, use specific interests:
- **Culture**: museums, art, history, architecture
- **Adventure**: hiking, diving, climbing, sports
- **Food**: restaurants, markets, street food, cuisine
- **Nature**: parks, beaches, mountains, wildlife
- **Urban**: shopping, nightlife, hotels, entertainment

## 📞 Support

### Getting Help
1. Check Ollama documentation: https://github.com/ollama/ollama
2. Verify Django logs for errors
3. Test Ollama independently: `ollama run llama2`

### Common Issues
| Issue | Solution |
|-------|----------|
| AI not responding | Restart Ollama service |
| Wrong recommendations | Refine your query with more details |
| Outdated info | AI uses training data; verify current info |
| Incomplete itinerary | Increase number of days or simplify interests |

---

## 🎉 Enjoy Your Enhanced Travel Planner!

Your application now combines:
- ✨ Beautiful modern UI with gradients and animations
- 🤖 Intelligent AI-powered recommendations
- 📅 Smart itinerary planning
- 💡 Expert travel insights
- 🌐 Comprehensive destination database

**Happy Traveling! 🌍✈️**
