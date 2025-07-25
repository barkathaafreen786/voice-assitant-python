import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser
import pyjokes

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index to 1 for female voice

# Initialize speech recognizer
listener = sr.Recognizer()

# Speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Listen and convert voice to text
def listen_command():
    try:
        with sr.Microphone() as source:
            print("Mic ready. Listening...")
            listener.adjust_for_ambient_noise(source, duration=1)
            audio = listener.listen(source, timeout=5, phrase_time_limit=7)
            print("Recognizing...")
            command = listener.recognize_google(audio)
            command = command.lower()
            print("You said:", command)
            return command
    except sr.WaitTimeoutError:
        speak("You didn't say anything.")
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
    except sr.RequestError:
        speak("Network error. Please check your connection.")
    except Exception as e:
        print("Error:", e)
        speak("Something went wrong.")
    return ""

# Run the assistant
def run_assistant():
    speak("Hello! I am your voice assistant. How can I help you?")
    
    while True:
        command = listen_command()

        if 'open notepad' in command:
            speak("Opening Notepad")
            os.system("notepad.exe")

        elif 'open chrome' in command:
            speak("Opening Google Chrome")
            os.system("start chrome")

        elif 'play music' in command:
            music_path = "C:\\Users\\Public\\Music\\Sample Music"  # Change path if needed
            try:
                os.startfile(music_path)
                speak("Playing music")
            except Exception as e:
                speak("Music folder not found.")

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {time}")

        elif 'search' in command:
            search_query = command.replace('search', '').strip()
            if search_query:
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)
                speak(f"Searching for {search_query}")
            else:
                speak("Please say what you want to search for.")

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'take note' in command or 'note' in command:
            speak("What should I write?")
            note = listen_command()
            if note:
                with open('note.txt', 'a') as f:
                    f.write(f"{datetime.datetime.now()}: {note}\n")
                speak("Note saved.")

        elif 'show note' in command or 'read note' in command:
            try:
                with open('note.txt', 'r') as f:
                    notes = f.read()
                    if notes:
                        speak("Here are your notes.")
                        print(notes)
                    else:
                        speak("Your note file is empty.")
            except FileNotFoundError:
                speak("No notes found yet.")

        elif 'news' in command:
            speak("Opening Google News.")
            webbrowser.open("https://news.google.com")

        elif 'exit' in command or 'stop' in command or 'bye' in command:
            speak("Goodbye! Have a nice day.")
            break

        elif command:
            speak("Sorry, I didn't understand that. Please try again.")

# Entry point
if __name__ == "__main__":
    run_assistant()
