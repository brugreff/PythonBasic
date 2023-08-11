# Ex 4 - Threads em Py

# exemplo mais prático(mundo real)

import threading 
import urllib.request
import time

start = time.time()
urls = ["http://www.google.com", "http://www.Apple.com", "http://www.Microsoft.com", "http://www.instagram.com"]

# objetivo: fazer o request a cada uma dessas urls
# def função chama_url
def chama_url(url):
    req = urllib.request.Request(url) # verif. confiabilidade da url (resultado armazenado em req)
    response = urllib.request.urlopen(req) # acessa url
    the_page = response.read() # leitura da estrutura da página da url
    print ("%s\ carregado em %ss" % (url, (time.time() - start))) # printar url e o tempo que ela levou para ser carregada (dif do tempo inicial)

# criação da thread
threads = [threading.Thread(target=chama_url, args=(url,)) for url in urls]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print ("Elapsed Time: %s" % (time.time() - start))

