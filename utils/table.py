import tkinter as tk
from tkinter import ttk

def create_table(parent_frame, df):

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"), foreground="green", background="blue")

    tree = ttk.Treeview(parent_frame, show='headings')

    tree["columns"] = tuple(df.columns)

    for col in df.columns:
        tree.heading(col, text=col)

    for col in df.columns:
        tree.column(col, width=100, anchor="center")

    for row in df.itertuples(index=False, name=None):
        tree.insert("", "end", values=row)

    scrollbar = tk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")

    tree.pack(side="left", fill=tk.BOTH, expand=True)

    return tree