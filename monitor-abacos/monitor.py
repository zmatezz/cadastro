import time
import pyautogui

tempo_sem_resposta = 0  # Inicializa o contador de tempo sem resposta em segundos

while True:
    active_window_title = pyautogui.getActiveWindowTitle()
    
    if "Não está respondendo" in active_window_title:
        print(f"A janela está marcada como 'Não está respondendo'. Aguardando... {tempo_sem_resposta} segundos.")
        tempo_sem_resposta += 1  # Incrementa o contador
    else:
        if tempo_sem_resposta > 0:
            print(f"A janela estava sem resposta por {tempo_sem_resposta} segundos e agora está respondendo.")
            tempo_sem_resposta = 0  # Reseta o contador se a janela estiver respondendo

    # Aguarde 1 segundo antes de verificar novamente
    time.sleep(1)
