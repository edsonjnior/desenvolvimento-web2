# Crie um programa que, usando dicionário, crie uma agenda de tamanho fornecido inicialmente pelo
# usuário. Leia os dados de todos os contatos do usuário de forma que a agenda fique completa e por fim
# imprima todos os contatos

def obter_dicionario(qtde):
    dic = {}
    for i in range(qtde):
        nome = input("Digite o nome do contanto %d" % (i + 1))
        telefone = input("Digite o número de telefone de %s" % nome)

        dic[nome] = telefone

    return dic

qtde = int(input("Quantas pessoas deseja adicionar na agenda? "))
agenda = obter_dicionario(qtde)

print(agenda)
