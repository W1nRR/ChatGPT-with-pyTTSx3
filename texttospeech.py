import pyttsx3

def text_to_speech(text, language='tr'):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the language (optional, default is English)
    engine.setProperty('language', language)

    # Set the rate of speech (optional, default is 200)
    engine.setProperty('rate', 150)

    # Set the voice (optional, you can experiment with different voices)
    # You can get the available voices with: engine.getProperty('voices')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change the index if needed

    # Speak the given text
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()