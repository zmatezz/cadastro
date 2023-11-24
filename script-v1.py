import pyautogui
from time import time, sleep
import openpyxl

""" 
pyautogui.alert('Pressione OK para iniciar')
# Abrir o 'abacos' e fazer login com seu usuário
pyautogui.press('winleft')
pyautogui.write('Abacos - Atalho')
sleep(5)  # Ajuste o intervalo conforme necessário
pyautogui.press('enter')
sleep(6)  # Aguarde alguns segundos para o 'abacos' abrir completamente
pyautogui.click(874, 469, duration=0.5)
sleep(5)
# Clique nos campos de login e digite as informações
pyautogui.click(760, 437, duration=0.5)
pyautogui.write('matheuscosta')  
pyautogui.press('tab')
pyautogui.write('Connect@abc1')  
pyautogui.press('enter')
sleep(8)

#Entre na tela de produtos
pyautogui.click(60,61)
sleep(4)
pyautogui.doubleClick(54,220)
sleep(4) """

# Abrir a planilha do Excel
workbook = openpyxl.load_workbook("DKS.xlsx")
sheet = workbook.active


# Inicializar array de produtos
produtos = []

# Loop atráves das linhas da planilha para criar a lista de produtos
for row in sheet.iter_rows(min_row=2, values_only=True):
    codigo = str(row[0])
    nome = row[1]
    componentes = row[2].split(",")
    quantidades = row[3].split(",")

    produto = {
        "codigo": codigo,
        "nome": nome,
        "componentes": componentes,
        "quantidades": quantidades,
    }

    produtos.append(produto)

# Fechar a planilha
workbook.close()

# Inicializa o índice do produto atual
index = 0

while index < len(produtos):  # Enquanto houver produtos na lista
    produto = produtos[index]  # Obtenha o produto atual

    for index, produto in enumerate(produtos):
        codigo_produto_atual = produto["codigo"]
        nome_produto_atual = produto["nome"]
        componentes = produto["componentes"]
        quantidades = produto["quantidades"]
        # Localize um produto pelo DK
        pyautogui.click(150, 171)
        sleep(1)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("delete")
        sleep(1)
        pyautogui.write(codigo_produto_atual)
        sleep(2)
        pyautogui.click(1568, 132)
        sleep(4)
        pyautogui.doubleClick(610, 544)
        sleep(4)

        # Preencher o nome do produto atual
        pyautogui.click(791, 298)
        sleep(0.01)
        pyautogui.hotkey("ctrl", "a")
        sleep(0.01)
        pyautogui.press("delete")
        sleep(0.01)
        pyautogui.write(nome_produto_atual)
        sleep(0.01)
        pyautogui.click(782, 322)
        pyautogui.hotkey("ctrl", "a")
        sleep(0.01)
        pyautogui.press("delete")
        sleep(0.01)
        pyautogui.write(nome_produto_atual)
        sleep(0.01)
        pyautogui.click(542, 369)
        pyautogui.hotkey("ctrl", "a")
        sleep(0.01)
        pyautogui.press("delete")
        sleep(0.01)
        pyautogui.write("Kit")
        sleep(0.01)
        pyautogui.click(758, 620)
        sleep(0.01)
        pyautogui.hotkey("ctrl", "end")
        sleep(0.01)
        pyautogui.press("space")
        sleep(0.01)
        pyautogui.write(nome_produto_atual)
        sleep(0.01)
        pyautogui.click(891, 617)
        sleep(0.01)

        # Entrar na tela de componentes
        pyautogui.click(1011, 256)
        sleep(0.50)
        pyautogui.click(352, 304)
        sleep(0.50)
        pyautogui.click(375, 350)
        sleep(0.50)

        # Preencher os componentes e suas quantidades
        for componente, quantidade in zip(componentes, quantidades):
            pyautogui.click(763, 359)
            sleep(0.01)
            pyautogui.write(componente)
            sleep(0.01)
            pyautogui.click(756, 591)
            sleep(0.01)
            pyautogui.hotkey("ctrl", "a")
            pyautogui.press("delete")
            pyautogui.write(str(quantidade))
            sleep(0.01)
            pyautogui.click(711, 309)
            sleep(0.01)
            pyautogui.press("enter")
        # validar para enquanto tiver componentes para o produto atual, ele deve ficar voltando e preenchendo componente e quantidade relacionada

        # Após acabar a quantidade de componentes fechar a tela de componentes
        pyautogui.press("esc")
        sleep(2)

        # Após fechar a tela de componentes, fechar o produto
        pyautogui.press("esc")
        sleep(2)
        pyautogui.press("enter")
        contador = 1
        start_time = time()
        while True:
            active_window_title = pyautogui.getActiveWindowTitle()
            if "Produto" in active_window_title:
                print(f"Aguarde o erro no sistema. Aguardando... {contador} segundos")
                contador += 1
                if time() - start_time > 2400:
                    print("Erro no sistema. Encerrando o script")
                    break

                sleep(1)
            else:
                sleep(3)
                break

        """ while True:
            active_window_title = pyautogui.getActiveWindowTitle()
            if "Produto (Não está respondendo)" in active_window_title:
                print("Não está respondendo. Aguardando...")
                sleep(1)
            else:
                break """
        sleep(2)
        pyautogui.click(955, 560)
        sleep(2)

        pyautogui.press("esc")
        sleep(2)

        # Após concluir as ações para o produto atual, atualize o índice para o próximo produto
        index += 1

        if index < len(produtos):  # Verifica se há mais produtos na lista
            # Use os dados do próximo produto para continuar (por exemplo, o próximo código)
            proximo_produto = produtos[index]
            codigo_proximo_produto = proximo_produto["codigo"]

    # Após terminar voltar para tela de produto
    pyautogui.press("esc")
    sleep(2)

    pyautogui.alert("Sistema de cadastro finalizado com sucesso")
