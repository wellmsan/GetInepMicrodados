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

    for item in opcoes:
        menuArray.append(Menu(position + 1, item.getText(), item.data))

        print(item)
        
    print(menuArray)
