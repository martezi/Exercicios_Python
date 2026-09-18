f=str(input('Digite uma frase: ')).strip().upper()
l=f.split()
j=''.join(l)
i=''
for c in range  (len(j)-1,-1,-1):
    i+=j[c]
print('O inverso de {} é {}.'.format(j,i))
if i==j:
    print('É um Palíndromo')
else:
    print('Não é um Palíndromo')