from pynput import mouse
import pyautogui
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

def clean_ocr_text(text):
    """Remove common OCR garbage"""
    # Remove special characters and noise
    import re
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Keep only letters and spaces
    text = text.replace('istenе', '')  # Remove known false readings
    text = text.replace('listeheron', '')
    text = text.strip().lower()
    return text

def getGUItext(x, y):
    try:
        ix, iy = int(x), int(y)
        
        # Try different capture positions
        # Button text is usually above or inside the button
        positions = [
            (ix-60, iy-40, 120, 50),   # Above click
            (ix-60, iy-25, 120, 40),   # Center
            (ix-60, iy-50, 120, 50),   # Higher up
        ]
        
        for left, top, width, height in positions:
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            
            # Enhance image
            screenshot = screenshot.convert('L')  # Grayscale
            screenshot = screenshot.point(lambda x: 0 if x < 140 else 255, '1')  # Binarize
            
            text = pytesseract.image_to_string(screenshot).strip()
            text = clean_ocr_text(text)
            
            # Common button texts
            buttons = ["submit", "next", "login", "sign", "ok", "cancel", 
                       "save", "delete", "edit", "continue", "allow", "deny",
                       "back", "yes", "no", "agree", "click", "button", "send"]
            
            for button in buttons:
                if button in text:
                    return button.capitalize()
            
            if len(text) > 2 and len(text) < 20:
                return text.capitalize()
        
        return "Unknown"
        
    except Exception as e:
        return "Unknown"

def handleClick(x, y, button, pressed):
    if pressed:
        text = getGUItext(x, y)
        print(f"Clicked: {text} at ({int(x)},{int(y)})")

print("Improved Button Detector")
print("Press Ctrl+C to stop\n")

listener = mouse.Listener(on_click=handleClick)
listener.start()
listener.join()