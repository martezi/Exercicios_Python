l=[]
p=[]
i=[]
while True:
    v=int(input('Digite um valor: '))
    if v % 2 == 0:
        p.append(v)
    else:
        i.append(v)
    l.append(v)
    c=str(input('Quer continuar? [S/N] ')).strip().upper()
    if c=='N':
        break
print(f'''{'=-'*20}
A lista completa é: {l}
Os números pares são: {p}
Os números ímpares são: {i}''')
