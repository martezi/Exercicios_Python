e=str(input('Digite a expressão matemática: '))
if e.count('(') == e.count(')'):
    print('Sua expressão é valida!')
else:
    print('Sua expressão é invalida!')