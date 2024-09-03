# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será
# a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a 
# sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence 
# ou não a sequência. 

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência 
# ou pode ser previamente definido no código;

def Fibonacci():
    try:
        number = int(input("Digite um possivel numero da sequencia de Fibonacci: "))

        fist, second, constant = 0, 1, 0
        fibonacci = [fist, second]
        while True:

            constant = fist + second
            fibonacci.append(constant)

            if constant == number or number == 0:
                print(f'\nO {number} esta nos valores de Fibonacci')
                break
            elif constant > number:
                print(f'O {number} não esta na sequencia de Fibonacci')
                break

            fist = second
            second = constant

        print()
        print(f'Sequencia de Fibonacci:\n{fibonacci}')
        print()
    except Exception as err:
        print(err)


# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja 
# maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre. 

# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência 
# ou pode ser previamente definida no código; 

def String_a():
    text = str(input("Digite um texto/frase para saber quantos 'A' tem: "))
    variant = ['a','á','à','ã','â','ä']

    def counting(text):
        cont = 0
        for letter in text.lower():
            if letter in variant:
                cont += 1
        return cont

    events = counting(text)
    print(f'Foram encontrados {events} letras a-A')
    print()


# 3) Observe o trecho de código abaixo: 
# int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } 
# imprimir(SOMA); 

# Ao final do processamento, qual será o valor da variável SOMA? 

def Codigo_K():
    indice = 12
    soma = 0
    k = 1

    while k < indice:
        k = k + 1
        soma = soma + k

    print(f'Valor final da variável SOMA: {soma}')
    # A resposta é 77.
    print()


"""
4) Descubra a lógica e complete o próximo elemento: 
a) 1, 3, 5, 7, ____
  Resposta é 9
  Aumentou de 2 em 2.

b) 2, 4, 8, 16, 32, 64, ____ 
  Resposta é 128
  Multiplicou 2 com o valor anterior.

c) 0, 1, 4, 9, 16, 25, 36, ____ 
  Resposta é 49    
  Aumentou apenas com valores impares apartir do 1.

d) 4, 16, 36, 64, ____ 
  Resposta é 100
  Aumenta de acordo com o quadrado dos números pares 2², 4², 6², 8², 10².

e) 1, 1, 2, 3, 5, 8, ____
  Resposta é 13
  Aumenta com a soma dos dois números anteriores, Sequencia de Fibonacci.

f) 2, 10, 12, 16, 17, 18, 19, ____
  Resposta é 200
  Todos os números começam com a letra "D". Dois, Dez, Dezesseis, ...,  Duzentos
"""

"""
5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes.
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores 
quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.
Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas,
qual interruptor controla cada lâmpada? 

Resposta: 
Eu ativaria um interruptor por 15 minutos e depois apagaria, após esse tempo ligaria outro
interruptor e iria em uma sala, caso a luz acessa, refere-se ao segundo interruptor, se 
apagada e quente, refere-se ao primeiro interruptor, se apagada e fria, refere-se ao terceiro.
Depois eu iria na segunda sala, e analisaria conforme anteriormente. Assim, caso a primeira sala
estive-se apagada e quente, a segudna sala apagada e fria, a terceira sala estaria ligada.
Logo, o primeiro interruptor seria da primeira sala, o terceiro interruptor da segunda sala
e o segundo interruptor seria da terceira sala.
"""


if __name__ == '__main__':
    Fibonacci()
    String_a()
    Codigo_K()
