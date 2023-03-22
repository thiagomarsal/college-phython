# IT 280 – Lab #14: Program Launch Instructions
import subprocess
import os


def askForPath(text):
    isExist = False
    image = ''
    while isExist is False:
        image = input(text)
        isExist = os.path.exists(image)
    return image


def main():
    imagePath = './zophie.jpg'
    # imagePath = askForPath('Please, inform the absolute path for your image: ')
    subprocess.Popen(['C:\\Windows\\System32\\mspaint.exe', imagePath], bufsize=0)

    audioPath = './Scots Wha Hae.mp3'
    # audioPath = askForPath('Please, inform the absolute path for your audio: ')
    subprocess.Popen(['C:\\Program Files (x86)\\VideoLAN\\\VLC\\vlc.exe', audioPath], bufsize=0)

main()