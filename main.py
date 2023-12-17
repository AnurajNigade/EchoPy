import os

import speech_recognition as sr
import win32com.client
import webbrowser
import openai
import datetime
import random
speaker = win32com.client.Dispatch("SAPI.SpVoice")

chatStr = ""
def chat(query):
    global chatStr
    # print(chatStr)  # Optional
    openai.api_key = "Open-API-key"
    chatStr += f"Anuraj: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    speaker.Speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = "Open-API-key"
    text = f"OpenAI response for Prompt: {prompt} \n ********************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1,2343434356)}.txt","w") as f:
    with open(f"Openai/{''.join(prompt.split('ai')[1:]).strip() }.txt", "w") as f:
        f.write(text)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"



if __name__ == '__main__':
    speaker.Speak("Jarvis AI")
    while 1:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com/"],
               ["wikipedia","https://www.wikipedia.com"],
               ["hackerrank","https://www.hackerrank.com/profile/anuraj_nigade"],
               ["github","https://github.com/"],
               ["leetcode","https://leetcode.com/Anuraj_Nigade/"],
               ["chat gpt","https://chat.openai.com/"],
                ["linkedin ", "https://www.linkedin.com/in/anurajnigade/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} Sir....")
                webbrowser.open(site[1])

        if "open music" in query:
            music_path=r"D:\Song\LITE_BRITE.mp3"
            os.startfile(music_path)

        elif "the time" in query:
            strfTimme = datetime.datetime.now().strftime("%H:%M:%S")
            speaker.Speak(f"Sir the time is {strfTimme}")

        elif "open vscode" in query:
            os.startfile(r'C:\Users\user\AppData\Local\Programs\Microsoft VS Code\Code.exe')

        elif "Using ai".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)






        # speaker.Speak(query)
