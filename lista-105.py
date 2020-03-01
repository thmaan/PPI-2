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