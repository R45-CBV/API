import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech (default ~200)
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Speak text
engine.say("nice to meet you.")
engine.runAndWait()  # Blocks execution until speech is finished
