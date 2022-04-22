class ExtratorURL:
    def __init__(self,url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def sanitiza_url(self,url):
        if type(url) == str:
            return url.replace(' ','')
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')
    
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao] # (do início, até a posição x = '?')
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:] # da posição x = ('?'+1), até o final.
        return url_parametros

    def get_valor_parametro(self,parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca) #fazendo a busca dentro da url_parametros já filtrada.
        indice_valor= indice_parametro+len(parametro_busca)+1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor_url_parametros = self.get_url_parametros()[indice_valor:]
        else:
            valor_url_parametros = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor_url_parametros

extrator_url = ExtratorURL(None)
print(extrator_url.get_valor_parametro('Q'))
