import tkinter as tk
import time
import threading

# Function to handle the "cool print" effect
def cool_print():
    alp = "abcdefghijklmnopqrstuvwxyz"
    inp = entry.get()  # Get input from the entry box
    res = ''
    j = 0
    while len(res) != len(inp):
        if inp[j] == ' ':
            res += ' '
            j += 1
        for i in alp:
            if i == inp[j]:
                res += i
                result_label['text'] = res  # Update the label with current result
                j += 1
                break
            else:
                time.sleep(0.07)
                result_label['text'] = res + i  # Show intermediate steps
                

# Function to run the cool print in a separate thread (to prevent UI freezing)
def start_cool_print(event=None):  # Add 'event' parameter to work with key binding
    threading.Thread(target=cool_print).start()

# Initialize tkinter
root = tk.Tk()
root.title("Cool String Printer code")

# Set window size (width x height)
root.geometry("500x300")

# Input field for the string
entry_label = tk.Label(root, text="Enter String:", font=("Helvetica", 12))
entry_label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Helvetica", 14))
entry.pack(pady=10)

# Button to trigger the cool print
print_button = tk.Button(root, text="Magic 🪄", font=("Helvetica", 12), command=start_cool_print)
print_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=10)

# Bind the Enter key to the start_cool_print function
root.bind('<Return>', start_cool_print)

# Run the tkinter event loop
root.mainloop()
