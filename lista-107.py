###
# Exercicio
###

# 1) Imprima os metodos disponiveis para uma lista e para uma tupla.
print(dir(list))
print(dir(tuple))
# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos
lista = dir(list)
tupla = dir(tuple)

def diff(list1,list2):
    print('Unique methods from list 1: ', set(list1) - set(list2))
    print('Unique methods from list 2: ', set(list2) - set(list1))

diff(lista,tupla)

# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3. Copie os dicts do arquivo 106.py
professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}
professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}
professor3 = dict(id=28, name='Jorge Armino', idade=37)
print(type(professor3))
professor3['state_origin'] = 'Rio Grande do Sul'
professor3['courses'] = ['Filosofia', 'Informática e Sociedade']

professor1['coordenadas'] = 100,200
professor2['coordenadas'] = (-4848,6)
professor3['coordenadas'] = (0,55)