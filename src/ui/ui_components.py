"""
UI Components module - Handles all UI creation and styling
"""

from tkinter import Tk, Canvas, Label, StringVar, Button, PhotoImage
from tkinter import ttk
import randomcolor
import sys
from pathlib import Path

# Add parent directory to path to import config
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from config import (
    WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, RESIZABLE,
    FONT_TITLE, FONT_LABEL, FONT_LABEL_SMALL, FONT_BUTTON, FONT_DROPDOWN,
    HEADER_BG, SELECTOR_BG, CITY_LIST,
    HEADER_X, HEADER_Y, HEADER_WIDTH, HEADER_HEIGHT,
    SELECTOR_X, SELECTOR_Y, SELECTOR_WIDTH, SELECTOR_HEIGHT,
    SELECTOR_LABEL_X, SELECTOR_LABEL_WIDTH,
    WEATHER_DISPLAY_START_Y, WEATHER_DISPLAY_Y_OFFSET,
    LABEL_X, VALUE_X, DISPLAY_WIDTH, DISPLAY_HEIGHT,
    BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT,
    FOOTER_X, FOOTER_Y, FOOTER_WIDTH, FOOTER_HEIGHT
)

# ============================================================================
# GLOBAL UI REFERENCES
# ============================================================================
# These will be set during initialization

weather_label = None
description_label = None
temperature_label = None
pressure_label = None
humidity_label = None
city_name = None


# ============================================================================
# COLOR AND GRADIENT UTILITIES
# ============================================================================

def generate_gradient_colors():
    """
    Generate two random colors for gradient background.
    
    Returns:
        tuple: Two hex color strings (color1, color2)
    """
    color_generator = randomcolor.RandomColor()
    return color_generator.generate()[0], color_generator.generate()[0]


def create_diagonal_gradient(canvas, width, height, color1, color2):
    """
    Create a diagonal gradient from color1 to color2.
    
    Args:
        canvas (Canvas): Tkinter Canvas widget
        width (int): Width of the gradient
        height (int): Height of the gradient
        color1 (str): Starting color (hex format)
        color2 (str): Ending color (hex format)
    
    Returns:
        PhotoImage: Gradient image
    """
    gradient = PhotoImage(width=width, height=height)
    r1, g1, b1 = canvas.winfo_rgb(color1)
    r2, g2, b2 = canvas.winfo_rgb(color2)
    
    for i in range(width):
        nr = int(r1 + (r2 - r1) * (i / width))
        ng = int(g1 + (g2 - g1) * (i / width))
        nb = int(b1 + (b2 - b1) * (i / width))
        color = "#%04x%04x%04x" % (nr, ng, nb)
        gradient.put(color, to=(i, 0, i+1, height))
    
    return gradient


# ============================================================================
# WINDOW INITIALIZATION
# ============================================================================

def create_window():
    """
    Create and configure the main application window.
    
    Returns:
        Tk: The main window object
    """
    window = Tk()
    window.title(WINDOW_TITLE)
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    window.resizable(RESIZABLE, RESIZABLE)
    return window


def create_gradient_background(window, color1, color2):
    """
    Create and set a gradient background for the window.
    
    Args:
        window (Tk): The main window
        color1 (str): First gradient color
        color2 (str): Second gradient color
    
    Returns:
        tuple: (canvas, gradient) - The canvas and gradient image
    """
    canvas = Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    
    gradient = create_diagonal_gradient(canvas, WINDOW_WIDTH, WINDOW_HEIGHT, color1, color2)
    canvas.create_image(0, 0, anchor="nw", image=gradient)
    
    return canvas, gradient


# ============================================================================
# HEADER AND TITLE
# ============================================================================

def create_header(window):
    """
    Create the application header label.
    
    Args:
        window (Tk): The main window
    
    Returns:
        Label: The header label widget
    """
    header = Label(
        window,
        bg=HEADER_BG,
        text='Welcome to the Weather App',
        font=FONT_TITLE
    )
    header.place(x=HEADER_X, y=HEADER_Y, height=HEADER_HEIGHT, width=HEADER_WIDTH)
    return header


