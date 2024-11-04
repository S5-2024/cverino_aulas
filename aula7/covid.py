import requests
import webbrowser
import json

country = "bra"

url = f"https://disease.sh/v3/covid-19/countries/{country}"

response = requests.get(url)
dados = response.json()

if(response.status_code == 200):
  data = response.json()

  pais = data.get("country")
  casos = data.get("cases")
  deaths = data.get("deaths")
  hoje = data.get("todayCases")
  print(f"Covid no {pais}:  -casos: {casos}  - mortes: {deaths}  - Casos de hoje: {hoje} ")

#Abrir em página
  # with open('response.json','w') as json_file:
  #   json.dump(data,json_file,indent=4)

  #   webbrowser.open('response.json')
else:
  print(response.status_code)