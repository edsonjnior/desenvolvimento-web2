# Criar um algoritmo que leia um número que será o limite superior de um intervalo e o incremento (inc). Imprimir
# todos os números naturais no intervalo de zero até o limite superior. Suponha que o incremento é maior do que
# zero e o limite superior maior que o incremento

def valida_inc(inc):
    return inc > 0

def valida_limite(limite, incremento):
    return valida_inc(incremento) and limite > incremento

limite = int(input('Digite o limite superior do intervalo: '))
incremento = int(input('Digite o incremento: '))

if valida_limite(limite, incremento):
    for valor in range(0, limite + 1, incremento):
        print(valor)
elif not valida_inc(incremento):
    print("Incremento deve ser maior que zero")
else:
    print("Limite superior deve ser maior que o incremento")
