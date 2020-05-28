import os, sys
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import time
import webbrowser
import subprocess
import datetime
import os.path
from googlesearch import search
from PyDictionary import PyDictionary

# функция за говорене
def speak_text(string):
    date = datetime.datetime.now()
    file_name = "cache/" + str(date).replace(":", "-") + "-speak.mp3"
    speak = gTTS(text = string, lang = "en", slow = False)
    print("Eyeris : " + string)
    speak.save(file_name)
    playsound.playsound(file_name)

# функция за представяне
def introduction():
    introduce = gTTS(text = "Hello, my name is Eyeris 1.0, made for TUE S Fest 2020! My full version will be available soon.", lang = "en", slow = False)
    print("Eyeris : Hello, my name is Eyeris 1.0, made for TUES Fest 2020! My full version will be available soon.")
    introduce.save("introduce.mp3")
    playsound.playsound("introduce.mp3")

# функция за разпознаване на глас
def speech_recognition():
    print("* Eyeris is waiting for your voice *")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said_by_user = r.recognize_google(audio)
            print("User : " + said_by_user.capitalize())

        except Exception as e:
            speak_text("Exception : I couldn't understand this. There is an error in Google SpeechRecognition! ")
            said_by_user = ""

    return said_by_user.lower()

#функция - пита те за име
def ask_for_name():
    ask_name = gTTS(text = "What's your name?", lang = "en", slow = False)
    print("Eyeris : What's your name")
    ask_name.save("ask_for_name.mp3")
    playsound.playsound("ask_for_name.mp3")
    name = speech_recognition()
    tts_your_name = gTTS(text = 'Nice to meet you, ' + name, lang = "en", slow = False)
    print("Eyeris : Nice to meet you, " + name.capitalize())
    tts_your_name.save("name.mp3")
    playsound.playsound("name.mp3")

def make_dir():
    if not os.path.exists('cache'):
        os.mkdir('cache')

    if not os.path.exists('notes'):
        os.mkdir('notes')

    if not os.path.exists('screenshots'):
        os.mkdir('screenshots')

    if not os.path.exists('test'):
        os.mkdir('test')

#функция за времето
def get_time():
    localtime = time.localtime()
    the_time = time.strftime("%I:%M:%S", localtime)
    speak_text("The time is " + the_time)

#функция за правене на note в notepad.exe на Windows
def make_a_note(note_string):
    date = datetime.datetime.now()
    note_file_name = "notes/" + str(date).replace(":", "-") + "-note.txt"
    with open(note_file_name, "w") as file:
        file.write(note_string)
    subprocess.Popen(["notepad.exe", note_file_name])

#функция за google търсене
def google_search():
    query = speech_recognition()
    speak_text("I am searching it")
    speak_text("I found some results : ")
    my_results_list = []

    for i in search(query, tld = 'com', lang = 'en', num = 5, start = 0, stop = 5, pause = 2.0):
        my_results_list.append(i)
        print(i + "\n")

def dictionary():
    dictionary=PyDictionary()
    speak_text("What are you looking for?")
    word = speech_recognition()
    speak_text("This is the meaning of " + word)
    print("\n")
    print(dictionary.meaning(word))

#функция за фрази
def simple_phrases():
    speech_input = speech_recognition()

    if "how are you" in speech_input:
        speak_text("Fine, i am feeling fine")

    elif "your name" in speech_input:
        speak_text("My name is Eyeris. Don't forget my name!")

    elif "are you ok" in speech_input:
        speak_text("Yes, i am! I am artificial intelligent. Emotions will be added soon!")

    elif "hey siri" in speech_input:
        speak_text("I am not Siri, i am Eyeris! Don't change my name please!")

    elif "time" in speech_input:
        get_time()

    elif "goodbye" in speech_input:
        speak_text("Goodbye. Have a good time")
        sys.exit()

    elif "bye" in speech_input:
        speak_text("Bye. Have a good time")
        sys.exit()

    elif "hey" in speech_input:
        speak_text("Hey there!")

    elif "hello" in speech_input:
        speak_text("Hello there! How are you?")

    elif "play music" in speech_input:
        speak_text("I can't do this! I will teach myself to do it soon.")

    elif "take a screenshot" in speech_input:
        speak_text("No problem! 3. 2. 1. Cheese! ")
        myScreenshot = pyautogui.screenshot()
        date = datetime.datetime.now()
        screenshot_file_name = "screenshots/" + str(date).replace(":", "-") + "-screenshot.png"
        myScreenshot.save(screenshot_file_name)
        speak_text("It's done!")

    elif "thanks" in speech_input:
        speak_text("Thanks to my creators, not to me!")

    elif "thank you" in speech_input:
        speak_text("Thanks to my creators, not to me!")

    elif "can you hear me" in speech_input:
        speak_text("Yes, i can!")

    elif "open google" in speech_input:
        speak_text("I am opening Google")
        webbrowser.open('http://google.com', new=2)

    elif "open youtube" in speech_input:
        speak_text("I am opening YouTube")
        webbrowser.open('http://youtube.com', new=2)

    elif "open facebook" in speech_input:
        speak_text("I am opening Facebook")
        webbrowser.open('http://facebook.com', new=2)

    elif "take a selfie" in speech_input:
        speak_text("I am opening the camera!")
        subprocess.run('start microsoft.windows.camera:', shell=True)

    elif "take a picture" in speech_input:
        speak_text("I am opening the camera")
        subprocess.run('start microsoft.windows.camera:', shell=True)

    elif "notepad" in speech_input:
        speak_text("Do you want to write down something on the text file?")
        answer_note = speech_recognition()

        if "yes" in answer_note:
            speak_text("what do you want to write down?")
            take_a_note = speech_recognition()
            make_a_note(take_a_note)
            return

        elif "no" in answer_note:
            speak_text("I am opening the notepad")
            subprocess.Popen("notepad.exe")
            return

    elif "open wikipedia" in speech_input:
        speak_text("I am opening Wikipedia")
        webbrowser.open('http://wikipedia.com', new=2)

    elif "open reddit" in speech_input:
        speak_text("I am opening Reddit")
        webbrowser.open('http://reddit.com', new=2)

    elif "search in google" in speech_input:
        speak_text("What do you want me to search?")
        google_search()

    elif "open explorer" in speech_input:
        speak_text("I am opening Explorer")
        subprocess.Popen("explorer.exe")

    elif "open file manager" in speech_input:
        speak_text("I am opening Explorer")
        subprocess.Popen("explorer.exe")

    elif "open calculator" in speech_input:
        speak_text("I am opening calculator")
        subprocess.Popen("calc.exe")

    elif "open settings" in speech_input:
        speak_text("I am opening Settings")
        #subprocess.run('start microsoft.windows.settings:')

    elif "open dictionary" in speech_input:
        speak_text("Dictionary is open and ready to use")
        dictionary()

    elif "open the dictionary" in speech_input:
        speak_text("Dictionary is open and ready to use")
        dictionary()

    else:
        speak_text("I don't get it. Sorry.")

#main f
def main():
    make_dir()
    #introduction()
    #ask_for_name()

    while True:
        simple_phrases()



if __name__ == "__main__":
    main()
