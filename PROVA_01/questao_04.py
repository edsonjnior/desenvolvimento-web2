# Converter uma lista de números e transforma-la em uma lista de valores booleanos
# Para valores positivos adicionar True, caso contrário False

def criar_lista(qtde):
    lista = []
    for i in range(qtde):
        n = int(input("%d. Digite um número: " % (i + 1)))
        lista.append(n)
    return lista

def converte_lista_bool(lista):
    lista_b = []
    for valor in lista:
        lista_b.append(valor > 0)
    return lista_b

qtde = int(input("Quantos elementos deseja incluir? "))
lista = criar_lista(qtde)
lista_conv_bool = converte_lista_bool(lista)
print(lista_conv_bool)
