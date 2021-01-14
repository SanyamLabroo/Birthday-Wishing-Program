from __future__ import print_function
import pyttsx3
import speech_recognition as sr
import time
from itertools import chain, repeat
import winsound
import pyfiglet
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)       #1 for female voice and 0 for male voice


name = input("Enter Birthday Boy's/Girl's Name: ")
sender = input("Enter sender's name: ")

if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

time.sleep(2)

print('Ha', end='')
winsound.Beep(264, 250)
time.sleep(500/2000.0)
print('ppy ', end='')
winsound.Beep(264, 250)
time.sleep(250/2000.0)
print('birth', end='')
winsound.Beep(297, 1000)
time.sleep(250/2000.0)
print('day ', end='')
winsound.Beep(264, 1000)
time.sleep(250/2000.0)
print('to ', end='')
winsound.Beep(352, 1000)
time.sleep(250/2000.0)
print('you')
winsound.Beep(330, 2000)
time.sleep(500/2000.0)

print('Ha', end='')
winsound.Beep(264, 250)
time.sleep(500/2000.0)
print('ppy ', end='')
winsound.Beep(264, 250)
time.sleep(250/2000.0)
print('birth', end='')
winsound.Beep(297, 1000)
time.sleep(250/2000.0)
print('day ', end='')
winsound.Beep(264, 1000)
time.sleep(250/2000.0)
print('to ', end='')
winsound.Beep(396, 1000)
time.sleep(250/2000.0)
print('you')
winsound.Beep(352, 2000)
time.sleep(500/2000.0)

print('Ha', end='')
winsound.Beep(264, 250)
time.sleep(250/2000.0)
print('ppy ', end='')
winsound.Beep(264, 500)
time.sleep(250/1000.0)
print('birth', end='')
winsound.Beep(440, 1000)
time.sleep(250/2000.0)
print('day ', end='')
winsound.Beep(352, 1000)
time.sleep(250/2000.0)
print('dear ', end='')
winsound.Beep(330, 1000)
print(name)
time.sleep(250/2000.0)
winsound.Beep(297, 1000)

winsound.Beep(440, 1000)
time.sleep(250/2000.0)

time.sleep(500/2000.0)
print('Ha', end='')
winsound.Beep(466, 250)
time.sleep(500/2000.0)
print('ppy ', end='')
winsound.Beep(466, 250)
time.sleep(250/2000.0)
print('birth', end='')
winsound.Beep(440, 1000)
time.sleep(250/2000.0)
print('day ', end='')
winsound.Beep(352, 1000)
time.sleep(250/2000.0)
print('to ', end='')
winsound.Beep(396, 1000)
time.sleep(250/2000.0)
print('you')
winsound.Beep(352, 2000)
time.sleep(250/2000.0)


result1 = pyfiglet.figlet_format("Happy", font = "slant" ) 
result2 = pyfiglet.figlet_format("Birthday", font = "slant" ) 
result3 = pyfiglet.figlet_format(name, font = "slant" ) 
time.sleep(2.5)
print(result1) 
time.sleep(2.5)
print(result2)
time.sleep(2.5)
print(result3)
time.sleep(2.5)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()


lst = ["Happy birthday to you dear" + name, "May god bless you", "Hope all you'r wishes comes true.", 
            "Again a very Happ Birthday to you.", "Enjoy your day.", "From" + sender]


for i in chain.from_iterable(repeat(lst, 1)):
    time.sleep(0.1)
    speak(i)
