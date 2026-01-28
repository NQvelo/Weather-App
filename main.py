
import tkinter as tk
from src.ui.window_setup import WeatherApp

def main():
    root = tk.Tk()
    WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
