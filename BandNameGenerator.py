import tkinter as tk

def on_button_click():
    entry1_text = entry1.get()
    entry2_text = entry2.get()
    result_label.config(text=f"{entry1_text} {entry2_text}")

# Create the main window
window = tk.Tk()
window.title("Welcome to the Band Name Generator.")

# Create the first entry widget
entry1_label = tk.Label(window, text="What's the name of the city you grew up in?")
entry1_label.grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=10, pady=10)

# Create the second entry widget
entry2_label = tk.Label(window, text="What's the name of your pet?")
entry2_label.grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create a button to trigger an action
button = tk.Button(window, text="Name Reveal", command=on_button_click)
button.grid(row=2, column=0, columnspan=2, pady=10)

# Display the result
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Start the GUI event loop
window.mainloop()

