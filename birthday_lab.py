# Import the tkinter library for creating the GUI
import tkinter as tk
# Import the messagebox module from tkinter to show pop-up messages
from tkinter import messagebox
# Import the datetime module to work with dates and times
from datetime import datetime
# Import the random module to generate random colors for the birthday message
import random

# Create the main window for the application
root = tk.Tk()
# Set the title of the main window
root.title("Fun Birthday Program")
# Set the size of the window to 400x300 pixels
root.geometry("400x300")
# Set the background color of the window to light blue
root.config(bg="lightblue")

# Define a function to calculate the user's age based on their birthday
def calculate_age():
    # Get the user's input birthday from the entry widget
    birthdate_str = entry_birthdate.get()
    try:
# Convert the input string to a datetime object using the specified format
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

# Get the current date and time
        today = datetime.now()
# Calculate the initial age by subtracting birth year from current year
        age = today.year - birthdate.year
# Adjust age if the birthday has not occurred yet this year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

# Update the result label to show the user's age
        label_result.config(text=f"You are {age} years old")

# Check if today is the user's birthday
        if today.month == birthdate.month and today.day == birthdate.day:
# If it is their birthday, show a celebratory message
            show_birthday_message(age)
        else:
# Otherwise, show a message stating that it's not their birthday
            messagebox.showinfo("Result", f"You are {age} years old.\nToday is not your birthday.")
    except ValueError:
# Show an error message if the input date format is invalid
        messagebox.showerror("Invalid date", "Please enter the date in format YYYY-MM-DD.")

# Define a function to show a birthday message with animation
def show_birthday_message(age):
# Define a nested function to change the text color
    def change_color():
# List of colors to choose from for the text
        colors = ["red", "yellow", "green", "blue", "pink", "purple", "orange"]
# Change the label text color to a random color from the list
        label_birthday.config(fg=random.choice(colors))
# Call this function again after 500 milliseconds to create a loop
        root.after(500, change_color)

# Update the birthday label with a celebratory message and specific font settings
    label_birthday.config(text=f"🎉 Happy Birthday! You are now {age} years old! 🎉", font=("Arial", 18, "bold"))
# Start the color-changing effect
    change_color()

# Create a label prompting the user to enter their birthday
label_prompt = tk.Label(root, text="Enter your birthday (YYYY-MM-DD):", bg="lightblue")
# Pack the label into the window with some padding
label_prompt.pack(pady=10)

# Create an entry widget for the user to input their birthday
entry_birthdate = tk.Entry(root, width=20)
# Pack the entry widget into the window with some padding
entry_birthdate.pack(pady=5)

# Create a button that will trigger the age calculation when clicked
button_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
# Pack the button into the window with some padding
button_calculate.pack(pady=10)

# Create a label to display the result of the age calculation
label_result = tk.Label(root, text="", bg="lightblue", font=("Arial", 12))
# Pack the result label into the window with some padding
label_result.pack(pady=5)

# Create a label to display the birthday message
label_birthday = tk.Label(root, text="", bg="lightblue")
# Pack the birthday message label into the window with additional padding
label_birthday.pack(pady=30)

# Start the Tkinter event loop, which waits for user interaction
root.mainloop()
