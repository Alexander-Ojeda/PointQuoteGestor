# brands.py
import tkinter as tk

def create_brands_frame(parent):
    # Limpiar cualquier contenido anterior
    for widget in parent.winfo_children():
        widget.destroy()
