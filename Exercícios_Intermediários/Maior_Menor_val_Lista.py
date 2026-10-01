n=[]
for c in range(0,5):
    n+=[(int(input(f'Digite um Valor na posição {c}: ')))]
print(f'''{'='*20}
Você digitou os valores {n}
O maior valor digitado foi o {max(n)}, e ele está na posição: {n.index(max(n))}
O menor valor digitado foi o {min(n)}, e ele está na posição: {n.index(min(n))}''')