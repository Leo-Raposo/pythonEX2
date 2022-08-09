from time import sleep
count = count2 = count3 = 0
while True:
    idade = int(input('Digite seu nome: '))
    sexo = str(input('Digite seu sexo [M / F]: ')).strip().upper()[0]
    if idade >= 19:
        count += 1
    if sexo == 'M':
        count2 += 1
    elif sexo == 'F' and idade <= 20:
        count3 += 1
    p = ' '
    while p not in 'SN':
        p = str(input('Deseja inserir novos dados? [S / N]: ')).strip().upper()[0]
    print('Processando...')
    sleep(1)
    if p == 'N':
        print('Programa encerrado!')
        break
print(f'{count} Pessoas tem mais de 18 anos!\n'
      f'{count2} Homens foram cadastrados\n'
      f'{count3} Mulheres tem menos de 20 anos!')
