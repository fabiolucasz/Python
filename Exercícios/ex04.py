salario = float(input('Digite seu salário: '))
porcentagem = float(input('Digite a % de aumento: '))

aumento = (salario * porcentagem / 100)

total = salario + aumento

print (f' Seu aumento foi de: R$ {aumento:.2f}')
print (f' Seu salário é: R$ {total:.2f}')
