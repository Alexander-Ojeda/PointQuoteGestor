# parts.py
import tkinter as tk

def create_parts_frame(parent):
    # Limpiar cualquier contenido anterior
    for widget in parent.winfo_children():
        widget.destroy()

