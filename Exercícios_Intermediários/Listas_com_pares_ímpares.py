l=[]
l2=[]
r=[]
for c in range (0,7):
    c+=1
    v=int(input(f'Digite o {c}º valor: '))
    if v%2==0:
        l.append(v)
    else:
        l2.append(v)
l.sort()
l2.sort()
r.append(l[:])
r.append(l2[:])
print(f'''{'=-'*30}
A lista de pares é: {r[0]}
A lista de impares é {r[1]}
{'-'*20}
E a lista completa é {r}
Duas listas dentro de uma lista, organizadas em ordem crescente''')

