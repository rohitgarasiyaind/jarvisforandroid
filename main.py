import speech_recognition as sr
import os
import time
import requests
from gtts import gTTS
from playsound import playsound

# Function to make Jarvis speak
def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("response.mp3")
    playsound("response.mp3")
    os.remove("response.mp3")

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError:
            print("Speech recognition service error")
            return ""

# Function to handle commands
def process_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "time" in command:
        speak(f"The current time is {time.strftime('%I:%M %p')}")
    elif "weather" in command:
        response = requests.get("https://wttr.in/?format=3").text
        speak(f"The weather is {response}")
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I did not understand that.")

# Main Loop
if __name__ == "__main__":
    speak("Jarvis is now active.")
    while True:
        command = listen()
        if command:
            process_command(command)