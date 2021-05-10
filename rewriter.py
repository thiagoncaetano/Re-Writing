import requests
import random
import time

url = 'http://www.mit.edu/~ecprice/wordlist.10000'

resposta = requests.get(url)
palavras = resposta.content.splitlines()
palavras = [palavra.decode('utf-8') for palavra in palavras]

random_words = random.sample(palavras, 10)

pontos = 0
tic = time.perf_counter()

for palavra in random_words:
  print(palavra)
  entrada = input()
  if entrada == palavra:
        pontos = pontos + 1

toc = time.perf_counter()

print('Quantidade de pontos:') 
print(pontos)

print('Tempo em segundos:') 
print(toc-tic)
