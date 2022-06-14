import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import webbrowser
import time
import subprocess
import wolframalpha
import urllib.parse
import requests
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()
root.config(bg="lightblue")
root.title("BUDDY")
root.iconbitmap("buddyico.ico")
chromedir = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

f1 = {
    "cniot" : [["tuesday","10:50",256],["thursday","9:55",228],["friday","11:45",245]],
    "cniot lab" : [["tuesday","14:30",35]],
    "se" : [["tuesday","11:45",259],["wednesday","9:00",256],["friday","13:35",256]],
    "se lab" : [["thursday","14:30",151]]
    }
f2 = {
    "cniot" : [["tuesday","10:50",259],["wednesday","13:35",254],["friday","11:45",259]],
    "cniot lab" : [["tuesday","14:30",35]],
    "se" : [["tuesday","11:45",259],["wednesday","9:00",259],["thursday","9:55",259]],
    "se lab" : [["thursday","14:30",151]]
    }
f3 = {
    "cniot" : [["tuesday","10:50",257],["wednesday","13:35",259],["friday","11:45",228]],
    "cniot lab" : [["tuesday","14:30",35]],
    "se" : [["tuesday","11:45",259],["wednesday","9:00",256],["friday","13:35",256]],
    "se lab" : [["thursday","14:30",151]]
    }
f4 = {
    "cniot" : [["tuesday","10:50",228],["wednesday","13:35",257],["friday","11:45",226]],
    "cniot lab" : [["friday","13:35",35]],
    "se" : [["tuesday","11:45",259],["wednesday","9:00",259],["thursday","9:55",259]],
    "se lab" : [["tuesday","14:30",151]]
    }
f5 = {
    "cniot" : [["tuesday","9:55",254],["wednesday","13:35",228],["thursday","9:55",226]],
    "cniot lab" : [["friday","13:35",35]],
    "se" : [["tuesday","10:50",226],["wednesday","9:00",228],["thursday","14:30",259]],
    "se lab" : [["monday","14:30",35]],
    }
f6 = {
    "cniot" : [["tuesday","9:55",259],["wednesday","13:35",226],["thursday","15:25",259]],
    "cniot lab" : [["thursday","9:55",35]],
    "se" : [["tuesday","10:50",226],["wednesday","9:00",228],["thursday","14:30",259]],
    "se lab" : [["monday","14:30",35]],
    }
f7 = {
    "cniot" : [["monday","9:55",228],["tuesday","9:55",256],["thursday","9:55",254]],
    "cniot lab" : [["friday","9:00",35]],
    "se" : [["tuesday","11:45",259],["wednesday","9:00",256],["friday","13:35",256]],
    "se lab" : [["tuesday","14:30",151]]
    }
f8 = {
    "cniot" : [["tuesday","9:55",257],["thursday","14:30",254],["friday","12:40",259]],
    "cniot lab" : [["friday","9:00",35]],
    "se" : [["tuesday","11:45",259],["wednesday","9:00",259],["thursday","9:55",259]],
    "se lab" : [["tuesday","14:30",151]]
    }
    
cse = {
    "large database" : [["monday","9:00",254],["wednesday","14:30",254],["friday","10:50",254]],
    "big data" : [["wednesday","9:55",228],["thursday","10:50",257],["friday","15:25",257]],
    "ai" : [["tuesday","11:45",256],["wednesday","9:00",257],["friday","16:20",257]],
    "ai lab" : [["monday","14:30",150]],
    "blockchain" : [["wednesday","9:55",259],["thursday","10:50",254],["friday","15:25",254]],
    "qpen source" : [["wednesday","9:55",256],["thursday","10:50",259],["friday","15:25",259]],
    "fundamental distributed" : [["wednesday","9:55",257],["thursday","10:50",256],["friday","15:25",256]],
    "sensor android" : [["monday","9:00",259],["wednesday","14:30",257],["friday","10:50",259]],
    "soft computing" : [["monday","9:00",257],["wednesday","14:30",226],["friday","10:50",226]],
    "web cyber" : [["monday","9:00",256],["wednesday","14:30",259],["friday","10:50",228]],
    "marketing" : [["monday","9:55",254],["friday","12:40",256]],
    "project management" : [["monday","16:20",257],["tuesday","9:00",257],["wednesday","11:45",257]],
    "numerical" : [["monday","10:50",259],["thursday","13:35",259]],
    "organizational" : [["monday","13:35",259],["wednesday","10:50",257]],
    "global politics" : [["monday","13:35",256],["wednesday","10:50",259]],
    "cognitive" : [["monday","13:35",257],["wednesday","10:50",256]],
    "operational research" : [["tuesday","9:00",259],["wednesday","11:45",259]]
    }

def all_lect(subject,type):
    if type[subject].len(): 
        for i in type[subject]:
            print(i)

def specify_days(subject,type):
  for i in type[subject]:
    print(i[0])

def day_lect(day,type):
  for sub,val in type.items():
    for lectures in val:
      if (lectures[0] == day):
        print(sub)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello mam,Good Morning")
        print("Hello mam,Good Morning")
        label = Label(root, text= "Hello mam,Good Morning")
        label.pack()
    elif hour >= 12 and hour < 18:
        speak("Hello mam,Good Afternoon")
        print("Hello mam,Good Afternoon")
        label = Label(root, text= "Hello mam,Good Afternoon")
        label.pack()
    else:
        speak("Hello mam,Good Evening")
        print("Hello mam,Good Evening")
        label = Label(root, text= "Hello mam,Good Evening")
        label.pack()


def tellDay():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print("The day is ", day_of_the_week)
        speak("The day is " + day_of_the_week)
        label = Label(root, text= "The day is " + day_of_the_week)
        label.pack()


