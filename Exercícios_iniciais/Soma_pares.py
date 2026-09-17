soma=0
print('Vou somar todos os números que você digitar.\n'
      'Porém, eu não gosto de números impares, então não vou somar eles :D')
for c in range (1,7):
    n=int(input('Digite um número: '))
    if (n%2)==0:
        soma=n+soma
print('A soma apenas dos números pares é de {}'.format(soma))