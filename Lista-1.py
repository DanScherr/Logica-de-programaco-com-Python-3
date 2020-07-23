# Lista 1  //  1st List

# Dados dois números, imprima o maior
# Given two numbers, print the biggest
def maior_de_dois(a,b):
    iguais = (a==b)
    maior = (a>b)

    if (iguais):
        return "Os números digitados são iguais."
    elif (maior):
        return a
    else:
        return b

#Dados dois números, checar se são diferentes. Se forem, imprimir qual o número maior e qual o número menor.
#Given 2 numbers, check if they are diferent. If they are, print the biggest and the lowest.
def checarDiferenca_maior_menor(a,b):
    diferentes = (a!=b)
    maior = (a>b)
    if (diferentes):
        if (maior):
            return "{0} é maior que {1}" .format(a,b)
        else:
            return "{1} é maior que {0}" .format(a,b)
    else:
        return "Os números digitados são iguais."

#Imprimir todos os números inteiros de 1 a 10
#Print the integer number from 1 to 10
def contagem10():
    for i in range(1,10+1):
        print (i)

#Dada uma lista, somar os números
#Given a lista, sum the numbers
def somaLista():
    N = 0
    soma = 0

    while True:
        N = int(input("Insira um número para somar ou 0 para sair: "))
        soma += N
        sair = (N == 0)
        if (sair):
            return soma
            break

#Dada uma razao de PA e dois números limites, imprimir todos os numeros da PA entre os limites
#Print a arithmetic progression
def progressaoAritmetica(a,b,r):
    maior = (a > b)
    menor = (a < b)
    if maior:
        for i in range (b, a, r):
            print (i)
    elif menor:
        for i in range (a, b, r):
            print (i)
    else:
        print ("Os números digitados são iguais.")

#Dividir um número dado por 2 até que o mesmo seja maior que 0
#Divide a number by 2 until it's bigger then 0
def dividePor2(quociente):
    contador = 0

    while quociente>0:
        quociente = quociente/2
        contador += 1
    return contador

#Dada um lista de números fornecidos pelo usuário, imprimir a média aritmética entre os números
#Given a list of number, print de arithmetic avarege
def mediaAritmetica():
    soma = 0
    contador = 0
    while True:
        N=float(input("Digite um número para se tirar a média aritmética ou 99.99 para sair: "))
        if N == 99.99:
            break
        else:
            contador +=1
            soma += N

    return (soma/contador)

#Dado um número, imprima o maior número quadrado menor que o número dado
#Given an integer number, print the biggest square root number smaller then the given number
def maiorQuadrado(N):
    quadrado = 0
    for i in range (1, N+1):
        quadrado = (i*i) + i
        if quadrado >= N:
            return i * i
            break