l=[]
while True:
    n = int(input('Digite um valor: '))
    if n in l:
        print('Valor duplicado, não irei adicionar à lista.')
    else:
        l.append(n)
    c = str(input('Quer continuar? [S/N]: ')).upper()
    if c == 'N':
        break
l.sort()
print(f'''{'='*20}
Os valores digitados foram: {l}''')