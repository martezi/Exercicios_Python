s=0
while s!='F' and s!='M':
    s=str(input('Qual é o seu sexo [M/F]? ')).upper()
    if s=='M':
        print('Sexo Masculino registrado com sucesso!')
    elif s=='F':
        print('Sexo Feminino registrado com sucesso!')
    else:
        print('Comando invalido.\n'
              'Tente novamente!')