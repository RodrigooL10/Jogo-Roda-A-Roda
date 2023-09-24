import random
import csv

nome1 = input("Digite o nome do primeiro jogador: ")
nome2 = input("Digite o nome do segundo jogador: ")
nome3 = input("Digite o nome do terceiro jogador: ")

nomes = {
    'nome1':{'nome': nome1, 'pontuacao':0},
    'nome2':{'nome': nome2, 'pontuacao':0},
    'nome3':{'nome': nome3, 'pontuacao':0},
}

pontuacao = 0
valores = []
palavras = []

with open ('./opcoes.txt','r') as f:

    linha = f.readline()
    while linha:
        valor = int(linha)
        valores.append(valor)

        linha = f.readline()
    


with open ('./palavra.csv','r') as f:
    palavra = csv.reader(f)

    for linha in palavra:
        palavras += linha
    
    #Seleciona a palavra
    select2 = random.choice(palavras)

# print("Valor da roda:", select)
# print("Palavra selecionada:", select2)

if select2 == 'chocolate':
    print("Dica: Alimento doce")

elif select2 == 'elefante':
    print("Dica: Animal grande")

elif select2 == 'amarelo':
    print("Dica: É uma cor")


x = 1
dica = ["_" for _ in range(len(select2))]
contador = 0


while "_" in dica:
    nome_jogador = nomes['nome'+str(x)]['nome']
    pontuacaoJog = nomes['nome'+str(x)]['pontuacao']
    
    print("----- Painel -----")   
    for jogador, info in nomes.items():
        nome = info['nome']
        pontuacao = info['pontuacao']
        print(f"{nome}\t{pontuacao}")

    print(f"\nVez de {nome_jogador}:")

    #Seleciona o valor da roda
    num = random.randint(0, len(valores) - 1)
    select = valores[num]

    print(f"Valendo: R${select}")

    print(f"Palavra: {dica}")


    if select == 0:
        print("Jogador Perdeu tudo!")
        nomes['nome'+str(x)]['pontuacao'] = 0
        if x == 3:
            x = 1        
        else:
            x += 1
    
    else:
        if dica.count("_") == 3:
            arriscar = input("Deseja arriscar um palpite? ('S' para arriscar) ").lower()
            if arriscar == 's':
                palpite = input("Dê seu palpite: ")

                if palpite == select2:
                    print(f"Parabéns, {nome_jogador}! Você acertou a palavra!")
                    break
                else:
                    print(f"{nome_jogador} errou o palpite, perdeu tudo!")
                    nomes['nome'+str(x)]['pontuacao'] = 0
                    if x == 3:
                        x = 1
                    else:
                        x += 1

        tentativa = input("Digite uma letra: ")

        if tentativa in select2:            
            for i in range(len(select2)):
                if tentativa == select2[i]:
                    dica[i] = tentativa
                    contador += 1 #conta a qtd das letras inseridas na palavra

            print(f"{nome_jogador} acertou\n")
            pontuacaoJog += select * contador
            nomes['nome'+str(x)]['pontuacao'] += pontuacaoJog

            contador = 0

            if x == 3:
                x = 1
            
            else:
                x += 1

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

print(f"A palavra era: {select2}")

print(f"Parabéns,você venceu o jogo")

