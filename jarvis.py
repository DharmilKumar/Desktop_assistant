import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")

    speak(" I am desktop assistent sir, please tell me how may I help You")
def takeCommand():
    #It takes microphone input from the user and returns string output
    
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Listening...")
    #     r.pause_threshold = 1
    #     audio = r.listen(source)
    # try:
    #     print("Recognizing...")    
    #     query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
    #     print(f"User said: {query}\n")  #User query will be printed.

    # except Exception as e:
    #     print(e)    
    #     print("Say that again please...")   
    #     return "None"
    # return query

    #for manual search
    print("Write whatever you want to do")
    query = input()
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email@gmail.com', 'password')
    server.sendmail('email@gmail.com', to, content)
    server.close()   
if __name__=="__main__" :
    wishMe()
    while True:
        query = takeCommand().lower() 

        
        if 'wikipedia' in query:  
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com/in/dharmilkumar")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            path = "c:\\Users\\91814\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(path)
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "aefwefEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("mail is not send, please try again")