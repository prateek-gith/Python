import tkinter as tk

def on_button_click():
    label.config(text="Hello, World!")

# Create the main application window
root = tk.Tk()
root.title("My Python Application")

# Create a label
label = tk.Label(root, text="Click the button to change me!")
label.pack()

# Create a button
button = tk.Button(root, text="Click me!", command=on_button_click)
button.pack()

# Start the main event loop
root.mainloop()
