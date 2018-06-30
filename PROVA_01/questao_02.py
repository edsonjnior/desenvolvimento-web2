# dado um número inteiro qualquer, mostre quantos digitos esse número possui
# exemplo: 1.323, mostrar o número 4

num = int(input("Digite um número inteiro: "))

cont = 0
div = 1
while num // div > 0:
    cont += 1
    div *= 10

print("O número %d possuí %d caracteres." % (num, cont))
