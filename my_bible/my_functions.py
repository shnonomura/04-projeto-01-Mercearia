def objetivo(texto):
    t =texto.upper()
    print('{:=^111}'.format(t))

def definicao(texto):
    t = 'DEFINICAO: ' + texto
    print('{:<102}'.format(t))

def descricao(texto):
    t = 'Descricao: ' + texto
    print('{:<102}'.format(t))

def secao(texto):
    print('\nSECAO' + '{:-^106}'.format(texto))

def comentario(texto):
    print('Comentario: ' + '{:<102}'. format(texto))

def observacao(texto):
    print('Obs.: '+'{:<106}'. format(texto))

