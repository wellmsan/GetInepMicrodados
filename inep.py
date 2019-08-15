from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

from models import Menu

try:
    html = urlopen("http://inep.gov.br/microdados")
except HTTPError as e:
    print(e)
except URLError:
    print("Servidor INEP fora ou caiu")
else:
    res = BeautifulSoup(html.read(), "html5lib")
    opcoes = res.find_all("a", {"class": "anchor"})
    print("######## OPÇÕES DE DOWNLOAD '" + res.title.getText() + "' ########") 
    menuArray = []
    position = 0
    for x in opcoes:
        position = position + 1
        menuArray.append(Menu(position, x.getText(), x["data-anchor"]))
    for menu in menuArray:
        print(menu)
    opcao = input("Escolha uma opção [1-{0}]: ".format(len(menuArray)))
    for item in menuArray:
        if item._position == int(opcao):
            divDownloads = res.find_all("div", {"data-anchor": item._dataAnchor})
            print(divDownloads[0])
            #for download in divDownloads[0].a:
                #print(download)
    
