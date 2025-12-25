import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
r = sr.Recognizer()

with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language="en-US")
    print(f"Atumalaca: {text}")
    engine.say(text)
    engine.runAndWait()
except sr.UnknownValueError:
    print("could not understand audio")
except sr.RequestError as e:
    print(f"could not request results; {e}")