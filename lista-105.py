#!/usr/bin/python3

# Importacao do modulo sys
import sys

'''
	DESAFIO!!!
	1) Crie uma lista com os 1000 primeiros numeros pares. Não use loop!
	2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999. Depois crie um loop para percorrer a lista ateh encontrar o primeiro multiplo de 5.
	OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

## Loops

i = 1

# While
while (i <= 10):
	print(i)
	i += 1

# Aborta o script
sys.exit(0)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Percorrendo uma lista
for x in list:
	print(x)

## Percorrendo um 'range'

# range(0, n-1)
for x in range(11):
	print(x)

# range(inicio, fim)
for x in range(1, 11):
	print(x)

# range(inicio, fim, passo)
for x in range(0, 11, 2):
	print(x)

##  list comprehension
# uma lista com o cubo dos elementos de 0 a 9
cubes = [i ** 3 for i in range(10)]

print('Cubes:')
for i in cubes:
	print(i)

# uma lista com o cubo dos elementos pares de 0 a 9
cubes = [i ** 3 for i in range(10) if i % 2 == 0]
# cubes = [i ** 3 for i in range(0, 10, 2)]

print('Cubos dos numeros pares:')
for i in cubes:
	print(i)

## Clausula ELSE !!!

# Suponha que voce queira iterar em uma lista de elementos até encontrar uma determinada condicao,
# apos isso, voce pode encerrar a execucao do loop usando o break.
# Caso nenhum elemento se encaixe na condicao voce precisa executar uma acao,
# por exemplo: gerar um log, enviar uma mensagem/email, etc.
# Esse problema pode resolvido com a utilizacao de uma flag boolena, por exemplo;
# porem, em python temos a opcao de usar a clausa else

# percorre uma lista e imprime se encontrou, ou nao, o elemento 6
for i in range(999):
	if i == 6:
		print('Elemento 6 encontrado na lista')
else:
	print('O elemento 6 NAO foi encontrado na lista')

# Encontra os fatores de um numero entre 2 e 10
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print( n, ' = ', x, '*', n/x)
			break
	else:
		# Se nao encontrou um fator
		print(n, 'eh numero primo')


###
# Exercicios
###

## Usando a lista: ['a','b','c']
# 1) Faca um loop para retornar: ['A','B','C']
list = ['a','b','c']
for i in list:
	print(i.upper())
## Usando os numeros: [0, 1, 3, 4, 5]
# 2) Faca um loop para retornar a soma de todos os elementos da listas
# 3) Faca um loop para retornar apenas os numeros impares
numeros = [0, 1, 3, 4, 5]
soma = 0
for i in numeros:
	soma += i
print(soma)
for i in numeros:
	if i % 2 == 1:
		print(i)
## usando a string: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string
string = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''
c = 0
for i in string.split():
    if(len(i)>= 5):
            c += 1
print(c)
# 5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100
multiplos3 = [i for i in range(100) if i % 3 == 0]
multiplos3 = [i for i in range(0, 100, 3)]

# Faca uma funcao para encontrar os numeros primos no intervalo [2, 10), mas nao utilize a clausula else do for

def isPrimo(num):
    contador = 0
    for i in range(1, num + 1):
        if num % i == 0:
            contador += 1                        
    if contador == 2:
        print(" O número é primo")
    else:
         print(" O número não é primo")
         
for i in range(2, 10):
    print(i, end='')
    isPrimo(i)