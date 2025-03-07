import pyttsx3
import threading
import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia #type:ignore
import pywhatkit #type:ignore
import webbrowser as wb
import os
import random
import pyautogui #type:ignore
import sqlite3
from time import sleep
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import pyjokes #type:ignore
import keyboard #type:ignore
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  #type:ignore
import threading

engine = pyttsx3.init()
chat_bubbles=[]
conn = sqlite3.connect("jasim.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS memory (id INTEGER PRIMARY KEY, data TEXT)")
conn.commit()
dictApp = {
    "command prompt": "cmd",
    "word": "winword",
    "excel": "EXCEL",
    "google chrome": "chrome",
    "pycharm": "pycharm64",
    "edge": "msedge",
    "browser": "chrome",
    "powerpoint": "POWERPNT",
    "powershell": "powershell",
    "one note": "onenote",
    "media player": "VLC",
    "sublime text": "C:\\Program Files\\Sublime Text\\sublime_text",
    "spotify": "spotify",
    "notepad": "notepad",
    "my computer": "explorer",
    "settings": "ms-settings:"
}

def openAppWeb(query):
    speak("Working on that, sir")
    add_chat_bubble(chat_container,"Working on that, sir","assistant")
    if ".com" in query or ".co.in" in query or ".org" or ".ac.in" in query:
        query = query.replace("open", "")
        query = query.replace("jasim", "")
        query = query.replace("launch", "")
        query = query.replace("slash", "/")
        query = query.replace(" ", "")
        wb.open(f"https://www.{query}")
        speak(f"Opening {query}")
        add_chat_bubble(chat_container,f"Opening {query}","assistant")
    else:
        keys = list(dictApp.keys())
        for app in keys:
            if app in query:
                speak(f"Opening {app}")
                add_chat_bubble(chat_container,f"Opening {app}","assistant")
                os.system(f"start {dictApp[app]}")

def closeAppWeb(query):
    speak("Closing, sir")
    add_chat_bubble(chat_container,"Closing, sir","assistant")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("One tab is closed, sir")
        add_chat_bubble(chat_container,"One tab is closed, sir","assistant")
    elif "to tabs" in query or "2 tabs" in query or "2 tab" in query or "to tab" in query or "too tabs" in query or "too tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("Two tabs are closed, sir")
        add_chat_bubble(chat_container,"Two tabs are closed, sir","assistant")
    else:
        keys = list(dictApp.keys())
        for app in keys:
            if app in query:
                speak(f"Closing {app}")
                add_chat_bubble(chat_container,f"Closing {app}","assistant")
                os.system(f"taskkill /f /im {dictApp[app]}.exe")

def speak(audio) -> None:
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        add_chat_bubble(chat_container,"Listening...","assistant")
        r.pause_threshold = 1
        r.energy_threshold = 170
        audio = r.listen(source, 0, 6)
    try:
        print("Recognizing...")
        add_chat_bubble(chat_container,"Recognizing...","assistant")
        query = r.recognize_google(audio, language="en-in")
        print(query)
        add_chat_bubble(chat_container,query,"user")
    except Exception as e:
        print(e)
        speak("Please Try again")
        add_chat_bubble(chat_container,"Please try again","assistant")
        return "Try Again"
    return query

def add_chat_bubble(chat_container, message, sender):
    bubble_frame = tk.Frame(chat_container, bg="white")
    bubble_frame.pack(fill="x", padx=10, pady=5, anchor="w" if sender == "assistant" else "e")
    bg_color = "#FFFFFF" if sender == "user" else "#DCF8C6"
    text_color = "black"
    alignment = tk.RIGHT if sender == "user" else tk.LEFT
    message_label = tk.Label(
        bubble_frame, 
        text=message, 
        bg=bg_color, 
        fg=text_color,
        font=("Arial", 12),
        wraplength=450, 
        justify=alignment,
        relief=tk.RAISED,
        borderwidth=1
    )
    message_label.pack(side=alignment, padx=5, pady=5)
    timestamp = datetime.datetime.now().strftime("%I:%M %p")
    timestamp_label = tk.Label(
        bubble_frame,
        text=timestamp,
        font=("Arial", 8),
        bg="white",
        fg="gray"
    )
    if sender == "user":
        timestamp_label.pack(anchor="e")
    else:
        timestamp_label.pack(anchor="w")

    chat_container.update_idletasks()
    chat_container.master.yview_moveto(1.0)

