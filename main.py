<<<<<<< HEAD
"""
Main application entry point for the Weather App
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from tkinter import Tk
from ui.ui_components import create_window, build_ui, update_weather_labels
from api.weather_api import get_weather_info


# ============================================================================
# EVENT HANDLERS
# ============================================================================

class WeatherApp:
    """Main Weather Application class."""
    
    def __init__(self):
        """Initialize the application."""
        self.window = None
        self.ui_components = None
        self.city_name_var = None
        self.weather_labels = None
    
    def on_get_weather(self):
        """
        Handle Get Weather button click.
        Fetches weather data and updates the display.
        """
        if self.city_name_var is None:
            return
        
        city = self.city_name_var.get()
        
        if not city:
            update_weather_labels(None, self.weather_labels)
            return
        
        print(f"Fetching weather for: {city}")
        
        # Fetch and display weather information
        weather_info = get_weather_info(city)
        
        if weather_info:
            print(f"Weather data fetched: {weather_info}")
        else:
            print("Failed to fetch weather data")
        
        update_weather_labels(weather_info, self.weather_labels)
    
    def run(self):
        """
        Initialize and run the Weather App.
        """
        # Create main window
        self.window = create_window()
        
        # Build UI with callback
        self.ui_components = build_ui(self.window, self.on_get_weather)
        
        # Store references
        self.city_name_var = self.ui_components['city_name']
        self.weather_labels = self.ui_components['weather_display']
        
        # Start the application
        self.window.mainloop()


# ============================================================================
# APPLICATION ENTRY POINT
# ============================================================================

def main():
    """Main entry point."""
    app = WeatherApp()
    app.run()


if __name__ == '__main__':
=======

import tkinter as tk
from src.ui.window_setup import WeatherApp
from src.ui.weather_controller import WeatherController

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
>>>>>>> e045f3c (Update main entry point)
    main()
