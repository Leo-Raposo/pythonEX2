n1 = int(input('Digite o primeiro Nº: '))
n2 = int(input('Digite o segundo Nº: '))
op = 0
while op != 5:
    print("""[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA""")
    op = int(input('Escolha uma opção: '))
    if op == 1:
        soma = n1 + n2
        print(f'Resultado: {n1} + {n2} = {soma}')
    elif op == 2:
        mult = n1 * n2
        print(f'RESULTADO: {n1} x {n2} = {mult}')
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior número é {maior}')
    elif op == 4:
        print('Informe os números nomavente!')
        n1 = int(input('Digite o primeiro Nº: '))
        n2 = int(input('Digite o segundo Nº: '))
    elif op == 5:
        print('Finalizado...')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')