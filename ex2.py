# Crie uma tupla preenchida com 20 primeiros colocados da tabela do campeonato brasileiro de futebol, ordem de colocação.
# Depois mostre:

# A- Apenas os 5 primeiros colocados.
# B- Os últimos 4 colocados da tabela.
# C- Uma lista com os times em ordem alfabetica.
# D- Em que posição na tabela está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 útimos colocados são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª')
print('-=' * 15)
print(f'O total de times no Brasileirão são: {len(times)}')

