'''
**************************** QUESTÃO 1 **************************** 
Raciocínio:

Inicialmente, precisamos pegar os duas listas do teclado
Pegamos valor a valor e colocamos numa Lista dentro do código para as duas Forças
Depois, precisamos inteirar elemento à elemento dentro da Lista
E guardar esses valores em uma lista.
'''


############### Pegando valor a valor ###############

forca_1 = []                                                    #Iniciamos a lista forca_1 vazia
forca_2 = []                                                    #Iniciamos a list forca_2 vazia
print("Digite os valores para o primeiro vetor de Força")       #Apenas um print para ajudar o usuário visualmente
for i in range(3):                                              #Para um alcance entre [0,3], eu faço o que está indentado. Após o código identado ser realizado, eu incremento de 1.
    valor = int(input("Digite o valor: "))                      #Entrada de dados sendo salva na variável valor
    forca_1.append(valor)                                       #Acrescentamos a variável valor no final da Lista forca_1

print("Digite os valores para o segundo vetor de Força")        #Apenas um print para ajudar o usuário visualmente
for i in range(3):                                              #Para um alcance entre [0,3], eu faço o que está indentado
    valor = int(input("Digite o valor: "))                      #Entrada de dados sendo salva na variável valor
    forca_2.append(valor)                                       #Acrescento a variável valor no final da Lista forca_2

forca_resultante = []                                           #Iniciamos a lista forca_resultante vazia
for i in range(3):                                              #Para um alcance entre [0,3], eu faço o que está indentado. Após o código identado ser realizado, eu incremento de 1.
    soma = forca_1[i] + forca_2[i]                              #Somamos o elemento da Lista forca_1 que está na posição i, o elemento da Lista forca_2 que está na posição i e guardo o resultado na variável soma
    forca_resultante.append(soma)                               #Acrescentamos a variável soma no final da Lista forca_resultante

print("A Força Resultando é: ", forca_resultante)               #Printamos o restulado

'''
**************************** QUESTÃO 1 **************************** 
Raciocínio:

Inicialmente, precisamos pegar as duas matrizes.
Pegamos valor a valor e colocamos numa Lista dentro do código e depois dentro de outra Lista para formar a matriz. 
    Vamos precisar de um For dentro de outro For. Um para percorrer coluna e outro para percorrer linha
Fazemos o mesmo acima para a segunda matriz.
Para calcular a matriz_resultante: 
    Vamos precisar de dois For. Um para percorrer coluna e outro para percorrer linha.
    Precisamos somar os elementos da Primeira Matriz e da Segunda Matriz que estejam na mesma Coluna e na mesma Linha.
    Precisamos guardar este valor em uma variável.
'''

matriz_1 = []                                                   #Iniciamos a lista matriz_1 vazia
matriz_2 = []                                                   #Iniciamos a lista matriz_2 vazia

for i in range(2):                                              #Para um alcance entre [0,2], eu faço o que está indentado. Após o código identado ser realizado, eu incremento de 1.                   
    lista = []                                                  #Iniciamos a lista lista vazia, isso é importante pois nas passadas dentro do For, precisamos que lista não tenha nenhum lixo da passada anterior             
    for j in range(2):                                          #Para um alcance entre [0,2], eu faço o que está indentado. Após o código identado ser realizado, eu incremento de 1.                   
        valor = int(input("Digite o valor: "))                  #Entrada de dados sendo salva na variável valor
        lista.append(valor)                                     #Acrescento a variável valor no final da Lista lista
    matriz_1.append(lista)                                      #Acrescento a variável lista no final da Lista matriz_1. Perceba que a variável lista já terá dois elementos por causa do segundo For.

print("Primeira Matriz: ")                                      #Apenas um print para ajudar o usuário visualmente
for i in range(2):                                              #Para um alcance entre [0,2], eu faço o que está indentado. Após o código identado ser realizado, eu incremento de 1.                   
    print(matriz_1[i])                                          #Printamos a variável matriz_1 nesta posição

for i in range(2):                                              #Para um alcance entre [0,2], eu faço o que está indentado. Após o código identado ser realizado, eu incremento de 1.                   
    lista = []                                                  #Iniciamos a lista lista vazia, isso é importante pois nas passadas dentro do For, precisamos que lista não tenha nenhum lixo da passada anterior                          
    for j in range(2):                                          #Para um alcance entre [0,2], eu faço o que está indentado. Após o código identado ser realizado, eu incremento de 1.                   
        valor = int(input("Digite o valor: "))                  #Entrada de dados sendo salva na variável valor
        lista.append(valor)                                     #Acrescento a variável valor no final da Lista lista
    matriz_2.append(lista)                                      #Acrescento a variável lista no final da Lista matriz_2. Perceba que a variável lista já terá dois elementos por causa do segundo For.

print("Segunda Matriz: ")                                       #Apenas um print para ajudar o usuário visualmente
for i in range(2):                                              #Para um alcance entre [0,2], eu faço o que está indentado. Após o código identado ser realizado, eu incremento de 1.                   
    print(matriz_2[i])                                          #Printamos a variável matriz_2 nesta posição

matriz_resultante = []                                          #Iniciamos a lista matriz_resultante vazia

for i in range(2):                                              #Para um alcance entre [0,2], eu faço o que está indentado. Após o código identado ser realizado, eu incremento de 1.                   
    lista = []                                                  #Iniciamos a lista lista vazia, isso é importante pois nas passadas dentro do For, precisamos que lista não tenha nenhum lixo da passada anterior                          
    for j in range(2):                                          #Para um alcance entre [0,2], eu faço o que está indentado. Após o código identado ser realizado, eu incremento de 1.                   
        valor = matriz_1[i][j] + matriz_2[i][j]                 #Somamos os elementos das variáveis matriz_1 e matriz_2 que estão na mesma coluna e mesma linha
        lista.append(valor)                                     #Acrescento a variável valor no final da Lista lista
    matriz_resultante.append(lista)                             #Acrescento a variável lista no final da Lista matriz_resultante. Perceba que a variável lista já terá dois elementos por causa do segundo For.

print("Resultado: ")                                            #Apenas um print para ajudar o usuário visualmente
for i in range(2):                                              #Para um alcance entre [0,2], eu faço o que está indentado. Após o código identado ser realizado, eu incremento de 1.                   
    print(matriz_resultante[i])                                 #Printamos a variável matriz_resultante nesta posição