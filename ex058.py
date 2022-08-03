from random import randint
from time import sleep
n = 1
j = 0
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
pc = randint(0, 10) #comando para sortear número
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO ...')
sleep(1)

while j != pc:
    print('Errou, tente novamente!')
    print('~*~' * 8)
    j = int(input('Em que número eu pensei? '))
    print('PROCESSANDO ...')
    sleep(1)
    n += 1
    if j == pc:
        print(f'Parabens! Você tentou {n} vezes para me vencer!\nO número que eu estava pensando era {pc}!')
