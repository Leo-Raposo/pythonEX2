total = totmil = menor = cont = 0
barato = ''
while True:
    prod = str(input('Nome do Produto: ')).strip()
    preco = int(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = prod
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S / N]')).upper().strip()[0]
    if c == 'N':
        break
print('{:-^40}'.format('> FIM DO PROGRAMA <'))

print(f'O total da compra foi R${total:5.2f}')
print(f'Temos {totmil} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
