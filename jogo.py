import random
import csv

nome1 = input("Digite o nome do primeiro jogador")
nome2 = input("Digite o nome do segundo jogador")
nome3 = input("Digite o nome do terceiro jogador")

nomes = {
    'nome1':nome1,
    'nome2':nome2,
    'nome3':nome3
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
    
    num = random.randint(0, len(valores) - 1)

    #Seleciona o valor da roda
    select = valores[num]

with open ('./palavra.csv','r') as f:
    palavra = csv.reader(f)

    for linha in palavra:
        palavras += linha
    
    #Seleciona a palavra
    select2 = random.choice(palavras)

print("Valor da roda:", select)
print("Palavra selecionada:", select2)

if select2 == 'Chocolate':
    print("Dica: Alimento doce")

elif select2 == 'Elefante':
    print("Dica: Animal grande")

elif select2 == 'Amarelo':
    print("Dica: É uma cor")

jogador1 = jogador2 = jogador3 = 0

x = 1

while True:
    val = 'nome' + str(x)
    nome = nomes.get(val)

    print(f"Vez de {nome}:")

    if select == 0:
        print("Jogador Perdeu tudo!")
        x += 1   
    
    tentativa = input("Digite uma letra")

    if tentativa in select2:
        print(f"{nome} acertou")
