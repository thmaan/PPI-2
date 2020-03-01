#########
# Exercicios - Listas
# Faca sem usar loops
#########

# Como selecionar 'wed' pelo indice?
print(days_list[2])
# Como verificar o tipo de 'mon'?
type(days_list[0])
# Como separar 'wed' até 'fri'?
days = days_list[2:5]
# Quais as maneiras de selecionar 'fri' por indice?
days_list[-1]
days_list[4]
days_list[4:]
# Qual eh o tamanho dos dias e days_list?
len(days) 
#O tamanho days é 3
len(days_list)
#Tamanho days_list é 5
# Como inverter a ordem dos dias?
days_list[::-1]
# Como inserir a palavra 'zero' entre 'a' e 1 de list?
list.insert(1,'zero')
# Como limpar list?
list.clear()
list = []
list *= 0
del list[:]
# Como deletar list?
del list
# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
ultimo_elemento = list[-1]
list.pop()
del list[-1]