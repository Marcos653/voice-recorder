import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

#use the microphone as source for input.
with sr.Microphone() as source2:

    #wait for a second to let the recognizer
    #adjust the energy threshold based on the surrounding noise level
    r.adjust_for_ambient_noise(source2, duration=0.2)



    while True:
        aiName = 'AI'
        audio = r.listen(source2)
        try:
            result = r.recognize_google(audio)
            print("You said: " + result)
            words = result.lower()

            if words=="hello":
                print(aiName + ' hello, what is your name?')
                SpeakText('Hello, what is your name?')
                result = r.recognize_google(audio)
                print("You said: " + result)
                words = result.lower()

            word_list = words.split()
            if "your name is" in words:
                aiName =  word_list[-1]
                print(aiName + ': my name is ' + word_list[-1])
                SpeakText('my name is ' + word_list[-1])

            word_list = words.split()
            if "my name" in words:
                print(aiName + ': nice to meet you ' + word_list[-1])
                SpeakText('nice to meet you ' + word_list[-1])


            if words=="facebook":
                webbrowser.open('https://www.facebook.com')
            if words=="google":
                webbrowser.open('https://www.google.com.br')
            if words=="break":
                break

        except LookupError:
            print("Please, speak more clearly")