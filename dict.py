perguntas = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5x5',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

jogo_acabou = False
while jogo_acabou == False:
    i = 0
    acertos = 0
    while i < 3:
        d = 0
        print(f"Pergunta: {perguntas[i]['Pergunta']}")
        print("Opções:")
        while d < 4:
            print(f"{d + 1}) {perguntas[i]['Opções'][d]}")
            d = d + 1
        resposta = int(input("Escolha uma opção:"))
        resposta = resposta - 1
        if perguntas[i]['Opções'][resposta] == perguntas[i]['Resposta']:
            i = i + 1
            print("Acertou!")
            print()
            acertos = acertos + 1
            if i == 3:
                print(f"Você acertou {acertos} de 3 perguntas.")
                jogo_acabou = True
        else:
            i = i + 1
            print("Errou!")
            print()
            if i == 3:
                print(f"Você acertou {acertos} de 3 perguntas.")
                jogo_acabou = True