import tkinter as tk
from tkinter import ttk

def create_window():
    main_window = tk.Tk()
    menubar = tk.Menu(main_window)

    main_window.config(menu=menubar)
    return main_window
