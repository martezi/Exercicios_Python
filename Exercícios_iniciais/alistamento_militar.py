a=int(input('Ano de nascimento: '))
alm=a+18
print('Você nasceu em {} e tem {} anos.'.format(a, 2026-a))
if 2026<alm:
    print('Você terá que se alistar no ano {}'.format(alm))
elif 2026>alm:
    print('Já passou do prazo do seu alistamento, você precisava ter ser alistado\n'
          'no ano {}'.format(alm))
elif 2026==alm:
    print('Você está na idade de se alistar!')