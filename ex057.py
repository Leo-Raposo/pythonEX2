r = 1
s1 = 'M'
s2 = 'F'
while r != 'M' and r != 'F':
    r = str(input('Digite o seu sexo [M/F]: ')).upper()
    if r != 'M' and r != 'F':
        print('Comando inválido!')
print('Fim')
