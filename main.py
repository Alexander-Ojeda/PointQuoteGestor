# main.py
import tkinter as tk
from parts_module.parts import create_parts_frame
from brands_module.brands import create_brands_frame
from utils.toparquet import leer_parquet
from utils.table import create_table

def main_window():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Point Quote App")
    root.geometry("1920x1080")

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    side_bar = tk.Frame(main_frame, bg="lightgray")
    side_bar.pack(side="left", fill="y", padx=10, pady=10)

    content = tk.Frame(main_frame, bg="white")
    content.pack(side="right", fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Funciones para cambiar el contenido del Frame
    def show_parts():
        create_parts_frame(content)
        df_parts = leer_parquet(r'parts_module\parts.parquet')
        create_table(content, df_parts)

    def show_brands():
        create_brands_frame(content)
        df_brands = leer_parquet(r'brands_module\brands.parquet')
        create_table(content, df_brands)

    # Función para mostrar el mensaje de bienvenida
    def show_welcome_message():
        # Limpiar cualquier contenido anterior
        for widget in content.winfo_children():
            widget.destroy()

        label = tk.Label(content, text="¡Bienvenido a la aplicación!", font=("Arial", 16))
        label.pack(padx=20, pady=20)

    # Botones para alternar entre los módulos
    btn_parts = tk.Button(side_bar, text="Ir a Parts", command=show_parts)
    btn_parts.pack(padx=10, pady=10)

    btn_brands = tk.Button(side_bar, text="Ir a Brands", command=show_brands)
    btn_brands.pack(padx=10, pady=10)

    # Mostrar el mensaje de bienvenida por defecto al iniciar la aplicación
    show_welcome_message()

    # Iniciar la interfaz gráfica
    root.mainloop()

if __name__ == "__main__":
    main_window()