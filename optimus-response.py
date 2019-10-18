#!/usr/bin/python3
from pynput import keyboard
import time

def velofix_part(prompt, size=100):
    return prompt+ ", What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills."

log=""
def on_press(key):
    global log
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        log= log+key.char
    except AttributeError:
        print('special key {0} pressed'.format(key))
        if key== keyboard.Key.space:
            log+=" "
        if key== keyboard.Key.enter:
            log+="\n"
        if key== keyboard.Key.backspace:
            log=log[:-1]

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.pause or key== keyboard.Key.f12:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
print("vomiting")
listener.stop()

time.sleep(0.5)
keyboard.Controller().type(velofix_part(log))