# ============================================================================
# CITY SELECTOR
# ============================================================================

def create_city_selector(window):
    """
    Create the city dropdown selector and its label.
    
    Args:
        window (Tk): The main window
    
    Returns:
        tuple: (city_dropdown, city_name_var) - The dropdown widget and StringVar
    """
    global city_name
    city_name = StringVar()
    
    # Selector label
    selector_label = Label(
        window,
        bg=SELECTOR_BG,
        text='Select',
        font=FONT_TITLE
    )
    selector_label.place(
        x=SELECTOR_LABEL_X,
        y=SELECTOR_Y,
        height=SELECTOR_HEIGHT - 4,
        width=SELECTOR_LABEL_WIDTH
    )
    
    # City dropdown
    city_dropdown = ttk.Combobox(
        window,
        textvariable=city_name,
        values=CITY_LIST,
        font=FONT_DROPDOWN,
        state='readonly'
    )
    city_dropdown.place(
        x=SELECTOR_X,
        y=SELECTOR_Y,
        height=SELECTOR_HEIGHT,
        width=SELECTOR_WIDTH
    )
    
    return city_dropdown, city_name


# ============================================================================
# WEATHER DISPLAY
# ============================================================================

def create_weather_display(window):
    """
    Create weather information display labels.
    
    Args:
        window (Tk): The main window
    
    Returns:
        dict: Dictionary of label references
    """
    global weather_label, description_label, temperature_label, pressure_label, humidity_label
    
    y_pos = WEATHER_DISPLAY_START_Y
    labels = {}
    
    # Weather Report
    Label(window, text='Weather Report', font=FONT_LABEL).place(
        x=LABEL_X, y=y_pos, height=DISPLAY_HEIGHT, width=DISPLAY_WIDTH
    )
    weather_label = Label(window, text='', font=FONT_LABEL)
    weather_label.place(x=VALUE_X, y=y_pos, height=DISPLAY_HEIGHT, width=DISPLAY_WIDTH)
    labels['weather'] = weather_label
    
    # Weather Description
    y_pos += WEATHER_DISPLAY_Y_OFFSET
    Label(window, text='Description', font=FONT_LABEL_SMALL).place(
        x=LABEL_X, y=y_pos, height=DISPLAY_HEIGHT, width=DISPLAY_WIDTH
    )
    description_label = Label(window, text='', font=FONT_LABEL_SMALL)
    description_label.place(x=VALUE_X, y=y_pos, height=DISPLAY_HEIGHT, width=DISPLAY_WIDTH)
    labels['description'] = description_label
    
    # Temperature
    y_pos += WEATHER_DISPLAY_Y_OFFSET
    Label(window, text='Temperature (°C)', font=FONT_LABEL).place(
        x=LABEL_X, y=y_pos, height=DISPLAY_HEIGHT, width=DISPLAY_WIDTH
    )
    temperature_label = Label(window, text='', font=FONT_LABEL)
    temperature_label.place(x=VALUE_X, y=y_pos, height=DISPLAY_HEIGHT, width=DISPLAY_WIDTH)
    labels['temperature'] = temperature_label
    
    # Pressure
    y_pos += WEATHER_DISPLAY_Y_OFFSET
    Label(window, text='Pressure (mb)', font=FONT_LABEL).place(
        x=LABEL_X, y=y_pos, height=DISPLAY_HEIGHT, width=DISPLAY_WIDTH
    )
    pressure_label = Label(window, text='', font=FONT_LABEL)
    pressure_label.place(x=VALUE_X, y=y_pos, height=DISPLAY_HEIGHT, width=DISPLAY_WIDTH)
    labels['pressure'] = pressure_label
    
    # Humidity
    y_pos += WEATHER_DISPLAY_Y_OFFSET
    Label(window, text='Humidity (%)', font=FONT_LABEL).place(
        x=LABEL_X, y=y_pos, height=DISPLAY_HEIGHT, width=DISPLAY_WIDTH
    )
    humidity_label = Label(window, text='', font=FONT_LABEL)
    humidity_label.place(x=VALUE_X, y=y_pos, height=DISPLAY_HEIGHT, width=DISPLAY_WIDTH)
    labels['humidity'] = humidity_label
    
    return labels


