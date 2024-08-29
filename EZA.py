import pyautogui
import time


FIGHT_X = 970
FIGHT_Y = 700
START_X = 1100
START_Y = 928

def wait_for_image(image_path, confidence=0.7, delay=7):
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location is not None:
                return location
            time.sleep(delay)
        except Exception as e:
            print(f"Waiting for image : {e}")
            time.sleep(delay)

def click_image(image_location):
    pyautogui.click(image_location)
    print(f"Image clicked : {image_location}")
    
while True:
    # Time to Start
    time.sleep(10)
    
    print("Searching SELECT LEVEL...")
    select_level_location = wait_for_image('./Asset/EZA_LVL.PNG')
    pyautogui.click(x=FIGHT_X, y=FIGHT_Y)
    print("SELECT LEVEL reconnu et clique.")

    print('Searching Start button...')
    bouton_start_location = wait_for_image('./Asset/EZA_START.PNG')
    click_image(bouton_start_location)

    print("Searching OK...")
    ok_screen_location = wait_for_image('./Asset/OK.PNG')
    click_image(ok_screen_location)

    print("Searching friend screen...")
    ami_screen_location = wait_for_image('./Asset/AMI.PNG')
    pyautogui.click(x=960, y=650)

    print("Searcing End screen...")
    end_screen_location = wait_for_image('/Asset/EZA_END.PNG')
    click_image(end_screen_location)

    print("Level Finished")
