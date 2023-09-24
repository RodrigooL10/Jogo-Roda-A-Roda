import random
import csv

nome1 = input("Digite o nome do primeiro jogador: ")
nome2 = input("Digite o nome do segundo jogador: ")
nome3 = input("Digite o nome do terceiro jogador: ")

nomes = {
    'nome1': {'nome': nome1, 'pontuacao': 0},
    'nome2': {'nome': nome2, 'pontuacao': 0},
    'nome3': {'nome': nome3, 'pontuacao': 0},
}

valores = []
palavras = []

with open('./opcoes.txt', 'r') as f:
    linha = f.readline()
    while linha:
        valor = int(linha)
        valores.append(valor)
        linha = f.readline()

with open('./palavra.csv', 'r') as f:
    word = csv.reader(f)
    for linha in word:
        palavras += linha

x = 1
dica = ["_ " * len(palavra) for palavra in palavras]

while "_ " in dica[0] or "_ " in dica[1] or "_ " in dica[2]:
    contador = 0
    nome_jogador = nomes['nome' + str(x)]['nome']
    pontuacaoJog = nomes['nome' + str(x)]['pontuacao']

    print("----- Painel -----")
    for jogador, info in nomes.items():
        nome = info['nome']
        pontuacao = info['pontuacao']
        print(f"{nome}\t\t{pontuacao}")

    print(f"\nVez de {nome_jogador}:")

    # Seleciona o valor da roda
    num = random.randint(0, len(valores) - 1)
    select = valores[num]

    print(f"Valendo: R$ {select}")
    for i in range(len(dica)):
        print(f"Palavra {i + 1}: {dica[i]}")

    if select == 0:
        print("Jogador Perdeu tudo!")
        nomes['nome' + str(x)]['pontuacao'] = 0
        if x == 3:
            x = 1
        else:
            x += 1

    else:
        tentativa = input("Digite uma letra: ").lower()

        for i in range(len(palavras)):
            palavra = palavras[i]
            if tentativa in palavra:
                acertou_letra = False
                for j in range(len(palavra)):
                    if tentativa == palavra[j]:
                        dica[i] = dica[i][:j * 2] + tentativa + dica[i][j * 2 + 1:]
                        contador += 1
                        acertou_letra = True

                if acertou_letra:
                    print(f"{nome_jogador} acertou!\n")
                    pontos = select * contador
                    nomes['nome' + str(x)]['pontuacao'] += pontos
                else:
                    print(f"{nome_jogador} errou\n")

        if x == 3:
            x = 1
        else:
            x += 1

print("----- Placar Final -----")
for jogador, info in nomes.items():
    nome = info['nome']
    pontuacao = info['pontuacao']
    print(f"{nome}\t{pontuacao}")

print(f"A palavras eram:")
print(palavras[0])
print(palavras[1])
print(palavras[2])

print(f"Parabéns, você venceu o jogo")
