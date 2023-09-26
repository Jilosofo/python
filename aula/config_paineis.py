# TODO: usar um dict para cada matriz de telas porque além do IP elas tem as
# config padrao

# IP da primera tela/tv do painel 1
tela_inicial_1 = '10.10.10.126'
# IP da primera tela/tv do painel 2
tela_inicial_2 = '10.10.10.151'

# dimensões dos paineis
lins = 4
cols = 4

# display ID usado pelas telas/TVs
display_id = 0

# entradas disponíveis
entradas = [
    {'descricao': 'Plenário 1', 'nome': 'HDMI1'},
    {'descricao': 'Plenário 2', 'nome': 'HDMI2'},
    {'descricao': 'TV Câmara', 'nome': 'DVI'}
]

icone = './icone_camara_deputados.png'
painelweb_url_base = 'http://10.10.10.200:8080'
stream_url = 'http://FONTE_DO_STREAM'
