#perguntar valor da hora e numero de horas trabalhadas

hora = float(input('Valor da hora: R$'))
tempo = int(input('Quantidade de horas trabalhadas: '))

salario_bruto = (hora*tempo)
print (f'Salário bruto: R${salario_bruto}')

#irrf
if salario_bruto < 1903.98:
    irrf = (salario_bruto * 0)
    salario_bruto_irrf = salario_bruto - irrf
    print (f'-IRRF: R${irrf:.2f}')
    print (f'Você está isento!')

elif salario_bruto >= 1903.99 and salario_bruto <=  2826.65:
        irrf = (salario_bruto * 0.075)
        salario_bruto_irrf = salario_bruto - irrf
        print (f'-IRRF: R${irrf:.2f}')
        

elif salario_bruto >= 2826.66 and salario_bruto <=  3751.05:
        irrf = (salario_bruto * 0.15)
        salario_bruto_irrf = salario_bruto - irrf
        print (f'-IRRF: R${irrf:.2f}')
        

elif salario_bruto >= 3751.06 and salario_bruto <=  4664.68:
        irrf = (salario_bruto * 0.225)
        salario_bruto_irrf = salario_bruto - irrf
        print (f'-IRRF: R${irrf:.2f}')
        


#inss

if salario_bruto <= 1100:
        inss = (salario_bruto * 0.075)
        salario_bruto_inss = salario_bruto - inss
        print (f'-INSS: R${inss:.2f}')

elif salario_bruto >= 1100.01 and salario_bruto <=  2203.48:
        inss = (salario_bruto * 0.09)
        salario_bruto_inss = salario_bruto - inss
        print (f'-INSS: R${inss:.2f}')

elif salario_bruto >= 2203.49 and salario_bruto <= 3305.22:
        inss = (salario_bruto * 0.12)
        salario_bruto_inss = salario_bruto - inss
        print (f'-INSS: R${inss:.2f}')

elif salario_bruto >= 3305.23 and salario_bruto <= 6433.57:
        inss = (salario_bruto * 0.14)
        salario_bruto_inss = salario_bruto - inss
        print (f'-INSS: R${inss:.2f}')

sindicato = (salario_bruto * 0.05)
salario_bruto - sindicato

print (f'Sindicato: R${sindicato}')
    
salario_liquido = salario_bruto - irrf - inss - sindicato
print (f'Total de descontos: R${irrf + inss + sindicato}')
print (f'Seu salário líquido é: R${salario_liquido}')