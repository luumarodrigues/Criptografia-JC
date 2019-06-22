
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# definindo API 
API_TOKEN = 'TOKEN'

# definindo endereço 
API_URL = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=TOKEN'

#importando biblioteca
import requests
import json as JSON
from ast import literal_eval

#get request
response = requests.get(API_URL)

#resultado do Get request
resultado_json = (response.content)

#substitui aspas simples por aspas duplas
json = resultado_json.decode('utf8').replace("'", '"')

#cria e escreve conteudo no arquivo json
arquivo = open ('C:\\Users\\luma.de.f.rodrigues\\python\\answer.json', 'w')
arquivo.write(str(json))

#converte str em obj python
objeto = JSON.loads(json)

#pega dados específicos do json
cifrado = (objeto['cifrado'])
casas = (objeto['numero_casas'])

#declara a variavel da mensagem
mensagem = (cifrado)

#declara a variavel do numero de casas
key = int(casas)

# Conjunto de caracteres válidos no algoritmo
Alfabeto = 'abcdefghijklmnopqrstuvwxyz'

# Converter todo o texto em minusculo:
mensagem = mensagem.lower()

# Variável para armazenar o texto criptografado
decifrado = ''

# Código que será executado em cada caractere do texto:
for caracter in mensagem:
    if caracter not in '!@#$%.,;123456789 ':
      posicao = Alfabeto.find(caracter)
      novaposicao = (posicao - key) % 26
      novocaracter = Alfabeto[novaposicao]
      decifrado += novocaracter
    else:
      decifrado += (caracter)

else:
    print('Nova mensagem criptografada:', decifrado)

#alterando valor de decifrado
objeto['decifrado']= decifrado

#atualiza o json
arquivo = open ('C:\\Users\\luma.de.f.rodrigues\\python\\answer.json', 'w')
arquivo.write(str(objeto))

#SHA1
import hashlib
hash_object = hashlib.sha1()
hash_object.update(decifrado.encode('utf8')) 
print('Resumo Criptográfico:', hash_object.hexdigest())

#alterando valor de resumo_criptografico
objeto['resumo_criptografico'] = hash_object.hexdigest()

#atualiza o json
arquivo = open ('C:\\Users\\luma.de.f.rodrigues\\python\\answer.json', 'w')
arquivo.write(str(objeto))

#Converte obj python em str e atualiza o json final
json_final = JSON.dumps(objeto)
arquivo = open ('C:\\Users\\luma.de.f.rodrigues\\python\\answer.json', 'w')
arquivo.write(str(json_final))

#post request

answer = {'answer': open('C:\\Users\\luma.de.f.rodrigues\\python\\answer.json', 'rb')}
url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=TOKEN'
response = requests.post(url = url, files = answer)
print (response.text)
print (response.status_code)