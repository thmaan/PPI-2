###
## Exercicios
###
professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}

professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}

professor3 = dict(id=28, name='Jorge Armino', idade=37)
print(type(professor3))

professor3['state_origin'] = 'Rio Grande do Sul'
professor3['courses'] = ['Filosofia', 'Informática e Sociedade']



# 1) Implemente o metodo define_default_city de acordo com a docstring definida no inicio da funcao. Utilize a clausula else no loop implementado.
	''' Define a capital do estado de origem como city_origin para um professor existente no arquivo. Retorna True se a capital do estado de origem existe no arquivo capitais-BR.csv e False, caso contrario.

	Keyword arguments:
		state -- O estado de origem do professor
	'''
def define_default_city(state):
    with open('capitais-BR.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if row[0] == state:
                professor1['city_origin'] = row[1]
                return True
        else:
            return False
print(define_default_city(professor1['state_origin']))
print(professor1)

# 2) Remova do arquivo capitais-BR.csv todas capitais dos estados do sudeste e teste se sua funcao estah robusta o suficiente.
#Ao remover capitais do arquivo, retorna-se False, devido a clausula else no loop.

# 3) Faca uma funcao que le o arquivo lista-cpf.txt, retorne a quantidade de CPF unicos (sem repeticao) e os escreva em um arquivo lista-cpf-unicos.txt. Eh necessario descompactar o arquivo lista-cpf.txt.tar.gz primeiro.
unico = set()
with open('lista-cpf.txt') as entrada:
    with open('unique-cpf.txt', 'w+') as saida:
        for linha in entrada:
            if linha not in unico:
                saida.write(linha)
                unico.add(linha)