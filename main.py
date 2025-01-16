import os
import webbrowser
import openai
import speech_recognition as sr
from config import apikey
import datetime

chatStr = ""

def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"User: {query} \n Assistant: "
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query}
    ],
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

    reply = response["choices"][0]["message"]["content"].strip()
    chatStr += f"{reply}\n"
    print(f"Assistant: {reply}")
    say(reply)
def say(text):
    os.system(f'say "{text}"')
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Sorry, I didnt catch that.")
            return "Some error occured. "
            
if __name__ == "__main__":
    print("Hello my name is Victor your AI Assistant! ")
    say("Hello my name is Victor your AI Assistant! ")
    
    while True:
        query = takeCommand().lower()

        if "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            say("Opening Youtube ")
        elif "open google" in query:
            webbrowser.open("https://www.google.com")
            say("Opening Google. ")
        elif "open canvas " in query:
            webbrowser.open("https://canvas.fiu.edu")
            say("Opening FIU canvas")
        elif "what time is it" in query:
            now = datetime.datetime.now()
            say(f"The time is {now.strftime('%H:%M')}. ")
        else:
            chat(query)

'''
to start the AI Agent i have to activate the virtual enviroment 

python -m venv env 

source env/bin/activate

then i have to install the dependancies 

pip install openai SpeechRecognition pyaudio

pip freeze > requirements.txt

pip install -r requirements.txt


'''


            
            
            



