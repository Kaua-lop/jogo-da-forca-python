import random

palavras = []

print('Temas: [1]Desenhos [2]Filmes [3]Frutas [4]Jogos')
escolha = input('Escolha um tema: ')

try: #Verifica se o usuario digitou um numero e se ele digitou um numero valido
    escolha = int(escolha)
    if escolha == 1:
        print('Tema escolhido: Desenhos')
        palavras = ['ScoobyDoo','Shrek','PicaPau','Madagáscar ','Barbie']
    elif escolha == 2:
        print('Tema escolhido: Filmes')
        palavras = ['Herege','Nos','Ferias','Ted','Observada']
    elif escolha == 3:
        print('Tema escolhido: Frutas')
        palavras = ['Abacaxi','Laranja','Maca','Pera','Uva']
    elif escolha == 4:
        print('Tema escolhido: Jogos')
        palavras = ['Minecraft','Valorant','Terraria','Fortnite','CounterStrike']
    else:
        print('Porfavor escolha um tema valido!')
        
except: 
    print('Como você chegou aqui?')
    

#Sorteia uma palavra da lista.
palavra_sorteada = random.choice(palavras).upper() #choice = escolhe uma palavra da lista aleatoria.
    
#String com traços representando as letras.
letras_escondidas = '*' * len(palavra_sorteada) #len = comprimento da palavra.

letras_advinhadas = [] #Armazena as letras advinhadas.
tentativas = 6 #Quantidade de tentativas.

while True:
    #Mostrar na tela a palavra escondida
    print(letras_escondidas)

    #Perguntar a letra
    letra = input('Digite uma letra: ').upper() #upper = torna a letra maiuscula.

    #Verificar se a letra ja foi digitada
    if letra in letras_advinhadas:
        print('Essa letra ja foi digitada')
        continue
    #Adicionar a letra a lista de letras digitadas
    letras_advinhadas.append(letra)
        
    #Verificar se a letra esta na palavra sorteada
    if letra in palavra_sorteada:
        #Substituir o asterisco pela Letra
        lista = []
        for i in range(len(palavra_sorteada)):
            if letra == palavra_sorteada[i]:
                lista.append(letra)
            else:
                lista.append(letras_escondidas[i])
        letras_escondidas = ''.join(lista) #Se o jogador a letra "a" então teremos = *a**a*

    else: #Se a letra nao estiver na palavra sorteada
        #Diminuir a quantidade de tentativas
        tentativas -= 1
        print('Letra não encontrada. Você tem mais {} tentativas'.format(tentativas))

        #Verificar se o jogador perdeu
    if letras_escondidas == palavra_sorteada:
        print('Parabéns! Venceu! A palavra era: {}'.format(palavra_sorteada))
        break
    elif tentativas == 0:
        print('Perdeu! A palavra era: {}'.format(palavra_sorteada))
        break