import pygetwindow as gw
import pyautogui
from pynput import keyboard
import time

def mostrar_imagen_ascii():
    # Leer y mostrar el contenido del archivo furina_ascii.txt con codificación UTF-8
    try:
        with open("furina_ascii.txt", "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("The file furina_ascii.txt was not found.")
    except UnicodeDecodeError:
        print("Error reading the file: possible encoding issue.")

def focus_youtube():
    windows = [w for w in gw.getAllWindows() if "YouTube" in w.title]
    if windows:
        windows[0].activate()  # Activar la primera ventana que contenga "YouTube"
        time.sleep(0.2)  # Espera un poco para asegurar el foco
        return True
    return False

def send_youtube_shortcut(key):
    if focus_youtube():
        pyautogui.press(key)

def on_press(key):
    try:
        if key == keyboard.Key.media_next:
            send_youtube_shortcut('right')  # Adelantar 5 segundos
        elif key == keyboard.Key.media_previous:
            send_youtube_shortcut('left')  # Retroceder 5 segundos
    except AttributeError:
        pass


def main():
    mostrar_imagen_ascii()  # Mostrar la imagen ASCII al inicio
    print ("Press the forward and backward buttons on your multimedia keyboard to skip forward or backward 5 seconds on YouTube.")# Mostrar instrucciones
    print ("To exit the program, close this window.") 
    print ("Created by Ryuunosuke28") # Mostrar el nombre del creador
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
