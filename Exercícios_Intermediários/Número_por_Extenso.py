n2 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
      'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n=int(input('Digite um número entre 0 e 20: '))
    if n>21:
        print('Número inválido, tente novamente')
    elif n<=20:
        break
print(f'O número digitado foi {n2[n]}')
