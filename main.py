
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishme():

    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak(" Good Afternoon!")
    else: 
        speak("Good Evening!")

    speak("Hello , I am Nicholas!")
    speak("I think Today is a great day")
    speak("Today we are Going to learn Alphabet")
    speak("A for Apple , B for Ball , C for Cat , D for Dog , E for Elephant , F for Fish , G for Grapes , H for Horse ,I for Ice Cream , J for Joker ,K for kite , L for Lion , M for Monkey, N for Nest , O for Orange ,P for Parrot , Q for Queen , R for rabbit ,S for Sun, T for Tiger, U for Umbrella , V for Van  , W for Watermelon,X for X-Ray,Y for Yak,Z for Zebra")


if __name__ == "__main__":
    wishme()