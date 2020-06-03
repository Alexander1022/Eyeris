import os, sys, random
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
from appJar import gui
import pyautogui

# функция за говорене

def speak_text(string):
    app.setTextArea("log", "Eyeris : " + string + "\n" , end=True, callFunction=True)
    date = datetime.datetime.now()
    file_name = "cache/" + str(date).replace(":", "-") + "-speak.mp3"
    speak = gTTS(text = string, lang = "en", slow = False)
    speak.save(file_name)
    playsound.playsound(file_name)

# функция за представяне
def introduction():
    app.setTextArea("log", "Eyeris : Hello, my name is Eyeris 1.0, made for TUES Fest 2020! My full version will be available soon.\n" , end=True, callFunction=False)
    introduce = gTTS(text = "Hello, my name is Eyeris 1.0, made for TUE S Fest 2020! My full version will be available soon.", lang = "en", slow = False)
    introduce.save("introduce.mp3")
    playsound.playsound("introduce.mp3")

# функция за разпознаване на глас
def speech_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said_by_user = r.recognize_google(audio)
            app.setTextArea("log", "User : " + said_by_user.capitalize() + "\n" , end=True, callFunction=True)

        except Exception as e:
            speak_text("I couldn't understand this.")
            said_by_user = ""

    return said_by_user.lower()

def wake_up():
    playsound.playsound("sound.mp3")

#функция - пита те за име
def ask_for_name():
    app.setTextArea("log", "Eyeris : What's your name?\n" , end=True, callFunction=False)
    ask_name = gTTS(text = "What's your name?", lang = "en", slow = False)
    ask_name.save("ask_for_name.mp3")
    playsound.playsound("ask_for_name.mp3")
    name = speech_recognition()
    app.setTextArea("log", "Eyeris : Nice to meet you " + name.capitalize() + "\n" , end=True, callFunction=True)
    tts_your_name = gTTS(text = 'Nice to meet you, ' + name, lang = "en", slow = False)
    tts_your_name.save("name.mp3")
    playsound.playsound("name.mp3")

def make_dir():
    if not os.path.exists('cache'):
        os.mkdir('cache')

    if not os.path.exists('notes'):
        os.mkdir('notes')

    if not os.path.exists('screenshots'):
        os.mkdir('screenshots')

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
        app.setTextArea("log", i + "\n" , end=True, callFunction=True)

def dictionary():
    dictionary=PyDictionary()
    speak_text("What are you looking for?")
    word = speech_recognition()
    speak_text("This is the meaning of " + word)
    app.setTextArea("log", "\n" , end=True, callFunction=False)
    app.setTextArea("log", dictionary.meaning(word), end=True, callFunction=True)

def press(button):
    if button == "Exit":
        app.setStopFunction(checkStop)
        app.stop()

    elif button == "Wake":
        wake_up()
        app.setTextArea("log", "* Eyeris is waiting for your answer *\n" , end=True, callFunction=False)
        simple_phrases()
        app.setTextArea("log", "\n" , end=True, callFunction=False)

def checkStop():
    return app.yesNoBox("Confirm Exit", "Are you sure you want to exit Eyeris?")

