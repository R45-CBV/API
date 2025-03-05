import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)  
engine.setProperty('volume', 10.0)  


engine.say("Congratulations! You win the lottery.")
engine.runAndWait()  
