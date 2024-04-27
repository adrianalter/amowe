import pyautogui
import time
from cv2 import imread

def playSpotify():
    pyautogui.hotkey("alt", "right")
    time.sleep(1)

def nextTab(tab):
    pyautogui.hotkey("ctrl", tab)

def playNextSong():
    image = imread('ytbutton.png')
    counter = 0
    print("(((((((((((( STARTING ))))))))))))")
    while True:
        time.sleep(23)
        pyautogui.hotkey("ctrl", "right")  # Spotify
        time.sleep(1)  # Wait for 1 second
        pyautogui.hotkey("ctrl", "2")
        time.sleep(1)
        pyautogui.hotkey("ctrl", "right")  # tidal
        time.sleep(1)  # Wait for 1 second
        pyautogui.hotkey("ctrl", "3")  # YT Music
        time.sleep(2)
        
        try:
            forward_button = pyautogui.locateOnScreen(image)
            if forward_button is not None:
                button_center = pyautogui.center(forward_button)
                pyautogui.click(button_center)
                print("Clicked YT")
                time.sleep(1)  # Wait for 1 second
            else:
                print("Forward button not found on the screen.")
        except Exception as e:
            print(f"An error occurred while attempting to click the button: {str(e)}")
        
        time.sleep(2)
        pyautogui.hotkey("ctrl", "4")
        time.sleep(1)
        pyautogui.hotkey("ctrl", "right")  # Spotify
        time.sleep(1)  # Wait for 1 second
        pyautogui.hotkey("ctrl", "1")
        
        counter += 1
        print("--------------Played " + str(counter) + " times")

if __name__ == "__main__":
    playNextSong()
