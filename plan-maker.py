import pyautogui
from time import sleep

sleep(5)
# Função para realizar as ações
def realizar_acoes(repeticoes):
    for _ in range(repeticoes):
        pyautogui.click(1070, 352)
        sleep(0.5)
        pyautogui.click(1149,328)
        sleep(0.5)
        pyautogui.hotkey("ctrl", "t")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "t")
        sleep(0.1)
        pyautogui.click(1195,100)
        sleep(0.5)
        pyautogui.click(1233,221)
        sleep(0.5)
        pyautogui.write("25")
        sleep(0.5)
        pyautogui.press("enter")
        sleep(1)
        
         # Ações para a primeira parte
        pyautogui.doubleClick(1070, 352)
        sleep(0.1)
        pyautogui.doubleClick(1040, 452)
        sleep(0.1)

        pyautogui.hotkey("esc")
        pyautogui.hotkey("ctrl", "up")
        sleep(0.1)
        pyautogui.hotkey("left")
        sleep(0.1)
        pyautogui.hotkey("left")
        pyautogui.hotkey("down")
        pyautogui.hotkey("ctrl", "down")

    
        # Primeiro DK
         
        
       
        
        pyautogui.hotkey('shift', 'ctrl', 'down')
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'c')


        
        sleep(0.1)

        
        pyautogui.hotkey('alt', 'tab')
        
        sleep(0.1)
        # Colar os dks
        pyautogui.click(73, 248)
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'down')
        sleep(0.1)
        pyautogui.press('down')
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'v')
        sleep(0.1)
        pyautogui.hotkey('alt', 'tab')
        sleep(0.1)
        
        
        # Copiar os nomes
        pyautogui.doubleClick(1070, 352)
        sleep(0.1)
        pyautogui.doubleClick(1040, 452)
        sleep(0.1)

        pyautogui.hotkey("esc")
        pyautogui.hotkey("ctrl", "up")
        sleep(0.1)

        pyautogui.click(293,533) #Pegar posição para cada planilha
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'shift', 'down')
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'c')
        sleep(0.1)
        pyautogui.hotkey('alt', 'tab')
        sleep(0.1)

        # colar os nomes
        pyautogui.click(257, 250)
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'down')
        sleep(0.1)
        pyautogui.press('down')
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'v')
        sleep(0.1)
        pyautogui.hotkey('alt', 'tab')
        sleep(1) 
        
        # Concatenar componentes
        pyautogui.doubleClick(1070, 352)
        sleep(1)

        pyautogui.hotkey("esc")
        pyautogui.hotkey("ctrl", "up")
        sleep(0.5)
        
        pyautogui.typewrite('=CONCAT(A3;",";A4;",";A5;",";A6;",";A7;",";A8;",";A9;",";A10;",";A11;",";A12;",";A13;",";)')
        sleep(0.5)
        pyautogui.press('enter')
        sleep(1)
        pyautogui.hotkey("up")
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        sleep(0.5)
        pyautogui.hotkey('alt', 'tab') 
         
        #Colar os componentes
        sleep(1)
        pyautogui.click(651,232)
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'down')
        sleep(0.1)
        pyautogui.press('down')
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'v')
        sleep(2)
        pyautogui.hotkey('ctrl')
        sleep(2)
        pyautogui.press('v')
        sleep(2)
        pyautogui.hotkey('ctrl', 'c')
        sleep(0.5)
        pyautogui.press('left')
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'down')
        sleep(0.1)
        pyautogui.press('right')
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'shift', 'up')
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'v')
        sleep(0.1)
        pyautogui.hotkey('alt', 'tab')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'pagedown')
        sleep(0.1) 


# Define o número de repetições desejado
repeticoes = 10

# Inicia o loop de ações
realizar_acoes(repeticoes)
