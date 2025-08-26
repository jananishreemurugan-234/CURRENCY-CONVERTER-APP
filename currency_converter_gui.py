import tkinter as tk
from tkinter import ttk

rates = {"USD": 1.0, "INR": 83.0, "EUR": 0.92, "GBP": 0.78, "JPY": 146.5}

def convert():
    amount = float(amount_entry.get())
    source = source_currency.get()
    target = target_currency.get()
    usd = amount / rates[source]
    result = usd * rates[target]
    output_label.config(text=f"Converted Amount: {result:.2f} {target}")

root = tk.Tk()
root.title("Currency Converter")

tk.Label(root, text="Amount").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="From").grid(row=1, column=0)
source_currency = ttk.Combobox(root, values=list(rates.keys()))
source_currency.current(0)
source_currency.grid(row=1, column=1)

tk.Label(root, text="To").grid(row=2, column=0)
target_currency = ttk.Combobox(root, values=list(rates.keys()))
target_currency.current(1)
target_currency.grid(row=2, column=1)

tk.Button(root, text="Convert", command=convert).grid(row=3, column=0, columnspan=2)
output_label = tk.Label(root, text="Converted Amount: ")
output_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
