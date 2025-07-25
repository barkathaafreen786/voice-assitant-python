import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Microphone is working. Speak something...")
    audio = r.listen(source)
    print("Processing...")
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
    except Exception as e:
        print("Error:", e)