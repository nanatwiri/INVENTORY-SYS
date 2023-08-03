import tkinter as tk


def add_item():
    item_name = entry_name.get()
    item_quantity = entry_quantity.get()
    # Add the item to the inventory system (you need to implement this function).

    # Optionally, you can display a message box to indicate successful addition.
    tk.messagebox.showinfo(
        "Success", f"Added {item_name} ({item_quantity} units) to the inventory.")


# Create the main window
root = tk.Tk()
root.title("Inventory System")

# Create labels, entries, and buttons
label_name = tk.Label(root, text="Product Name:")
entry_name = tk.Entry(root)
label_quantity = tk.Label(root, text="Quantity:")
entry_quantity = tk.Entry(root)
button_add = tk.Button(root, text="Add ItemProduct", command=add_item)

# Layout the widgets using grid
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name.grid(row=0, column=1, padx=5, pady=5)
label_quantity.grid(row=1, column=0, padx=5, pady=5)
entry_quantity.grid(row=1, column=1, padx=5, pady=5)
button_add.grid(row=2, columnspan=2, padx=5, pady=5)

# Start the main loop
root.mainloop()
