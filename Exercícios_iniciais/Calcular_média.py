print('A média necessária para passar de ano é 7.')
n1=float(input('Qual a primeira nota do aluno? '))
n2=float(input('Qual a segunda nota do aluno? '))
m=(n1+n2)/2
print('A média do Aluno é {}'.format(m))
if m>=7:
    print('Resultado: Aprovado')
elif m>=6.9:
    print('Resultado: Recuperação')
else:
    print('Resultado: Reprovado')