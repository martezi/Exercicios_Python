n=(int(input('Digite um número: ')),int(input('Digite outro número: ')),
   int(input('Digite mais um número: ')),int(input('Último número: ')))
print(f'''Você digitou: {n}
O valor 9 apareceu {n.count(9)} vezes
O valor 3 apareceu na {n.index(3)}ª posição
Os valores pares digitados foram {sum(1 for x in n if x %2==0)}''')
