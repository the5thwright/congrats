import pyautogui
import time
import subprocess

def write_love_message():
    # Open Notepad
    subprocess.Popen('notepad.exe')

    # Wait for Notepad to open
    time.sleep(1)

    # Type the message
    pyautogui.write('I love you')

if __name__ == '__main__':
    write_love_message()