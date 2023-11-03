import time
import pyautogui

while True:
    active_window_title = pyautogui.getActiveWindowTitle()
    if "Não está respondendo" in active_window_title:
        print("A janela está marcada como 'Não está respondendo'.")

    # Aguarde 1 segundo antes de verificar novamente
    time.sleep(1)
sleep(2)
