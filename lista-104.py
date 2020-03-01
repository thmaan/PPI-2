###
# Exercicios
###

# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.
#
def isEqual(a,b):
	return a == b

list1 = [1,2,3]
list2 = [1,2,3]

print(isEqual(list1,list2))
# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.
#
# OBS.: Utilize apenas o que foi estudado ate agora

def isPalindrome(a,b):
	if a.lower().replace(" ","") == b.lower().replace(" ",""):
		return True
	else:
		return False	

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

print(isPalindrome(palindrome_one,palindrome_one[::-1]))