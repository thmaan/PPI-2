###
# Exercicios
###

# 1) Extraia o titulo do livro da string
# 2) Salve o titulo de cada livro em uma variável
# 3) Quantos caracteres cada título tem?
# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}

book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

titulo1, resto1 = book1.split(' by ')
titulo2, resto2 = book2.split(' by ')
titulo3, resto3 = book3.rsplit(' by ', 1) # O regex ' by ', iria separar o nome do livro tambem, por isso utilizei rsplit e o parametro 1, para separar em 2 elementos.
len(titulo1)
len(titulo2)
len(titulo3)
autor1, ano1 = resto1.split(", ")
autor2, ano2 = resto2.split(", ")
autor3, ano3 = resto3.split(", ")
msg1 = '{0} - {1}, {2}!'.format(titulo1, autor1, ano1)
msg2 = '{0} - {1}, {2}!'.format(titulo2, autor2, ano2)
msg3 = '{0} - {1}, {2}!'.format(titulo3, autor3, ano3)

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

palindrome_one == palindrome_one[::-1]
palindrome_two.lower() == palindrome_two[::-1].lower()
palindrome_three.replace(" ","") == palindrome_three[::-1].replace(" ","")
palindrome_four.replace(" ","") == palindrome_four[::-1].replace(" ","")