def time() -> None:
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)
    add_chat_bubble(chat_container,f"The current time is {Time}","assistant")

def date() -> None:
    day: int = datetime.datetime.now().day
    month: int = datetime.datetime.now().month
    year: int = datetime.datetime.now().year
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print(f"The current date is {day}/{month}/{year}")
    add_chat_bubble(chat_container,f"The current date is {day}/{month}/{year}","assistant")

def wishme() -> None:
    hour: int = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
        add_chat_bubble(chat_container,"Good Morning Sir!!","assistant")
    elif 12 <= hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
        add_chat_bubble(chat_container,"Good Afternoon Sir!!","assistant")
    elif 16 <= hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
        add_chat_bubble(chat_container,"Good Evening Sir!!","assistant")
    else:
        speak("Good Evening Sir!!")
        add_chat_bubble(chat_container,"Good Evening Sir!!","assistant")
    speak("JASIM at your service sir, please tell me how may I help you.")
    print("JASIM at your service sir, please tell me how may I help you.")
    add_chat_bubble(chat_container,"JASIM at your service sir, please tell me how may I help you.","assistant")

def screenshot() -> None:
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\ss.png")
    img.save(img_path)

def sendWhatsAppMessage():
    contact_book={"tejas":"+919019853268","yuvraj":"+919449931713","shastri":"+918147543946"}
    try:
        speak("To whom should I send the message? Please provide the name.")
        add_chat_bubble(chat_container,"To whom should I send the message? Please provide the name.","assistant")
        name = takecommand().lower()
        if name == "try again":
            speak("I couldn't capture the name. Please try again.")
            add_chat_bubble(chat_container,"I couldn't capture the name. Please try again.","assistant")
            return
        phone = contact_book.get(name)
        if not phone:
            speak(f"I couldn't find {name} in your contact book. Please try again.")
            print(f"Unknown contact: {name}")
            add_chat_bubble(chat_container,f"Unknown contact:{name}","assistant")
            return
        speak("What is the message?")
        add_chat_bubble(chat_container,"What is the message?","assistant")
        message = takecommand()
        if message.lower() == "try again":
            speak("I couldn't capture the message. Please try again.")
            add_chat_bubble(chat_container,"I couldn't capture the message. Please try again.","assistant")
            return
        speak(f"Sending the following message: {message} to {name}")
        print(f"Name: {name}, Phone: {phone}, Message: {message}")
        add_chat_bubble(chat_container,f"Name: {name}, Phone: {phone}, Message: {message}","assistant")
        time_now = datetime.datetime.now()
        schedule_minute = (time_now.minute + 2) % 60
        schedule_hour = time_now.hour + ((time_now.minute + 2) // 60)
        def send_message():
            pywhatkit.sendwhatmsg(phone, message, schedule_hour, schedule_minute)
            sleep(30) 
            pyautogui.press("enter") 
        thread = threading.Thread(target=send_message)
        thread.start()        
        speak("Message scheduled successfully.")
        print("Message scheduled successfully.")
        add_chat_bubble(chat_container,"Message scheduled successfully.","assistant")
    except Exception as e:
        speak("I encountered an error while sending the message. Please try again.")
        add_chat_bubble(chat_container,"I encountered an error while sending the message. Please try again.","assistant")
        print("Error:", str(e))
        
def remember_data(data: str) -> None:
    cursor.execute("DELETE FROM memory")  
    cursor.execute("INSERT INTO memory (data) VALUES (?)", (data,))
    conn.commit()
    speak("You said me to remember that " + data)
    print("You said me to remember that " + data)
    add_chat_bubble(chat_container,f"You said me to remember that {data}","assistant")

def searchYouTube(query):
    if "youtube" in query:
        speak("working on that, sir")
        add_chat_bubble(chat_container,"Working on that,sir","assistant")
        query = query.replace("jasim", "")
        query = query.replace("youtube", "")
        query = query.replace("youtube search", "")
        query = query.replace("search", "")
        query = query.replace("on", "")
        web = "https://www.youtube.com/results?search_query=" + query
        speak(f"searching {query} on youtube")
        add_chat_bubble(chat_container,f"Searching {query} on youtube","assistant")
        wb.open(web)
        pywhatkit.playonyt(query)
        speak("This is what i found for your search on youtube")
        add_chat_bubble(chat_container,"This is what i found for your search on youtube","assistant")
        speak("Done, sir")
        add_chat_bubble(chat_container,"Done, sir","assistant")

def recall_data() -> None:
    cursor.execute("SELECT data FROM memory LIMIT 1")
    result = cursor.fetchone()
    if result:
        data = result[0]
        speak("You told me to remember that " + data)
        print("You told me to remember that " + data)
        add_chat_bubble(chat_container,f"You told me to remember that {data}","assistant")
    else:
        speak("I don't remember anything.")
        add_chat_bubble(chat_container,"I don't remember anything.","assistant")

def send_email():
    try:
        sender_email = "noir51617@gmail.com"
        sender_password = "lcga lroq ppzk srdd"  
        speak("To whom should I send the email? Please provide the email address.")
        add_chat_bubble(chat_container,"To whom should I send the email? Please provide the email address.","assistant")
        recipient_email = takecommand().lower()
        recipient_email = recipient_email.replace(" at ", "@").replace(" ", "")
        speak("What is the subject of the email?")
        add_chat_bubble(chat_container,"What is the subject of the mail?","assistant")
        subject = takecommand()
        speak("What should I say in the email?")
        add_chat_bubble(chat_container,"What should I say in the email?","assistant")
        body = takecommand()
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
        speak("Email has been sent successfully, sir!")
        add_chat_bubble(chat_container,"Email sent successfully,sir!","assistant")
    except smtplib.SMTPAuthenticationError:
        print("Invalid login credentials or less secure app access not enabled.")
        speak("I encountered an issue with the email credentials. Please check your settings.")
        add_chat_bubble(chat_container,"I encountered an issue with the email credentials. Please check your settings.","assistant")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
        speak("I encountered an error while sending the email. Please try again.")
        add_chat_bubble(chat_container,"I encountered an error while sending the email. Please try again.","assistant")

def get_weather():
    try:
        api_key = "acc6e8e72bc174b106ea87cb7e3a7b65"  
        speak("Please tell me the name of the city.")
        add_chat_bubble(chat_container,"Please tell me the name of the city","assistant")
        city = takecommand().lower()  
        city = city.replace(" ", "")  
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(base_url)
        weather_data = response.json()
        if weather_data["cod"] == 200:
            city_name = weather_data["name"]
            country = weather_data["sys"]["country"]
            temperature = weather_data["main"]["temp"]
            feels_like = weather_data["main"]["feels_like"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]
            weather_desc = weather_data["weather"][0]["description"]
            weather_report = (
                f"The weather in {city_name}, {country} is currently {weather_desc}.\n"
                f"The temperature is {temperature}°C, but it feels like {feels_like}°C.\n"
                f"The humidity level is {humidity}%, and the wind speed is {wind_speed} meters per second."
            )
            print(weather_report)
            speak(weather_report)
            add_chat_bubble(chat_container,f"The weather in {city_name}, {country} is currently {weather_desc}.","assistant")
            add_chat_bubble(chat_container,f"The temperature is {temperature}°C, but it feels like {feels_like}°C.","assistant")
            add_chat_bubble(chat_container,f"The humidity level is {humidity}%, and the wind speed is {wind_speed} meters per second.","assistant") 
        else:
            speak("Sorry, I couldn't find the weather information for that city. Please try again.")
            print("City not found. Please check the name and try again.")
            add_chat_bubble(chat_container,"City not found. Please check the name and try again.","assistant")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("I encountered an error while fetching the weather information. Please try again.")
        add_chat_bubble(chat_container,"I encountered an error while fetching the weather information. Please try again.","assistant")

def volumeUp():
    for _ in range(5):
        keyboard.press_and_release('volume up') 
        sleep(0.1)

def volumeDown():
    for _ in range(5):
        keyboard.press_and_release('volume down') 
        sleep(0.1)

def play_music():
    song_dir = os.path.expanduser("~\\Music")
    try:
        songs = [file for file in os.listdir(song_dir) if file.endswith(('.mp3', '.wav'))]
        if songs:
            song = random.choice(songs)
            song_path = os.path.join(song_dir, song)
            os.startfile(song_path)
            speak(f"Playing {song}")
            add_chat_bubble(chat_container, f"Playing {song}", "assistant")
        else:
            speak("No songs found in your Music folder.")
            add_chat_bubble(chat_container, "No songs found in your Music folder.", "assistant")
    except Exception as e:
        speak("An error occurred while trying to play music.")
        add_chat_bubble(chat_container, "An error occurred while trying to play music.", "assistant")
        print("Error:", str(e))

def start_listening_thread():
    listen_thread = threading.Thread(target=assistant_response, daemon=True)
    listen_thread.start()

def assistant_response():
    query = takecommand().lower()
    if "time" in query:
        time()

    elif "wish me" in query:
        wishme()

    elif "send email" in query or "email" in query:
        send_email()

    elif "date" in query:
        date()

    elif "who are you" in query:
        speak("I'm JASIM created by Mr.Yuvraj and Mr.Vishnu and I'm a desktop voice assistant.")
        print("I'm JASIM created by Mr.Yuvraj and Mr.Vishnu and I'm a desktop voice assistant.")
        add_chat_bubble(chat_container,"I'm JASIM created by Mr.Yuvraj and Mr.Vishnu and I'm a desktop voice assistant.","assistant")

    elif "what does jasim mean" in query:
        speak("JASIM STANDS FOR JUST A SIMPLE INTELLIGENT MACHINE")
        print("JASIM STANDS FOR JUST A SIMPLE INTELLIGENT MACHINE.")
        add_chat_bubble(chat_container,"JASIM STANDS FOR JUST A SIMPLE INTELLIGENT MACHINE.","assistant")

    elif "how are you" in query:
        speak("I'm fine sir, What about you?")
        print("I'm fine sir, What about you?")
        add_chat_bubble(chat_container,"I'm fine sir, what about you?","assistant")

    elif "fine" in query or "good" in query:
        speak("Glad to hear that sir!!")
        print("Glad to hear that sir!!")
        add_chat_bubble(chat_container,"Glad to hear that sir!!","assistant")

    elif "open" in query:
        query = query.replace("open", "")
        query = query.replace("jasim", "")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.sleep(2)
        pyautogui.press("enter")
        speak(f"Opening {query}")
        add_chat_bubble(chat_container,f"Opening {query}","assistant")

    elif "open" in query and "open youtube" not in query:
        openAppWeb(query)

    elif "close" in query:
        closeAppWeb(query)

    elif "wikipedia" in query:
        try:
            speak("Ok wait sir, I'm searching...")
            add_chat_bubble(chat_container,"Ok wait sir,I'm searching...","assistant")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
            add_chat_bubble(chat_container,result,"assistant")
        except:
            speak("Can't find this page sir, please ask something else")
            add_chat_bubble(chat_container,"Can't find this page sir, please ask something else","assistant")

    elif "open youtube" in query:
        wb.open("youtube.com")
        
    elif "weather" in query:
        get_weather()
        
    elif "youtube" in query:
        searchYouTube(query)

    elif "open google" in query:
        wb.open("google.com")

    elif "open stack overflow" in query:
        wb.open("stackoverflow.com")

    elif "play music" in query:
        play_music()

    elif "open chrome" in query:
        chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chromePath)

    elif "search on chrome" in query:
        try:
            speak("What should I search?")
            print("What should I search?")
            add_chat_bubble(chat_container,"What should I search?","assistant")
            search = takecommand()  
            search_url = "https://www.google.com/search?q=" + search.replace(" ", "+")  
            wb.open_new_tab(search_url)  
            print("Searching for:", search)
            add_chat_bubble(chat_container,f"Searching for:{search}","assistant")
        except Exception as e:
            speak("Can't open now, please try again later.")
            print("Can't open now, please try again later:", str(e)) 
            add_chat_bubble(chat_container,"Can't open now, Please try again later","assistant") 

    elif "remember that" in query:
        speak("What should I remember?")
        add_chat_bubble(chat_container,"What should I remember","assistant")
        data = takecommand()
        remember_data(data)

    elif "do you remember anything" in query:
        recall_data()

    elif "screenshot" in query:
        screenshot()
        speak("I've taken a screenshot, please check it")
        add_chat_bubble(chat_container,"I've taken the screenshot, please check it","assistant")
              
    elif "send a message" in query or "whatsapp" in query or "message" in query:
        sendWhatsAppMessage()
        speak("Please wait a minute")
        add_chat_bubble(chat_container,"Please wait a minute","assistant")

    elif "joke" in query:
        get = pyjokes.get_joke()
        speak(get)
        add_chat_bubble(chat_container,get,"assistant")

    elif "pause" in query:
        pyautogui.press("k")
        speak("Video paused, sir")
        add_chat_bubble(chat_container,"Video paused,sir","assistant")

    elif "play" in query:
        pyautogui.press("k")
        speak("video played, sir")
        add_chat_bubble(chat_container,"Video played,sir","assistant")

    elif "mute" in query:
        pyautogui.press("m")
        speak("Video Muted, Sir")
        add_chat_bubble(chat_container,"Video muted,sir","assistant")

    elif "full screen" in query:
        pyautogui.press("f")

    elif "mini player" in query:
        pyautogui.press("f")

    elif "normal screen" in query:
        pyautogui.press("i")

    elif "theatre mode" in query:
        pyautogui.press("t")

    elif "subtitle" in query:
        pyautogui.press("c")

    elif "next" in query:
        pyautogui.hotkey("shift", "n")
        sleep(0.5)
        speak("Playing new video, sir")
        add_chat_bubble(chat_container,"Playing new video,sir","assistant")

    elif "previous" in query:
        pyautogui.hotkey("shift", "p")
        sleep(0.5)
        speak("Playing previous video, sir")
        add_chat_bubble(chat_container,"Playing previous video,sir","assistant")

    elif "unmute" in query:
        pyautogui.press("m")
        speak("Video Un Muted, Sir")
        add_chat_bubble(chat_container,"Video UnMuted,Sir","assistant")

    elif "volume up" in query:
        speak("Turning volume up, sir")
        add_chat_bubble(chat_container,"Turning volume up,sir","assistant")
        volumeUp()

    elif "volume down" in query:
        speak("Turning volume down, sir")
        add_chat_bubble(chat_container,"Turning volume down,sir","assistant")
        volumeDown()
      
    elif "take a picture" in query:
        pyautogui.press("super")
        pyautogui.typewrite("camera")
        pyautogui.press("enter")
        pyautogui.sleep(2)
        speak("Smile Please, sir")
        add_chat_bubble(chat_container,"Smile please,sir","assistant")
        pyautogui.press("enter")

    elif "offline" in query:
        conn.close()  
        quit()

