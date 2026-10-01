l=[]
for c in range (0,5):
    n=int(input('Digite um valor: '))
    if c==0 or n>l[-1]:
        l.append(n)
        print(f'''Adicionado ao final da lista.
        {'-'*15}''')
    else:
        p=0
        while p<len(l):
            if n<=l[p]:
                l.insert(p,n)
                print(f'''Valor adicionado na posição {p}
                {'-'*15}''')
                break
            p+=1
print(f'''{'='*30}
Os valores digitados em ordem foram: {l}''')