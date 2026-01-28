"""
Backward-compatible entry point. Prefer: from src.ui.weather_app import WeatherApp
"""
import tkinter as tk

from .weather_app import WeatherApp

__all__ = ['WeatherApp']

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
