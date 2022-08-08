from random import randint
v = 0
while True:
    n = int(input('Digite um Valor: '))
    pc = randint(0, 11)
    total = n + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P / I]: ')).upper().strip()[0]
    print(f'Você jogou {n} e o PC jogou {pc}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 1 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos Jogar Novamente ...')
print(f'GAME OVER! Você venceu {v} vezes.')

