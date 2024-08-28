import pyautogui
import time

# Coordonnees des boutons pour lancer l'event
FIGHT_X = 970
FIGHT_Y = 700
START_X = 1100
START_Y = 928

def wait_for_image(image_path, confidence=0.7, delay=7):
    """Attend que l'image soit trouvee sur l'ecran."""
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location is not None:
                return location
            print(f"Image non detectee : {image_path}. Nouvel essai dans {delay} sec.")
            time.sleep(delay)
        except Exception as e:
            print(f"Erreur lors de la recherche de l'image : {e}")
            time.sleep(delay)

def click_image(image_location):
    """Clique sur la position de l'image trouvee."""
    pyautogui.click(image_location)
    print(f"Image cliquee : {image_location}")
    
while True:
    # Pause initiale
    time.sleep(10)
    
    # Verification et action pour le niveau selectionne
    print("Recherche de SELECT LEVEL...")
    select_level_location = wait_for_image('./Asset/EZA_LVL.PNG')
    pyautogui.click(x=FIGHT_X, y=FIGHT_Y)
    print("SELECT LEVEL reconnu et clique.")

    # Verification et action pour le boutton start
    print('Recherche du boutton start...')
    bouton_start_location = wait_for_image('./Asset/EZA_START.PNG')
    click_image(bouton_start_location)

    # Verification et action pour l'ecran OK
    print("Recherche de l'ecran OK...")
    ok_screen_location = wait_for_image('./Asset/OK.PNG')
    click_image(ok_screen_location)

    # Verification et action pour l'ecran d'ami
    print("Recherche de l'ecran d'ami...")
    ami_screen_location = wait_for_image('./Asset/AMI.PNG')
    pyautogui.click(x=960, y=650)

    # Verification et action pour l'ecran de fin
    print("Recherche de l'ecran de fin...")
    end_screen_location = wait_for_image('/Asset/EZA_END.PNG')
    click_image(end_screen_location)

    print("Niveau Fini")
