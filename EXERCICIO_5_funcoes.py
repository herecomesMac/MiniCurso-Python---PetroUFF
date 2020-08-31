'''
**************************** QUESTÃO 1 **************************** 
Raciocínio:

Precisamos primeiro pedir ao usuário o valor de n.
Depois, chamamos a função passando n como paramêtro.

Para criar a função:
    Precisamos de uma função que receba como paramêtro um valor.
    A função precisa ficar fazendo uma soma repetidamente, logo, usamos uma Estrutura de Repetição. Pode ser While ou For.
    Precisamos salvar esta soma em algum lugar.
    Precisamos retornar o valor da soma.

Como retornamos um valor, precisamos de uma variável para guardar este retorno.
Printamos na tela o resultado
'''


def soma_dos_inteiros(n):                           # Criação da função soma_dos_inteiros que recebe n como um paramêtro
    soma = 0                                        # Variável soma que se inicia com 0, pois 0 na adição não altera o resultado.
    for i in range(n+1):                            # Para valores entre 0 e n+1, faça o que está indentado.
        soma = soma + i                             # Soma recebe o que já estava em soma + o valor de i (neste caso, valores entre 0 e n+1)
    return soma                                     # Retornamos o valor guardado na variável soma



n = int(input("Digite o valor de n: "))             # Entrada de dados sendo salva na variável n
resultado = soma_dos_inteiros(n)                    # Chamada da função soma_dos_inteiros passando como paramêtro a variável n e recebendo o retorno na variável resultado

print("O resultado é: ", resultado)                 # Printamos o resultado na tela