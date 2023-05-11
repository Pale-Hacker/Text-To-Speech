import os
import pyttsx3

# --- #

Engine = pyttsx3.init()

Engine.setProperty('volume', 1)

# --- #


def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def Banner():
    Clear()
    print(""" _______        _                _______                  _____                      _     
|__   __|      | |              |__   __|                / ____|                    | |    
   | | _____  _| |_    ______      | | ___     ______   | (___  _ __   ___  ___  ___| |__  
   | |/ _ \ \/ / __|  |______|     | |/ _ \   |______|   \___ \| '_ \ / _ \/ _ \/ __| '_ \ 
   | |  __/>  <| |_                | | (_) |             ____) | |_) |  __/  __/ (__| | | |
   |_|\___/_/\_\\\__|               |_|\___/             |_____/| .__/ \___|\___|\___|_| |_|
                                                               | |                         
                                                               |_|                         \nCreated By : Pale-Hacker\n""")

# --- #


Banner()

Text_Input = input("Enter Text : ")
File_Name = input("Enter File Name : ")

# --- #

Engine.save_to_file(Text_Input, f'{File_Name}.mp3')
Engine.runAndWait()

# --- #

if os.name == 'nt':
    os.system('start "" "{}"'.format(f"{File_Name}.mp3"))
else:
    os.system('xdg-open "{}"'.format(f"{File_Name}.mp3"))

# --- #
