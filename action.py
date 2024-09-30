import datetime
import webbrowser
import text_to_speech  # Import the text-to-speech module
import weather

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        response = "My name is Virtual Assistant."
    
    elif "hey" in user_data or "hello" in user_data:
        response = "Hey, Sangamesh, how can I help you?"
    
    elif "How many languages do you know" in user_data:
        response = "i can speak in three language, english, kannada hindi."
    
    elif "what is the time now" in user_data:
        current_time = datetime.datetime.now()
        response = f"{current_time.hour} hour: {current_time.minute} minute"
    
    elif "shutdown" in user_data:
        response = "Ok sir."
    
    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        response = "Spotify is ready for you."
    
    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        response = "YouTube is ready for you."
    
    elif "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        response = "Google is ready for you."
    
    elif "weather" in user_data:
        location = "patan"  # Default location
        # Attempt to extract location if mentioned in the user input
        if "in" in user_data:
            parts = user_data.split("in")
            if len(parts) > 1:
                location = parts[1].strip()  # Get the location after "in"
        try:
            response = weather.weather(location)  # Pass the location to your weather function
        except Exception as e:
            response = f"Sorry, I couldn't fetch the weather for {location}. Error: {str(e)}"
    else:
        response = "Sorry, I am not able to understand."

    # Call text-to-speech to speak the response
    text_to_speech.text_to_speech(response)  
    return response  # Return the response