def update_weather_labels(weather_info, labels=None):
    """
    Update weather display labels with new data.
    
    Args:
        weather_info (dict): Weather information dictionary with keys:
                            - weather_condition
                            - description
                            - temperature
                            - pressure
                            - humidity
        labels (dict): Dictionary containing label references
    """
    if labels is None:
        labels = {
            'weather': weather_label,
            'description': description_label,
            'temperature': temperature_label,
            'pressure': pressure_label,
            'humidity': humidity_label
        }
    
    if weather_info is None:
        clear_weather_labels("City not found.", labels)
        return
    
    labels['weather'].config(text=weather_info['weather_condition'])
    labels['description'].config(text=weather_info['description'])
    labels['temperature'].config(text=str(weather_info['temperature']))
    labels['pressure'].config(text=str(weather_info['pressure']))
    labels['humidity'].config(text=str(weather_info['humidity']))


def clear_weather_labels(message="", labels=None):
    """
    Clear all weather display labels.
    
    Args:
        message (str): Optional message to display in weather condition label
        labels (dict): Dictionary containing label references
    """
    if labels is None:
        labels = {
            'weather': weather_label,
            'description': description_label,
            'temperature': temperature_label,
            'pressure': pressure_label,
            'humidity': humidity_label
        }
    
    labels['weather'].config(text=message)
    labels['description'].config(text="")
    labels['temperature'].config(text="")
    labels['pressure'].config(text="")
    labels['humidity'].config(text="")


# ============================================================================
# BUTTONS AND CONTROLS
# ============================================================================

def create_buttons(window, on_get_weather):
    """
    Create action buttons and footer.
    
    Args:
        window (Tk): The main window
        on_get_weather (callable): Callback function for Get Weather button
    
    Returns:
        Button: The Get Weather button widget
    """
    # Get Weather Button
    get_weather_btn = Button(
        window,
        text='Get Weather',
        font=FONT_BUTTON,
        command=on_get_weather,
        bg='#4CAF50',
        fg='white',
        activebackground='#45a049'
    )
    get_weather_btn.place(x=BUTTON_X, y=BUTTON_Y, height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    
    # Footer message
    footer = Label(
        window,
        text='🌤️  🌦️  ⛅  Enjoy the weather  🌤️  🌦️  ⛅',
        font=FONT_LABEL
    )
    footer.place(x=FOOTER_X, y=FOOTER_Y, height=FOOTER_HEIGHT, width=FOOTER_WIDTH)
    
    return get_weather_btn


# ============================================================================
# MAIN UI BUILDER
# ============================================================================

def build_ui(window, on_get_weather_callback):
    """
    Build the complete UI with all components.
    
    Args:
        window (Tk): The main window
        on_get_weather_callback (callable): Callback for Get Weather button
    
    Returns:
        dict: Dictionary containing all UI components
    """
    # Generate gradient colors
    color1, color2 = generate_gradient_colors()
    
    # Create background
    canvas, gradient = create_gradient_background(window, color1, color2)
    
    # Create UI components
    header = create_header(window)
    city_dropdown, city_name_var = create_city_selector(window)
    weather_display = create_weather_display(window)
    get_weather_btn = create_buttons(window, on_get_weather_callback)
    
    return {
        'canvas': canvas,
        'gradient': gradient,
        'header': header,
        'city_dropdown': city_dropdown,
        'city_name': city_name_var,
        'weather_display': weather_display,
        'get_weather_btn': get_weather_btn
    }
