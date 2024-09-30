import speech_recognition as sr

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as a source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        # Adjust the recognizer sensitivity to ambient noise
        recognizer.adjust_for_ambient_noise(source)
        print("Say something:")
        audio = recognizer.listen(source)

    # Recognize the speech
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from the service; {e}")
        return None
