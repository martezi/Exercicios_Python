tm = (
    'Athletico-PR',
    'Atlético-MG',
    'Bahia',
    'Botafogo',
    'Chapecoense',
    'Corinthians',
    'Coritiba',
    'Cruzeiro',
    'Flamengo',
    'Fluminense',
    'Grêmio',
    'Internacional',
    'Mirassol',
    'Palmeiras',
    'Red Bull Bragantino',
    'Remo',
    'Santos',
    'São Paulo',
    'Vasco',
    'Vitória'
)
print(f'''{'=-=' * 10}
Listas de times do Brasileirão: {tm}
{'=-=' * 10}
Os 5 primeiros são: {tm[0:5]}
{'=-=' * 10}
Os 4 últimos são: {tm[-4:]}
{'=-=' * 10}
Times em ordem alfabética: {sorted(tm)}
{'=-=' * 10}
O Chapecoense está na {tm.index('Chapecoense')+1}ª posição.''')

