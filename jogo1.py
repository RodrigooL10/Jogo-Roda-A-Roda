import random
import csv

#Recebe os nomes dos jogadores
nome1 = input("Digite o nome do primeiro jogador: ")
nome2 = input("Digite o nome do segundo jogador: ")
nome3 = input("Digite o nome do terceiro jogador: ")

#variável que auxiliará para saber o jogador, durante o loop principal
x = 1

#armazena os nomes e a pontuação num dicionário
nomes = {
    'nome1': {'nome': nome1, 'pontuacao': 0},
    'nome2': {'nome': nome2, 'pontuacao': 0},
    'nome3': {'nome': nome3, 'pontuacao': 0},
}

#variáveis que receberão os dados dos arquivos .txt e .csv
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
    
    resposta1 = palavras[0]
    resposta2 = palavras[1]
    resposta3 = palavras[2]


dica = []
for palavra in palavras:
    dica.append("_ " * len(palavra))

palavras_adivinhadas = [False] * len(palavras)

print("\n-Dicas das palavras: 1º- Um animal; 2º- Um alimento doce; 3º- Uma cor")


while "_ " in dica[0] or "_ " in dica[1] or "_ " in dica[2]:
    contador = 0
    nome_jogador = nomes['nome' + str(x)]['nome']

    print(f"\nVez de {nome_jogador}:")

    encontrou = False
    for d in dica:
        if d.count("_ ") == 3:
            encontrou = True
            break
        if d.count("_ ") == 2:
            encontrou = True
            break
        if d.count("_ ") == 1:
            encontrou = True
            break

    #Arriscar chute
    if encontrou:
        for i in range(len(dica)):
            print(f"Palavra {i + 1}: {dica[i]}")
            
        arriscar = input("Deseja arriscar um palpite? ('S' para arriscar) ").lower()
        if arriscar == 's':
            palpite = input("Dê seu palpite: ")
            palavra_correta = None
    
        # Encontre a posição da palavra no palavras
        for i, palavra in enumerate(palavras):
            if palpite == palavra and not palavras_adivinhadas[i]:
                palavra_correta = i
                break

        if palavra_correta is not None:
            print(f"\n-- Parabéns, {nome_jogador}! Você acertou a palavra! --\n")
            
            # Atualize a dica da palavra correta
            dica[palavra_correta] = palpite
            
            # Marca a palavra como adivinhada
            palavras_adivinhadas[palavra_correta] = True
            
            # Prêmio ao acertar a palavra, dobra a pontuação
            pontuacaoJog = nomes['nome' + str(x)]['pontuacao']
            nova_pontuacao = pontuacaoJog * 2
            nomes['nome' + str(x)]['pontuacao'] = nova_pontuacao

            #muda a vez para o próximo
            if x == 3:
                x = 1
            else:
                x += 1

                #mostra o placar atualizado
            print("----- Placar -----")
            for jogador, info in nomes.items():
                nome = info['nome']
                pontuacao = info['pontuacao']
                print(f"{nome}\t\t{pontuacao}")

            #exibe o nome do próximo jogador
            nome_jogador = nomes['nome' + str(x)]['nome']
            print(f"\nVez de {nome_jogador}:")

            #se errar o palpite, jogador perde tudo
        else:
            print(f"{nome_jogador} errou o palpite, perdeu tudo!\n")
            nomes['nome' + str(x)]['pontuacao'] = 0

            #muda a vez para o próximo jogador
            if x == 3:
                x = 1
            else:
                x += 1

            #exibe o placar atualizado
            print("----- Placar -----")
            for jogador, info in nomes.items():
                nome = info['nome']
                pontuacao = info['pontuacao']
                print(f"{nome}\t\t{pontuacao}")

            #exibe o nome do próximo jogador
            nome_jogador = nomes['nome' + str(x)]['nome']
            print(f"\nVez de {nome_jogador}:")
    

    #se todas as palavras forem adivinhadas, determina fim do loop while
    if palavras_adivinhadas[0] == True and palavras_adivinhadas[1] == True and palavras_adivinhadas[2] == True:
        break

    # Seleciona o valor da roda
    num = random.randint(0, len(valores) - 1)
    select = valores[num]

    #exibe a dica e quanto está valendo cada acerto nessa rodada
    print(f"Valendo: R$ {select}")
    for i in range(len(dica)):
        print(f"Palavra {i + 1}: {dica[i]}")


    #Jogador perde tudo
    if select == 0:
        nome_jogador = nomes['nome' + str(x)]['nome']
        print(f"\n\n--- {nome_jogador} Perdeu tudo! ---\n\n")
        nomes['nome' + str(x)]['pontuacao'] = 0
        if x == 3:
            x = 1
        else:
            x += 1
    
    #Jogador passa a vez
    elif select == 1:
        nome_jogador = nomes['nome' + str(x)]['nome']
        print(f"\n\n--- {nome_jogador} Perdeu tudo! ---\n\n")
        if x == 3:
            x = 1
        else:
            x += 1

    #Jogador tenta uma letra
    else:
        tentativa = input("Digite uma letra: ").lower()

        #checa se possui a letra nas palavras
        for i in range(len(palavras)):
            palavra = palavras[i]
            if tentativa in palavra and tentativa not in dica[i]:
                acertou_letra = False
                for j in range(len(palavra)):
                    if tentativa == palavra[j] and dica[i][j * 2] == "_":
                        dica[i] = dica[i][:j * 2] + tentativa + dica[i][j * 2 + 1:]
                        acertou_letra = True

                if acertou_letra:
                    print(f"{nome_jogador} acertou!\n")
                    contador += palavra.count(tentativa) #conta a quantidade da letra nas palavras
                
                else:
                    print(f"{nome_jogador} errou\n")
        
        #faz o cálculo da pontuação
        pontos = select * contador
        nomes['nome' + str(x)]['pontuacao'] += pontos
        
        #exibe o placar
        print("----- Placar -----")
        for jogador, info in nomes.items():
            nome = info['nome']
            pontuacao = info['pontuacao']
            print(f"{nome}\t\t{pontuacao}")

        #muda a vez
        if x == 3:
            x = 1
        else:
            x += 1
        
    
# Verifica se todas as palavras foram adivinhadas e remove as adivinhadas
novas_palavras = []
novas_dica = []
novas_palavras_adivinhadas = []

# Itere pelas listas originais e copie apenas os elementos não adivinhados para as novas listas
for i in range(len(palavras)):
    if not palavras_adivinhadas[i]:
        novas_palavras.append(palavras[i])
        novas_dica.append(dica[i])
        novas_palavras_adivinhadas.append(palavras_adivinhadas[i])

# Atualize as listas originais com as novas listas
palavras = novas_palavras
dica = novas_dica
palavras_adivinhadas = novas_palavras_adivinhadas

print("----- Placar Final -----")
for jogador, info in nomes.items():
    nome = info['nome']
    pontuacao = info['pontuacao']
    print(f"{nome}\t{pontuacao}")

print(f"A palavras eram:")
print(resposta1)
print(resposta2)
print(resposta3)

vencedor = ''
pontuacao_vencedor = -1  # Inicializa com um valor baixo para garantir que qualquer pontuação seja maior

for jogador, jogador_info in nomes.items():
    pontuacao = jogador_info['pontuacao']
    if pontuacao > pontuacao_vencedor:
        pontuacao_vencedor = pontuacao
        vencedor = jogador_info['nome']

print(f"\n\n----- Parabéns {vencedor} você venceu o jogo! -----")