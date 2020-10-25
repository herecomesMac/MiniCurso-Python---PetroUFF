'''
**************************** QUESTÃO 1 **************************** 
Raciocínio:
O fatorial de um número é calculado pela multiplicação desse número por todos os seus antecessores até chegar ao número 1.
Podemos fazer esse exercício tanto com while, quanto com for. Vamos fazer com os dois!
* Com While *
    Recebemos o número cujo fatorial será calculado.
    Enquanto este número for maior do que 1, eu multiplicamos este valor pelo valor anterior.
    Precisamos guardar o valor anterior em uma variável. 
    Printar na tela o fatorial

* Com For *
    Recebemos o número cujo fatorial será calculado.
    Para os valores num alcance entre o número e 1 (ou seja, estamos indo em ordem descrescente, logo, o incremento do for tem que ser -1), 
    multiplicamos estes valores pelo valor anterior.
    Precisamos guardar o valor anterior em uma variável.
    Printar na tela o fatorial
'''

############### While ###############

num = int(input("Digite o valor: "))            #Entrada de dados sendo salva na variável num

print("O fatorial de ", num)                    #Printo o valor de entrada agora, pois vou perdê-lo no decorrer do código
fatorial = 1                                    #Inicio a variavel fatorial para salvar os valores anteriores, iniciamos com 1, pois na multiplicação, 1 não altera o resultado

while num > 1:                                  #Enquanto a variável num for maior do que 1 eu faço o código indentado
    fatorial = fatorial * num                   #Multiplico o fatorial (que guarda o valor anteiror) pelo valor na variável num
    num = num - 1                               #Subtraio de um o valor da variável num para que eu vá para o próximo valor do fatorial
print("é ", fatorial)                           #Printo o resultado final da variável fatorial

num = int(input("Digite o valor: "))            #Entrada de dados sendo salva na variável num

############### For ###############

print("O fatorial de ", num)                    #Printo o valor de entrada agora, pois vou perdê-lo no decorrer do código
fatorial = 1                                    #Inicio a variavel fatorial para salvar os valores anteriores, iniciamos com 1, pois na multiplicação, 1 não altera o resultado

for i in range(num, 1, -1):                     #Para todos os valores dentro do alcance de [num , 1], eu faço o código indentado. Após o código identado ser realizado, eu incremento num de -1, ou seja, subtraio 1 de num.
    fatorial = fatorial * i                     #Multiplico o fatorial (que guarda o valor anteiror) pelo valor na variável num                 
print("é", fatorial)                            #Printo o resultado final da variável fatorial

'''
**************************** QUESTÃO 2 **************************** 
Raciocínio:
Pedir para o valor para o usuário.
Precisamos criar uma variável inicial com o elemento neutro da soma, para que possamos somar com o valor anterior.
Podemos fazer esse exercício tanto com while, quanto com for. Vamos fazer com os dois!
* Com While *
    Pede o valor ao usuário.
    Eleva o valor ao quadrado.
    Soma com o valor anterior
    Subtrai de -1 para poder mudar a condição.
* Com For *
    Pede o valor ao usuário.
    Eleva o valor ao quadrado.
    Soma com o valor anterior.
'''

############### While ###############

quant_valores = int(input("Insira a quantidade de valores que serão calculados: "))      #Entrada de dados sendo salva na variável quant_valores
soma_dos_quadrados = 0                                                                   #Variável que guardará a soma dos quadrados, iniciada com 0, pois na soma, 0 não altera o resultado
while quant_valores > 0:                                                                 #Enquanto o valor em quant_valores for maior que 0, eu faço o código indentado
    valor = float(input("Digite o valor: "))                                             #Entrada de dados sendo salva na variável valor
    soma_dos_quadrados = soma_dos_quadrados + (valor**2)                                 #Relizamos o quadrado do valor entrado (sendo feito primeiro, pois está entre parênteses) e depois fazemos a soma com a variável quant_valores
    quant_valores = quant_valores - 1                                                    #Subtraímos quant_valores de 1 para não entrarmos em loop infinito

print("A soma dos quadrados dos valores é: ", soma_dos_quadrados)                        #Printamos o restulado

############### For ###############

quant_valores = int(input("Insira a quantidade de valores que serão calculados: "))     #Entrada de dados sendo salva na variável quant_valores
soma_dos_quadrados = 0                                                                  #Variável que guardará a soma dos quadrados, iniciada com 0, pois na soma, 0 não altera o resultado
for i in range(quant_valores):                                                          #Para os valores dentro do alcance de [0, quant_valore], eu faço o código indentado. Após o código identado ser realizado, eu incremento de 1.
    valor = float(input("Digite ", i,"o valor: "))                                      #Entrada de dados sendo salva na variável valor
    soma_dos_quadrados = soma_dos_quadrados + (valor**2)                                #Relizamos o quadrado do valor entrado (sendo feito primeiro, pois está entre parênteses) e depois fazemos a soma com a variável quant_valores

print("A soma dos quadrados dos valores é: ", soma_dos_quadrados)                       #Printamos o restulado

