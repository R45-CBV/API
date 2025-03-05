import speech_recognition as sr
import pyaudio


recognizer = sr.Recognizer()


audio_file = "/Users/edelta077/Desktop/Raj/TS/output.wav"

with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)  # Read the audio file
    text = recognizer.recognize_google(audio_data)  # Convert speech to text

print("Transcription:", text)

