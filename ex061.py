print('Gerador de PA')
print('-=' * 10)
p1 = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
t = p1
cont = 1
while cont <= 10:
    print(f'{t} > ', end='')
    t += r
    cont += 1
print('FIM')