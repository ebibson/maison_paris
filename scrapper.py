import requests, bs4

req = requests.get('https://www.abritel.fr/search/keywords:paris-france?adultsCount=2&childrenCount=2&petIncluded=false')



print(req.text)

