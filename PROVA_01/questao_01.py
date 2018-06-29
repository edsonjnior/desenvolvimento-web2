# dado um determinado ângulo, determinar em qual quadrante esse angulo se encontra

def valida_angulo(angulo):
    return angulo >= 0 and angulo <= 360

angulo = int(input('Qual o valor do angulo? '))
if(valida_angulo(angulo)):
    if angulo >= 0 and angulo <= 90:
        print("PRIMEIRO")
    elif angulo > 90 and angulo <= 180:
        print("SEGUNDO")
    elif angulo > 180 and angulo <= 270:
        print("TERCEIRO")
    elif angulo > 270 and angulo <= 360:
        print("QUARTO")
else:
    print("O valor do ângulo informado é inválido.")
