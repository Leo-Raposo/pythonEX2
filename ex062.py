print('Gerador de PA')
print('-=' * 10)
p1 = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
t = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{t} > ', end='')
        t += r
        cont += 1
    print('PAUSA')
    mais = int(input('QUantos termos você quer mostrar a mais? '))
print(f'Progreção finalizada com {total} termos')