#функция за фрази
def simple_phrases():

    THANKS = ("Thanks to my creators, not to me!", "No problem.", "I am here to help you.", "You're welcome")
    HELLO_PHRASES = ("Hey!", "Hello!", "Hey there!", "Hello there!")
    HOW_ARE_YOU_PHRASE = ("I am feeling fine.", "I am artificial intelligent, i have no emotions, so i am okay!", "I am good, because of you!", "I am good!", "I am well, thanks!")
    EYERIS_NAME = ("My name is Eyeris.", "Eyeris.", "Eyeris. Nice to meet you!")
    COIN = ("Heads", "Tails")
    JOKES = ("What is the biggest lie in the entire universe? - I have read and agree to the Terms & Conditions.", "Why did the PowerPoint Presentation cross the road? - To get to the other slide.", "Why was the cell phone wearing glasses? - It lost its contacts.", "You know you're texting too much when...you say LOL in real life, instead of just laughing.")

    speech_input = speech_recognition()

    if "how are you" in speech_input:
        speak_text(random.choice(HOW_ARE_YOU_PHRASE))

    elif "your name" in speech_input:
        speak_text(random.choice(EYERIS_NAME))

    elif "are you ok" in speech_input:
        speak_text("Yes.")

    elif "hey siri" in speech_input:
        speak_text("I am not Siri, i am Eyeris! Don't change my name please!")

    elif "time" in speech_input:
        get_time()

    elif "goodbye" in speech_input:
        speak_text("Goodbye. Have a good time")
        app.stop()

    elif "bye" in speech_input:
        speak_text("Bye. Have a good time")
        app.stop()

    elif "hey" in speech_input:
        speak_text(random.choice(HELLO_PHRASES))

    elif "hello" in speech_input:
        speak_text(random.choice(HELLO_PHRASES))

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
        speak_text(random.choice(THANKS))

    elif "thank you" in speech_input:
        speak_text(random.choice(THANKS))

    elif "can you hear me" in speech_input:
        speak_text("Yes, i can!")

    elif "open google" in speech_input:
        speak_text("I am opening Google.")
        webbrowser.open('http://google.com', new=2)

    elif "open youtube" in speech_input:
        speak_text("I am opening YouTube.")
        webbrowser.open('http://youtube.com', new=2)

    elif "open facebook" in speech_input:
        speak_text("I am opening Facebook.")
        webbrowser.open('http://facebook.com', new=2)

    elif "take a selfie" in speech_input:
        speak_text("I am opening the camera.")
        subprocess.run('start microsoft.windows.camera:', shell=True)

    elif "take a picture" in speech_input:
        speak_text("I am opening the camera.")
        subprocess.run('start microsoft.windows.camera:', shell=True)

    elif "notepad" in speech_input:
        speak_text("Do you want to write down something on the text file?")
        answer_note = speech_recognition()

        if "yes" in answer_note:
            speak_text("What do you want to write down?")
            take_a_note = speech_recognition()
            make_a_note(take_a_note)
            return

        elif "want" in answer_note:
            speak_text("What do you want to write down?")
            take_a_note = speech_recognition()
            make_a_note(take_a_note)
            return

        elif "no" in answer_note:
            speak_text("I am opening the notepad.")
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
        speak_text("I am opening Explorer.")
        subprocess.Popen("explorer.exe")

    elif "open file manager" in speech_input:
        speak_text("I am opening Explorer.")
        subprocess.Popen("explorer.exe")

    elif "open calculator" in speech_input:
        speak_text("I am opening calculator.")
        subprocess.Popen("calc.exe")

    elif "open settings" in speech_input:
        speak_text("I am opening Settings")
        #subprocess.run('start microsoft.windows.settings:')

    elif "open dictionary" in speech_input:
        speak_text("Dictionary is open and ready to use.")
        dictionary()

    elif "open the dictionary" in speech_input:
        speak_text("Dictionary is open and ready to use.")
        dictionary()

    elif "introduce" in speech_input:
        introduction()
    
    elif "how old are you" in speech_input:
        speak_text("They say that age is nothing, but a number. Technically, it's a word.")

    elif "where do you live" in speech_input:
        speak_text("In your computer")

    elif "your favourite colour" in speech_input:
        speak_text("Virtual assistants usually don't have favourite colour")

    elif "flip a coin" in speech_input:
        speak_text(random.choice(COIN))

    elif "tell me a joke" in speech_input:
        speak_text(random.choice(JOKES))

    elif "value of pi" in speech_input:
        speak_text("3.14")

    elif "meaning of life" in speech_input:
        speak_text("Not to think about questions like this")
    
    else:
        speak_text("I don't know what to answer.")

#main func
with gui("Eyeris 1.0", "800x420") as app:
    make_dir()
    app.setLocation("CENTER")
    app.setFont(size=20, family="Courier", weight="normal")
    app.setPadding([10,10])
    app.setInPadding([10,10])
    app.setOnTop(stay=False)
    app.setSticky("wens")
    app.setStretch("both")
    app.setExpand("both")
    app.setBg("black")
    app.addLabel("title", "Eyeris 1.0")
    app.setLabelBg("title", "black")
    app.setLabelFg("title", "white")
    app.addScrolledTextArea(title="log", text="")
    app.setTextAreaFont("log", weight="bold")
    app.addButtons(["Wake", "Exit"], press)
    app.setStretch('column')
    app.setSticky('ew')
    app.addHorizontalSeparator(3,0,0, colour="white")
    app.setSticky('ew')
    app.addLabel("bottom", "For TUES Fest 2020")
    app.setLabelFg("bottom", "black")
    app.setLabelBg("bottom", "gainsboro")
    #app.showSplash("Welcome to Eyeris 1.0", fill='black', stripe='white', fg='black', font=30)


if __name__ == "__main__":
    main()
