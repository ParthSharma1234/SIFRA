import os
import sys
import time
from random import random
import psutil
import pyautogui
import pyjokes as pyjokes
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import datetime
import speedtest
import wikipedia
import webbrowser
import cv2
import smtplib
import PyPDF2

from bs4 import BeautifulSoup
from playsound import playsound
from pytube import YouTube
from pywikihow import search_wikihow
from requests import get
from sketchpy import library as lib

print("Initializing SIFRA............")

ADMIN = "Parth"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def lock():
    p = 'SIFRA'
    speak("Please enter your password")
    g = input("Enter your Password = ")
    if p == g:
        speak("Access granted, Welcome back Parth")
    else:
        exit("Access Denied")

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning" + ADMIN)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + ADMIN)

    else:
        speak("Good Evening" + ADMIN)

    speak('HI! I am SIFRA. Starting all systems and applications. Installing and checking all drivers. All systems have been activated. Now i am online. How may i help you!')

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','your password')
    server.sendmail('your email id', to, content)
    server.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print('Recognizing...')
        q = r.recognize_google(audio, language='en')
        print(f"User said: {q}\n")

    except Exception as e:

        print('say that again pls sir')
        return "None"
    return q

def pdf_reader():
    book = open('Bill Gates 101.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book {pages}")
    speak("Sir please enter the page number i have to read")
    pg = int(input("Please enter the page number:"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

if __name__ == "__main__":
   lock()
   print("Hello")
   wishMe()
   while True:
        q = takeCommand().lower()
   #executing task based on query

        if 'wikipedia' in q:
            speak('Searching wikipedia')
            q = q.replace("wikipedia", "")
            results = wikipedia.summary(q, sentences=1)
            speak("According to Wikipedia")
            speak(results)

        elif 'how r u' in q:
            speak("my A I mood levels are always positive")
            speak("how are you Parth?")

        elif 'fine' in q:
            speak("It's good to know that you are fine")

        elif 'meaning of your' in q:
            speak("Super Intelligent Female Robot Automation")

        elif "tell me a joke" in q:
            speak(pyjokes.get_joke())

        elif "who are you" in q:
            speak("I am your personal desktop assistant.")

        elif "who i am" in q:
            speak("You are my ADMIN")

        elif "draw" in q:
            from sketchpy import library as lib
            obj = lib.rdj()
            obj.draw()
            speak("I am done PARTH now i am ready for the next command")

        elif "shutdown" in q:
            speak("shutting down system in 5 seconds 5 4 3 2 1")
            os.system("shutdown /s /t 5")

        elif "restart" in q:
            speak("restarting the system")
            os.system("shutdown /r")

        elif 'reason for your creation' in q:
            speak("I was created by my ADMIN and make PARTH's task easier")

        elif "what can you do" in q:
            speak("I can do lots of things , for example you can ask me time , jokes, temperature , I can open applications for you , and more")

        elif "change password" in q:
            speak("What's the new password")
            new_pw = input("Enter the new password\n")
            new_password = open("password.txt", "w")
            new_password.write(new_pw)
            new_password.close()
            speak("Done sir")
            speak(f"Your new password is{new_pw}")

        elif "focus mode" in q:
            a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO] "))
            if (a == 1):
                speak("Entering the focus mode....")
                os.startfile("C:\\Users\\hp\\PycharmProjects\\SIFRA\\FocusMode.py")
            else:
                speak("Focus mode cancelled")

        elif 'notepad' in q:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(npath)
            speak('notepad is opening now')

        # elif 'word' in q:
        #     npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word"
        #     os.startfile(npath)
        #     speak('word is opening now')

        elif 'uml' in q:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StarUML"
            os.startfile(npath)
            speak('opening Star UML')

        elif 'media player' in q:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\VideoLAN\\VLC media player"
            os.startfile(npath)
            speak('opening VLC media player')

        elif 'reddit' in q:
            webbrowser.open("reddit.com")
            speak('reddit is opening  now')

        elif 'close' in q:
            pyautogui.hotkey('alt','f4')

        elif 'gmail' in q:
            webbrowser.open("gmail.com")

        elif 'stackoverflow' in q:
            webbrowser.open("www.stackoverflow.com")
            speak('opening stackoverflow')

        elif 'download youtube video' in q:
            #not working properly
            speak("Provide me the link sir")
            link = input("Enter the link ")
            speak("Downloading the video")
            YouTube(link).streams.first().download()
            speak("Sir your video is been downloaded") #problem

        elif "how much power do you have" in q or "how much power is left" in q or "battery" in q:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"your system have {percentage} percent battery")
            if percentage>=75:
                speak("we have enough power to continue our work")
            elif percentage>=40 and percentage<=75:
                speak("we should connect our system to charging point to charge our battery")
            elif percentage<=15 and percentage<=30:
                speak("we don't have enough power to work, please connect to charging")
            elif percentage<=15:
                speak("we have low power, please connect to charging the system will shutdown very soon")

        elif 'music' in q:
            songs_dir = "C:\\Users\\hp\\Music\\test"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'time' in q:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{ADMIN} the time is {strTime}")

        elif 'switch window' in q:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "pause" in q:

            pyautogui.press("k")
            speak("video paused")

        elif "play" in q:

            pyautogui.press("k")
            speak("video played")

        elif 'google' in q:
            speak("What should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "temperature" in q:
            search = "current temperature is"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is  {temp}")

        elif "google search" in q:
            import wikipedia as googleScrap
            q = q.replace("sifra" ,"")
            q = q.replace("google search","")
            q = q.replace("google","")
            speak("This is what I found on web")
            pywhatkit.search(q)

            try:
                result = googleScrap.summary(q,2)
                speak(result)

            except:
                speak("No speakable data available!")


        elif "send whatsapp message" in q:
            pywhatkit.sendwhatmsg("+91 82691 52059", "HELLO",16,15)

        elif "youtube song" in q:
            pywhatkit.playonyt("See You Again (Epic Orchestral Version)")

        elif "command prompt" in q:
            os.system("start cmd")
            speak("opening command prompt")

        elif "cmd" in q:
            os.system("start cmd")
            speak("opening command prompt")

        elif "camera" in q:
            cap = cv2.VideoCapture(0)
            while True:
                ret ,img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
            #press esc to close the camera

        elif "screenshot" in q:
            speak("Sir, please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("please sir hold the screen for few second, i am taking screenshot")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done sir, the screenshot is save in your folder,now i am ready for next command.")

        elif "ip address" in q:
            ip = get('http://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "volume up" in q:
            pyautogui.press("volumeup")

        elif "volume down" in q:
            pyautogui.press("volumedown")

        elif "volume mute" in q or 'mute' in q:
            pyautogui.press("volumemute")

        elif "change name" in q:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in q or "what is your name" in q:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif "activate how to do mode" in q:
            speak("How to do mode is activated please tell me what you want to know")
            how = takeCommand()
            max_result = 1
            how_to = search_wikihow(how, max_result)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)

# to set alarm
        elif "alarm" in q:
            speak("Enter the Time!")
            time = input(": Enter thke Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time to wake up!.Time to wake up!.Time to wake up!.Time to wake up!.Time to wake up!.Time to wake up!.Time to wake up!.Time to wake up!.Time to wake up!.Time to wake up!.Time to wake up!.")
                    speak("Alarm Closed")

                elif now>time:
                    break

# -------------------------To find my location using ip address
        elif "where we are" in q:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https:/api.ipify.org').text #to find the ip address
                print(ipAdd)
                url = 'https"://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_request = requests.get(url)
                geo_data = geo_request.json()
                print (geo_data)
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f"Sir, i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("Sorry sir, Due to network issue i am not able to find where we are.")
                pass
# To read PDF
        elif "read pdf" in q:
            pdf_reader()

#-------------------------To hide files and folder------------
        elif "hide all files" in q or "hide this folder" in q or "visible for everyone" in q:
            speak("Sir please tell me you want to hide this folder or make it visible for everyone ")
            condition = takeCommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d") #os module
                speak("Sir, all the files in this folder are now hidden.")

            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("Sir, all the files in this folder are now visible to everyone. I wish you are taking this decision in your own peace.")

            elif "leave it" in condition or "leave for now" in condition:
                speak("ok sir")

        # elif "ipl score" in q:
        #
        #     from plyer import notification
        #
        #     import requests
        #
        #     from bs4 import BeautifulSoup  # pip install bs4
        #
        #     url = "https://www.cricbuzz.com/"
        #
        #     page = requests.get(url)
        #
        #     soup = BeautifulSoup(page.text, "html.parser")
        #
        #     team1 = soup.find_all(class_="cb-ovr-flo cb-msvc-tm-nm")[0].get_text()
        #
        #     team2 = soup.find_all(class_="cb-ovr-flo cb-msvc-tm-nm")[1].get_text()
        #
        #     team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
        #
        #     team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()
        #
        #     a = print(f"{team1} : {team1_score}")
        #
        #     b = print(f"{team2} : {team2_score}")
        #
        #     notification.notify(
        #
        #         title="IPL SCORE :- ",
        #
        #         message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
        #
        #         timeout=15
        #
        #     )#error

        elif "internet speed" in q:
            wifi = speedtest.Speedtest()
            upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
            download_net = wifi.download() / 1048576
            print("Wifi Upload Speed is", upload_net)
            print("Wifi download speed is ", download_net)
            speak(f"Wifi download speed is {download_net}")
            speak(f"Wifi Upload speed is {upload_net}")

        elif "shut down the system" in q:
            speak("Are You sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")

            elif shutdown == "no":
                speak("ok,as you say sir")

        elif 'remember that' in q:
            rememberMsg = q.replace("remember that","")
            rememberMsg = rememberMsg.replace("sifra","")
            speak("You tell me to remind you that :"+rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()

        elif 'what do you remember' in q:
            remember = open('data.txt','r')
            speak("You tell me that" + remember.read())

        elif "send email to parth" in q:
            try:
                speak("what should i say")
                content = takeCommand().lower()
                to = "parthsharmaujj@gmail.com"
                sendEmail(to,content)
                speak("Email has been send to Parth")

            except Exception as e:
                print(e)
                speak("Sorry Parth, I am not able to send this mail to Parth, Due to low internet connection")

        elif 'you can quit now' in q:
            speak("Deactivation Sequence Initiated, Thanks for using me Parth, have a good day.")
            sys.exit()