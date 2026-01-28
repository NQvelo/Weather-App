# Weather API Testing & Integration Guide

## 📍 Where to Test the API

### Test Script
Run the test script to see what data the API returns:

```bash
# Activate virtual environment first
source venv/bin/activate

# Run the test script
python test_api.py
```

This will test the API with sample cities (Berlin, London) and show:
- Raw API response structure
- Parsed weather data
- Sunrise/Sunset times
- Visibility
- UV Index estimate

### API Endpoint
The API uses **OpenWeatherMap Current Weather Data API**:
- **URL**: `https://api.openweathermap.org/data/2.5/weather`
- **API Key**: Stored in `config.py`
- **Documentation**: https://openweathermap.org/current

### Test in Python Console
```python
from src.api.weather_api import get_weather_info

# Test with any city
data = get_weather_info("Berlin")
print(data)
```

## ✅ Integrated Features

### 1. **Sunrise & Sunset** ☀️🌙
- **Source**: OpenWeatherMap API (`sys.sunrise`, `sys.sunset`)
- **Format**: Unix timestamps converted to local time (e.g., "6:45 AM", "8:49 PM")
- **Status**: ✅ Fully integrated and working

### 2. **Visibility** 👁️
- **Source**: OpenWeatherMap API (`visibility`)
- **Format**: Converted from meters to kilometers (e.g., "10.0 km")
- **Status**: ✅ Fully integrated and working

### 3. **UV Index** ☀️
- **Source**: Estimated (OpenWeatherMap Current Weather API doesn't provide UV index)
- **Method**: Calculated based on:
  - Time of day (peak UV hours: 10 AM - 4 PM)
  - Weather conditions (Clear = higher UV, Cloudy = lower UV)
  - Daytime vs Nighttime
- **Format**: Categories like "High (7-9)", "Moderate (4-6)", "Low (2-4)", "None (Night)"
- **Status**: ✅ Estimated (for accurate UV index, would need One Call API 3.0)

## 📊 API Response Structure

The OpenWeatherMap API returns:
```json
{
  "coord": {...},
  "weather": [...],
  "base": "...",
  "main": {
    "temp": 277.68,      // Kelvin
    "pressure": 1025,
    "humidity": 54
  },
  "visibility": 10000,   // meters
  "wind": {...},
  "clouds": {...},
  "dt": 1234567890,
  "sys": {
    "sunrise": 1768806360,  // Unix timestamp
    "sunset": 1768836458    // Unix timestamp
  },
  "timezone": 3600,      // Offset from UTC in seconds
  "id": 123456,
  "name": "Berlin",
  "cod": 200
}
```

## 🔧 For Accurate UV Index

To get **real UV index data** (not estimated), you would need:

1. **OpenWeatherMap One Call API 3.0**
   - Requires subscription (paid)
   - Provides UV index, hourly forecasts, etc.
   - Endpoint: `https://api.openweathermap.org/data/3.0/onecall`

2. **Alternative APIs** (free options):
   - **WeatherAPI.com**: Free tier includes UV index
   - **Open-Meteo**: Free, open-source weather API

## 🚀 Usage in the App

The app now automatically displays:
- **Sunrise**: Real time from API
- **Sunset**: Real time from API  
- **Visibility**: Real distance in km
- **UV Index**: Estimated based on conditions

All data updates when you search for a new city!

## 📝 Files Modified

1. `src/api/weather_api.py` - Enhanced to parse sunrise, sunset, visibility, UV index
2. `src/ui/weather_controller.py` - Updated to pass new data fields
3. `src/ui/window_setup.py` - Updated UI to display real data instead of placeholders
4. `test_api.py` - New test script to verify API functionality
