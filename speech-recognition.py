import speech_recognition as sr
import pyttsx3
import pywhatkit

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to perform actions based on user command
def process_command(command):
    if "play" in command:
        song = command.replace("play", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif "search" in command:
        query = command.replace("search", "")
        speak(f"Searching for {query}")
        pywhatkit.search(query)
    else:
        speak("Sorry, I didn't understand that command.")

# Main loop
while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("User:", command)

        process_command(command)

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")