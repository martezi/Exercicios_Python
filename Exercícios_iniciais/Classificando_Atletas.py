ano=int(input('Qual seu ano de nascimento? '))
print('O atleta tem {} anos.'.format(2026-ano))
if 2026-ano>=26:
    print('Classificação: MASTER')
elif 2026-ano>=25:
    print('Classificação: SENIOR')
elif 2026-ano>=19:
    print('Classificação: JUNIOR')
elif 2026-ano>=14:
    print('Classificação: INFANTIL')
elif 2026-ano>=9:
    print('Classificação: MIRIM')



