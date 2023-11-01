import pyautogui
from time import sleep

pyautogui.alert("Pressione OK para iniciar")
# Abrir o 'abacos' e fazer login com seu usuário
pyautogui.press("winleft")
pyautogui.write("abacos")
sleep(1)  # Ajuste o intervalo conforme necessário
pyautogui.press("enter")
sleep(2)  # Aguarde alguns segundos para o 'abacos' abrir completamente
pyautogui.click(874, 469, duration=0.5)
sleep(1)
# Clique nos campos de login e digite as informações
pyautogui.click(760, 437, duration=0.5)
pyautogui.write("matheuscosta")
pyautogui.press("tab")
pyautogui.write("Connect@abc1")
pyautogui.press("enter")
sleep(5)

# Entre na tela de produtos
pyautogui.click(60, 61)
sleep(4)
pyautogui.doubleClick(54, 220)
sleep(2)

# Lista de produtos com código, nome, componentes e quantidades
produtos = [
    {
        "codigo": "298061",
        "nome": "Viés Vermelho Fino + Fita Led Vermelha + Xplode Vermelho",
        "componentes": [
            "291858",
            "246490",
            "67680",
            "246492",
            "20147",
            "80344",
            "80346",
            "249496",
            "248496",
            "248487",
            "249554",
            "169814",
        ],
        "quantidades": ["1", "2", "2", "2", "2", "1", "1", "1", "1", "1", "40", "1"],
    },
    {
        "codigo": "298062",
        "nome": "Viés Vermelho Largo + Fita Led Vermelha + Xplode Vermelho",
        "componentes": [
            "291858",
            "246490",
            "67680",
            "246492",
            "20147",
            "80344",
            "80346",
            "249496",
            "248496",
            "248488",
            "249554",
            "169814",
        ],
        "quantidades": ["1", "2", "2", "2", "2", "1", "1", "1", "1", "1", "40", "1"],
    },
    # Adicione mais produtos conforme necessário
]

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
        sleep(2)
        pyautogui.doubleClick(454, 574)
        sleep(2)

        # Preencher o nome do produto atual
        pyautogui.click(791, 298)
        sleep(0.5)
        pyautogui.hotkey("ctrl", "a")
        sleep(0.5)
        pyautogui.press("delete")
        sleep(0.5)
        pyautogui.write(nome_produto_atual)
        sleep(0.5)
        pyautogui.click(782, 322)
        pyautogui.hotkey("ctrl", "a")
        sleep(0.5)
        pyautogui.press("delete")
        sleep(0.5)
        pyautogui.write(nome_produto_atual)
        sleep(0.5)
        pyautogui.click(542, 369)
        pyautogui.hotkey("ctrl", "a")
        sleep(0.5)
        pyautogui.press("delete")
        sleep(0.5)
        pyautogui.write("Kit")
        sleep(0.5)
        pyautogui.click(758, 620)
        sleep(0.5)
        pyautogui.hotkey("ctrl", "end")
        sleep(0.5)
        pyautogui.press("space")
        sleep(0.5)
        pyautogui.write(nome_produto_atual)
        sleep(0.5)

        # Entrar na tela de componentes
        pyautogui.click(1011, 256)
        sleep(0.5)
        pyautogui.click(352, 304)
        sleep(0.5)
        pyautogui.click(375, 350)
        sleep(0.5)

        # Preencher os componentes e suas quantidades
        for componente, quantidade in zip(componentes, quantidades):
            pyautogui.click(763, 359)
            sleep(0.15)
            pyautogui.write(componente, interval=0.1)
            sleep(0.15)
            pyautogui.click(756, 591)
            sleep(0.15)
            pyautogui.hotkey("ctrl", "a")
            pyautogui.press("delete")
            pyautogui.write(str(quantidade))
            sleep(0.15)
            pyautogui.click(711, 309)
            sleep(0.15)
            pyautogui.press("enter")
        # validar para enquanto tiver componentes para o produto atual, ele deve ficar voltando e preenchendo componente e quantidade relacionada

        # Após acabar a quantidade de componentes fechar a tela de componentes
        pyautogui.press("esc")
        sleep(2)
        pyautogui.click(809, 505)
        sleep(2)

        # Após fechar a tela de componentes, fechar o produto
        pyautogui.click(955, 560)
        pyautogui.press("esc")
        sleep(2)
        pyautogui.press("enter")
        sleep(10)
        pyautogui.click(955, 560)
        sleep(10)
        pyautogui.press("esc")

        # Após concluir as ações para o produto atual, atualize o índice para o próximo produto
        index += 1

        if index < len(produtos):  # Verifica se há mais produtos na lista
            # Use os dados do próximo produto para continuar (por exemplo, o próximo código)
            proximo_produto = produtos[index]
            codigo_proximo_produto = proximo_produto["codigo"]

    # Após terminar voltar para tela de produto
    pyautogui.press("esc")
    sleep(2)

    pyautogui.alert("Trabaio escravo finalizado com sucesso")
