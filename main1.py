import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import news
import fitness
import education

#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif c.lower().startswith("play"):
        name = c.lower().replace("play", " ", 1).strip()

    if name in musiclibrary.music:
        link = musiclibrary.music[name]

    elif name in news.channels:
        link = news.channel[name]

    elif name in fitness.videos:
        link = fitness.videos[name]

    elif name in education.courses:
        link = education.courses[name]
       
    else:
        speak(f"Sorry, I could not find {name}")
        print(f"{name} not found")
        return
        webbrowser.open(link)
if __name__ == "__main__":
    speak("responding Vortex......")
    while True:
        #listen for the wake word "vertex"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listining...")
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
            word=r.recognize_google(audio)
            print("You said:", word)
            if"vortex" in (word.lower()): 
                speak("ya")
                #listen for command
                with sr.Microphone() as source:
                  print("vortex active...")
                  audio = r.listen(source)
                  command = r.recognize_google(audio)
                  
                  processcommand(command)
                  
        
        except Exception as e:
            print("Error; {0}".format(e))





    
    