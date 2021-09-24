p = float(input('Preço: R$'))
d = float(input('Desconto(%):'))

resto = (p * d / 100)
total = (p - resto)

print (f'Valor do desconto: R${resto:.2f}')
print (f'Total: R${total:.2f}')
