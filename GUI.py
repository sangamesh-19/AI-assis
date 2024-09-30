from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action

# Initialize the main application window
root = Tk()
root.title('AI Assistant')
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="yellow")

# Ask function to handle speech input
def ask():
    user_val = speech_to_text.speech_to_text()  # Get user input via speech
    if user_val:  # Check if user_val is not None or empty
        bot_val = action.Action(user_val)  # Get the bot's response
        text.insert(END, 'User ---> ' + user_val + "\n")  # Display user input
        if bot_val:  # Check if bot_val is not None or empty
            text.insert(END, 'BOT ----> ' + str(bot_val) + "\n")  # Display bot response
            if bot_val.lower() == "ok sir":  # Check for shutdown command
                root.destroy()  # Close the application

# Send function to handle text input from the Entry widget
def send():
    user_input = entry.get()  # Get text from the entry widget
    text.insert(END, "Me --> " + user_input + "\n")  # Display user input
    if user_input:  # Check if user_input is not empty
        bot_response = action.Action(user_input)  # Get the bot's response
        if bot_response:  # Check if bot_response is not None or empty
            text.insert(END, "BOT <-- " + str(bot_response) + "\n")  # Display bot response
            if bot_response.lower() == "ok sir":  # Check for shutdown command
                root.destroy()  # Close the application
    entry.delete(0, END)  # Clear the entry after sending

# Delete function to clear the text widget
def del_text():
    text.delete(1.0, END)  # Clear the text widget

# Frame for organizing UI elements
frame = LabelFrame(root, padx=100, pady=5, borderwidth=3, relief="raised")
frame.config(bg="yellow")
frame.grid(row=0, column=1, padx=55, pady=10)

# Text label for the assistant title
text_label = Label(frame, text='AI Assistant', font=("Comic Sans MS", 14, "bold"))
text_label.grid(row=0, column=0, padx=20, pady=10)

# Load and display image
image = ImageTk.PhotoImage(Image.open("AI.png"))  # Ensure "AI.png" is in the same directory
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)

# Text widget for conversation
text = Text(root, font=('Courier 10 bold'), bg="lime")
text.grid(row=2, column=0)
text.place(x=100, y=375, width=375, height=100)

# Entry widget for user input
entry = Entry(root, justify=CENTER)
entry.place(x=100, y=500, width=350, height=30)

# Button to ask the assistant
Button1 = Button(root, text='ASK', bg='aqua', pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=575)

# Button to send input from the entry widget
Button2 = Button(root, text='SEND', bg='aqua', pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=400, y=575)

# Button to delete text from the conversation
Button3 = Button(root, text='DELETE', bg='crimson', pady=16, padx=40, borderwidth=3, relief=SOLID, command=del_text)
Button3.place(x=225, y=575)

# Start the main loop of the application
root.mainloop()
