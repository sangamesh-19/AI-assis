import pyttsx3

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    try:
        # Get the current speaking rate
        rate = engine.getProperty('rate')

        # Set the speaking rate (reduce it by 70)
        engine.setProperty('rate', max(rate - 70, 50))  # Ensure it doesn't go below 50

        # Queue the text to be spoken
        engine.say(text)

        # Run the speech engine
        engine.runAndWait()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Clean up the engine resources
        engine.stop()
