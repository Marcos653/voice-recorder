import speech_recognition as sr
import webbrowser
r = sr.Recognizer()


with sr.Microphone() as source:                
    while True:
        audio = r.listen(source)
        try:
            result = r.recognize_google(audio)
            print("You said " + result)
            words = result.lower()
            if words=="facebook":
                webbrowser.open('https://www.facebook.com')
            if words=="google":
                webbrowser.open('https://www.google.co.uk')
            if words=="stop":
                break
        except LookupError:
            print("Please, speak more clearly")
