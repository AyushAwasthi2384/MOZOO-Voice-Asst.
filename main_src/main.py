import pyttsx3 as p
import speech_recognition as sr
import keyboard
import sys

print("START")
key = keyboard.read_key()

if key == "enter":
    # initialization of the text to speech module
    engine = p.init()
    engine.setProperty('rate', 175)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # The output...
    engine.say("Hello World, my name is mozoo.")
    # engine.say("Hi how are you?")
    engine.runAndWait()

    # initialization of the speech recognition module
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
else:
    print("END")