def create_scrollable_chat_frame(root, window_width, window_height):
    chat_frame = tk.Frame(root, bg="white")
    chat_frame.pack(fill="both", expand=True)
    canvas = tk.Canvas(chat_frame, bg="white", highlightthickness=0)
    scrollbar = ttk.Scrollbar(chat_frame, orient="vertical", command=canvas.yview)
    chat_container = tk.Frame(canvas, bg="white", width=window_width)
    canvas_frame = canvas.create_window((0, 0), window=chat_container, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(canvas_frame, width=canvas.winfo_width())
    
    chat_container.bind("<Configure>", update_scrollregion)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    return chat_frame, canvas, chat_container


root = tk.Tk()
root.title("JASIM Assistant")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = screen_width // 2
window_height = screen_height - 100
root.geometry(f"{window_width}x{window_height}")
root.resizable(False, False)
root.configure(bg="white")

header_frame = tk.Frame(root, bg="#25D366", height=50)
header_frame.pack(fill="x")
header_label = tk.Label(
header_frame,
text="JASIM Assistant",
bg="#25D366",
fg="white",
font=("Arial", 16, "bold")
)
header_label.pack(pady=10)
    
chat_frame, chat_canvas, chat_container = create_scrollable_chat_frame(root, window_width, window_height)
footer_frame = tk.Frame(root, bg="white", height=80)
footer_frame.pack(fill="x")
    
try:
    mic_icon = Image.open("mic_icon.png").resize((50, 50), Image.Resampling.LANCZOS)
    mic_photo = ImageTk.PhotoImage(mic_icon)
except FileNotFoundError:
    print("mic_icon.png not found. Using a placeholder.")
    mic_photo = None

mic_button = tk.Button(
    footer_frame,
    image=mic_photo if mic_photo else None,
    bg="white",
    bd=0,
    activebackground="white",
    command=start_listening_thread
)
mic_button.pack(pady=10)
    
add_chat_bubble(chat_container, "Hello! I'm JASIM, your desktop assistant.", "assistant")
add_chat_bubble(chat_container, "How can I help you?", "assistant")
    
root.mainloop()