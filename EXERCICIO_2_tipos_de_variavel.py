'''
**************************** QUESTÃO 1 **************************** 

Raciocínio:
A fórmula para conversão de Celsius para Fahrenheit é:
( x°C * 9/5) + 32
Logo, Recebemos a temperatura em Celsius do teclado. 
Calcular o grau em Celsius com a fórmula 
Printar na tela a temperatura em Fahrenheit.

'''

'''
celsius = float(input("Digite a temperatura em Celcius: "))                     #Entrada de dados sendo salva na variável celsius
fahrenheit = (celsius * (9/5)) + 32                                             #Fórmula para converter de Celsius para Fahrenheit e salvando o resultado na variável fahrenheit
print("A temperatura ", celsius, "em Celsius é ", fahrenheit, "em Fahrenheit")  #Printamos na tela os resultados
'''

'''
**************************** QUESTÃO 2 **************************** 
Raciocínio:
Inicialmente, precisamos pegar os 3 valores do teclado
Fazemos a soma desses valores e depois dividimos por 3
Fazemos a soma desses valores e fazemos a divisão inteira por 3
Fazemos a soma desses valores e calculamos o resto da divisão por 3
Printar na tela os resultados

'''


valor_1 = float(input("Digite o primeiro valor: "))                         #Entrada de dados sendo salva na variável valor_1
valor_2 = float(input("Digite o segundo valor: "))                          #Entrada de dados sendo salva na variável valor_2
valor_3 = float(input("Digite o terceiro valor: "))                         #Entrada de dados sendo salva na variável valor_3


soma = valor_1 + valor_2 + valor_3                                                                     #Os parentêses funcionam como na Matemática, dando prioridade para a operação dentro deles.
media = soma / 3                                   #Cálculo da Média sendo salvo na variável media
media_inteira = soma // 3                          #Cálculo da Média Inteira sendo salvo na variável media_inteira
resto = soma % 3                                   #Cálculo do Resto da Média Inteira sendo salvo na variável resto


print("Media: ", media)                                                     #Printamos a Média
print("Media Inteira", media_inteira)                                       #Printamos a Média Inteira
print("Resto da divisão inteira", resto)                                    #Printamos o Resto da Média Inteira