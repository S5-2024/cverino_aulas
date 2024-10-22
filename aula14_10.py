import requests
import webbrowser
import json

ip = '189.23.122.5'
key =  'b6ce9a45'

def pegando_ip(ips, keys):

  url = f'https://api.hgbrasil.com/geoip?fields=only_results,city,region,country_name,continent,code,capital&key={key}&address={ip}'

  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()
   
    with open('response.json','w') as json_file:
      json.dump(data,json_file,indent=4)

      webbrowser.open('response.json')
  else:
    print(response.status_code)
  

#pegando_ip(ip,key)


moeda = 'BRL'
def cotacao(moeda,key):
  url = f'https://api.hgbrasil.com/finance?key={key}'
  response =  requests.get(url)

  if response.status_code == 200:
    data = response.json()
    if moeda in data['results']['currencies']:
      valor = data['results'][currencies][moeda]['buy']
    with open('response.json','w') as json_file:
      json.dump(data,json_file,indent=4)
      webbrowser.open('response.json')   
  else:
      print(response.status_code)     

cotacao(moeda,key)