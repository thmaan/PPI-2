lista = dir(list)
tupla = dir(tuple)

def diff(list1,list2):
    print('Unique methods from list 1: ', set(list1) - set(list2))
    print('Unique methods from list 2: ', set(list2) - set(list1))

diff(lista,tupla)
