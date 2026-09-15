ps=float(input('Primeiro segmento: '))
ss=float(input('Segundo segmento: '))
ts=float(input('Terceiro segmento: '))
if ps<ss+ts and ss<ps+ts and ts<ps+ss:
    print('Pode formar um triangulo')
    if ps==ss==ts:
        print('Todos os lados são iguais.\n'
              'Portanto, tem um triangulo Equilátero.')
    elif ps!=ss!=ts!=ps:
        print('Todos os lados são diferentes.\n'
              'Portanto, tem um triangulo Escaleno.')
    else:
        print('Um lado é igual e dois são diferentes.\n'
              'Portanto, tem um triangulo Isósceles.')
else:
    print('Não pode formar um triangulo.')