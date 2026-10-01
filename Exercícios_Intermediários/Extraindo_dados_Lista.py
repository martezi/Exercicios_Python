l=[]
v=0
while True:
    n=int(input('Digite um valor: '))
    l.append(n)
    v+=1
    c=str(input('Quer continuar? [S/N] ')).strip().upper()
    if c=='N':
        break
l.sort(reverse=True)
print(f'''{'=-'*20}
Você digitou {v} valores.
OS valores digitados em ordem decrescente são: {l}.''')
if 5 in l:
    print('O valor 5 foi digitado na lista.')
else:
    print('O valor 5 não foi digitado na lista.')
