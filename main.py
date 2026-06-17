import tkinter as tk
from tkinter import ttk

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("450x420")
root.resizable(False, False)

# ---------------- STYLE ----------------
style = ttk.Style()
style.theme_use("clam")

# ---------------- TITLE ----------------
title = ttk.Label(
    root,
    text="Temperature Converter",
    font=("Segoe UI", 20, "bold")
)
title.pack(pady=(20, 15))

# ---------------- INPUT FRAME ----------------
frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

# Temperature Input
ttk.Label(
    frame,
    text="Enter Temperature",
    font=("Segoe UI", 11)
).pack(anchor="w")

temp_entry = ttk.Entry(
    frame,
    font=("Segoe UI", 12),
    width=30
)
temp_entry.pack(pady=(5, 15), fill="x")

# From Unit
ttk.Label(
    frame,
    text="From Unit",
    font=("Segoe UI", 11)
).pack(anchor="w")

from_unit = tk.StringVar(value="Celsius")

from_combo = ttk.Combobox(
    frame,
    textvariable=from_unit,
    values=["Celsius", "Fahrenheit", "Kelvin"],
    state="readonly"
)
from_combo.pack(pady=(5, 15), fill="x")

# To Unit
ttk.Label(
    frame,
    text="To Unit",
    font=("Segoe UI", 11)
).pack(anchor="w")

to_unit = tk.StringVar(value="Fahrenheit")

to_combo = ttk.Combobox(
    frame,
    textvariable=to_unit,
    values=["Celsius", "Fahrenheit", "Kelvin"],
    state="readonly"
)
to_combo.pack(pady=(5, 20), fill="x")

# Result Label
result_label = ttk.Label(
    frame,
    text="Result: --",
    font=("Segoe UI", 13, "bold")
)
result_label.pack(pady=10)

# ---------------- FUNCTIONS ----------------
def convert():
    try:
        temp = float(temp_entry.get())

        source = from_unit.get()
        target = to_unit.get()

        # Same unit
        if source == target:
            result = temp

        # Celsius conversions
        elif source == "Celsius" and target == "Fahrenheit":
            result = (temp * 9 / 5) + 32

        elif source == "Celsius" and target == "Kelvin":
            result = temp + 273.15

        # Fahrenheit conversions
        elif source == "Fahrenheit" and target == "Celsius":
            result = (temp - 32) * 5 / 9

        elif source == "Fahrenheit" and target == "Kelvin":
            result = (temp - 32) * 5 / 9 + 273.15

        # Kelvin conversions
        elif source == "Kelvin" and target == "Celsius":
            result = temp - 273.15

        elif source == "Kelvin" and target == "Fahrenheit":
            result = (temp - 273.15) * 9 / 5 + 32

        # Unit symbol
        symbols = {
            "Celsius": "°C",
            "Fahrenheit": "°F",
            "Kelvin": "K"
        }

        result_label.config(
            text=f"Result: {result:.2f} {symbols[target]}"
        )

    except ValueError:
        result_label.config(
            text="Please enter a valid number"
        )


def clear():
    temp_entry.delete(0, tk.END)
    from_combo.set("Celsius")
    to_combo.set("Fahrenheit")
    result_label.config(text="Result: --")

# ---------------- BUTTONS ----------------
button_frame = ttk.Frame(frame)
button_frame.pack(pady=10)

convert_btn = ttk.Button(
    button_frame,
    text="Convert",
    command=convert
)
convert_btn.grid(row=0, column=0, padx=5)

clear_btn = ttk.Button(
    button_frame,
    text="Clear",
    command=clear
)
clear_btn.grid(row=0, column=1, padx=5)

# ---------------- RUN ----------------
root.mainloop()