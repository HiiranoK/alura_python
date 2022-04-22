#url = "bytebank.com/cambio?mO=real&mD=doll&Q=100"
url = " bytebank.com/cambio?mO=real&mD=doll&Q=100"
#mO = moeda Origem | mD = moeda Destino, Q = quantidade.

#sanitização da URL
url = url.replace(' ','')

#validação da URL
if url == '':
    raise ValueError("A URL está vazia")

#separa a url
indice_interrogacao = url.find('?')
url_base = url[:url.find('?')] # (do início, até a posição x = '?')
url_parametros = url[url.find('?')+1:] # da posição x = ('?'+1), até o final.

#busca o valor de um parametro
parametro_busca = 'mO'
indice_parametro = url_parametros.find(parametro_busca) #fazendo a busca dentro da url_parametros já filtrada.
indice_valor= indice_parametro+len(parametro_busca)+1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor_url_parametros = url_parametros[indice_valor:]
else:
    valor_url_parametros = url_parametros[indice_valor:indice_e_comercial]

print(valor_url_parametros)
