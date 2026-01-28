"""
Sidebar UI: search, city list, and temperature unit switcher.
"""
import tkinter as tk
from types import SimpleNamespace

from .widgets import create_rounded_rect


def build_sidebar(parent, colors, cities, *,
                  on_city_click, on_search, on_unit_change, on_switcher_hover,
                  on_search_focus_in, on_search_focus_out):
    """
    Build the sidebar and return a namespace with widget references.

    Returns an object with: sidebar_search, city_buttons, unit_c_button, unit_f_button.
    """
    sidebar_canvas = tk.Canvas(
        parent, bg=colors['bg_dark'],
        highlightthickness=0, width=300
    )
    sidebar_canvas.grid(row=0, column=0, sticky='nsew', padx=30, pady=(30, 30))
    sidebar_canvas.grid_propagate(False)

    sidebar = tk.Frame(sidebar_canvas, bg=colors['sidebar_bg'], width=300)

    def draw_sidebar_bg(event=None):
        sidebar_canvas.delete("sidebar_bg")
        w = sidebar_canvas.winfo_width()
        h = sidebar_canvas.winfo_height()
        if w > 1 and h > 1:
            create_rounded_rect(
                sidebar_canvas, 0, 0, w, h, 10,
                fill=colors['sidebar_bg'], outline=colors['sidebar_bg']
            )

    sidebar_canvas.bind('<Configure>', draw_sidebar_bg)
    sidebar_window = sidebar_canvas.create_window(0, 0, window=sidebar, anchor='nw')

    def update_sidebar_size(event=None):
        w = sidebar_canvas.winfo_width()
        h = sidebar_canvas.winfo_height()
        if w > 1 and h > 1:
            sidebar.configure(width=w, height=h)
            sidebar_canvas.itemconfig(sidebar_window, width=w, height=h)
            draw_sidebar_bg()

    sidebar_canvas.bind('<Configure>', update_sidebar_size)
    sidebar.bind('<Configure>', lambda e: sidebar_canvas.configure(scrollregion=sidebar_canvas.bbox("all")))

    # Search
    search_frame = tk.Frame(sidebar, bg=colors['sidebar_bg'])
    search_frame.pack(fill='x', padx=10, pady=(10, 20))

    sidebar_search = tk.Entry(
        search_frame, font=('Arial', 11), bg=colors['bg_light'],
        fg=colors['text_primary'], insertbackground='white',
        relief='flat', bd=0
    )
    sidebar_search.pack(fill='x', ipady=8, padx=5)
    sidebar_search.insert(0, "  🔍 Search city...")
    sidebar_search.bind('<Return>', lambda e: on_search())
    sidebar_search.bind('<FocusIn>', on_search_focus_in)
    sidebar_search.bind('<FocusOut>', on_search_focus_out)

    # City list
    list_frame = tk.Frame(sidebar, bg=colors['sidebar_bg'])
    list_frame.pack(fill='both', expand=True, padx=10, pady=5)

    city_buttons = []
    for city in cities:
        btn_frame = tk.Frame(list_frame, bg=colors['card_bg'], bd=0)
        btn_frame.pack(fill='x', pady=3)

        btn = tk.Label(
            btn_frame, text=city, font=('Arial', 11), bg=colors['card_bg'],
            fg=colors['text_primary'], relief='flat', anchor='w',
            padx=15, pady=10, cursor='hand2'
        )
        btn.pack(fill='both')
        btn.bind('<Button-1>', lambda e, c=city: on_city_click(c))

        temp_label = tk.Label(
            btn_frame, text="--°", font=('Arial', 10),
            bg=colors['card_bg'], fg=colors['text_secondary']
        )
        temp_label.place(relx=0.85, rely=0.5, anchor='center')
        city_buttons.append((btn_frame, btn, temp_label, city))

    # Unit switcher
    switcher_container = tk.Frame(sidebar, bg=colors['sidebar_bg'])
    switcher_container.pack(fill='x', padx=10, pady=(10, 15))

    switcher_label = tk.Label(
        switcher_container, text="Temperature Unit", font=('Arial', 10),
        bg=colors['sidebar_bg'], fg=colors['text_secondary']
    )
    switcher_label.pack(pady=(0, 8))

    unit_switcher_frame = tk.Frame(switcher_container, bg=colors['card_bg'], relief='flat', bd=0)
    unit_switcher_frame.pack()

    unit_c_button = tk.Label(
        unit_switcher_frame, text="°C", font=('Arial', 13, 'bold'),
        bg=colors['accent'], fg=colors['text_primary'],
        relief='flat', padx=20, pady=8, cursor='hand2'
    )
    unit_c_button.pack(side='left')
    unit_c_button.bind('<Button-1>', lambda e: on_unit_change('celsius'))
    unit_c_button.bind('<Enter>', lambda e: on_switcher_hover('c', True))
    unit_c_button.bind('<Leave>', lambda e: on_switcher_hover('c', False))

    unit_f_button = tk.Label(
        unit_switcher_frame, text="°F", font=('Arial', 13, 'bold'),
        bg=colors['bg_light'], fg=colors['text_secondary'],
        relief='flat', padx=20, pady=8, cursor='hand2'
    )
    unit_f_button.pack(side='left')
    unit_f_button.bind('<Button-1>', lambda e: on_unit_change('fahrenheit'))
    unit_f_button.bind('<Enter>', lambda e: on_switcher_hover('f', True))
    unit_f_button.bind('<Leave>', lambda e: on_switcher_hover('f', False))

    return SimpleNamespace(
        sidebar_search=sidebar_search,
        city_buttons=city_buttons,
        unit_c_button=unit_c_button,
        unit_f_button=unit_f_button,
    )
