import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tkinter Basics")
root.geometry("300x200")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Create an entry widget
entry = tk.Entry(root)
entry.pack()

# Function to show message box
def show_message():
    message = entry.get()
    messagebox.showinfo("Message", message)

# Create a button
button = tk.Button(root, text="Show Message", command=show_message)
button.pack()

# Start the main event loop
root.mainloop()