def tellTime():#this function will tell time 
    time = str(datetime.datetime.now())

    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is mam" + hour + "Hours and" + min + "Minutes")
    label = Label(root, text= "The time is mam" + hour + "Hours and" + min + "Minutes")
    label.pack()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        label = Label(root, text= "Listening...")
        label.pack()
        print("Listening...")
        speak("Listening")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"You said:{statement}\n")
            label = Label(root, text=f"You said:{statement}\n") 
            label.pack()

        except Exception as e:
            speak("Pardon me, please say that again.")
            return "None"
        return statement

wishMe() # Calling the wishme function

print('Respected Shruti Mam, Anubhuti Mam and Himani Mam. I am Buddy, your basic model virtual assistant.')
speak("Respected Shruti Mam, Anubhuti Mam and Himani Mam. I am Buddy, your basic model virtual assistant.")
label = Label(root, text="Respected Shruti Mam, Anubhuti Mam and Himani Mam. I am Buddy, your basic model virtual assistant") 
label.pack()

if __name__== '__main__':
    while True:
        speak("Tell me how can I help you now?.")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement:
            speak('your personal assistant Buddy is shutting down,Good bye mam')
            print('your personal assistant Buddy is shutting down,Good bye mam')
            label = Label(root, text="your personal assistant Buddy is shutting down,Good bye mam") 
            label.pack()
            break

        if "from wikipedia" in statement:

            speak("Checking the wikipedia ")
            query = statement.replace("wikipedia", " ")

            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            print(result)
            label = Label(root, text=result) 
            label.pack()
            speak(result)


        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "37ad0f5bd38d157032013c7dc869f3c1"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
                label = Label(root, text=" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description)) 
                label.pack()

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            print(
                'I am Buddy - The Chatbot version 1.o a personal assistant created by GROUP19 . I am programmed to execute minor tasks like'
                'opening youtube,google chrome,gmail ,predict time,take a photo,search wikipedia,predict weather'
                'in different cities , get top headline news from times of india and you can ask me some computational questions too!. I am happy to help you.')
            speak(
                'I am Buddy - The Chatbot version 1.o a personal assistant created by GROUP19 . I am programmed to execute minor tasks like'
                'opening youtube,google chrome,gmail ,predict time,take a photo,search wikipedia,predict weather'
                'in different cities , get top headline news from times of india and you can ask me some computational questions too!. I am happy to help you.')
            label = Label(root, text= 'I am Buddy - The Chatbot version 1.o a personal assistant created by GROUP19 . I am programmed to execute minor tasks like'
                'opening youtube,google chrome,gmail ,predict time,take a photo,search wikipedia,predict weather'
                'in different cities , get top headline news from times of india and you can ask me some computational questions too!. I am happy to help you.') 
            label.pack()


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I have been created by MEMBERS OF GROUP 19, AMISHA, RAHUL MALIK, APARNA BANSAL and MANSI JOSHI")
            print("I have been created by MEMBERS OF GROUP 19, AMISHA, RAHUL MALIK, APARNA BANSAL and MANSI JOSHI")
            label = Label(root, text= "I have been created by MEMBERS OF GROUP 19, AMISHA, RAHUL MALIK, APARNA BANSAL and MANSI JOSHI") 
            label.pack()

        elif "will you be my friend" in statement or "will you be my best friend" in statement:
            speak("I'm not sure about, may be you should give me some time")


        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'search' in statement:
            statement = statement.replace("search", "")
            url = "https://www.google.com.tr/search?q=".format(statement)
            webbrowser.get(chromedir).open_new_tab(url)
            time.sleep(5)

        elif 'play' in statement:
            song = statement.replace('play', '')
            speak("playing " + song)
            pywhatkit.playonyt(song)


        elif "which day it is" in statement:
            tellDay()
            continue

        elif "tell me the time" in statement:
            tellTime()
            continue

        elif "schedule" in statement:
            print("choose one option : ")
            speak('choose one option')
            print("1. Get all lecture schedule corresponding to particular subject.")
            print("2. Get all lecture schedule days corresponding to particular subject.")
            print("3. Get all subjects lecture corresponding to particular day.")
            option =  takeCommand().lower()
            if '1' in option:
                speak("Enter subject")
                subject = takeCommand().lower()
                speak("Enter batch or cse (if elective)")
                type = takeCommand().lower()
                all_lect(subject,type)
            elif '2' in option:
                speak("Enter subject")
                subject = takeCommand().lower()
                speak("Enter batch or cse (if elective)")
                type = takeCommand().lower()
                specify_days(subject,type)
            elif '3' in option:
                speak('Enter day')
                day = takeCommand().lower()
                speak('Enter batch or cse (if elective)')
                type = takeCommand().lower()
                day_lect(day,type)
                continue

        elif 'do some maths' in statement or 'try some calculation' in statement or 'try some computtaional' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "E8X2QV-7T757T32XA"
            client = wolframalpha.Client('E8X2QV-7T757T32XA')
            res = client.query(question)
            answer = next(res.results).text
            print("Your answer is:" + answer)
            label = Label(root, text= "Your answer is:" + answer) 
            label.pack()
            speak("Your answer is:" + answer)


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec. Make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "shutdown" in statement:
            speak("Ok , your pc will shutdown in 10 sec. Make sure you exit from all applications")
            subprocess.call(["shutdown", "/s"])

        elif "restart" in statement:
            speak("Ok , your pc will restart in 10 sec. Make sure you exit from all applications")
            subprocess.call(["shutdown", "/r"])
root.mainloop()
time.sleep(0)
