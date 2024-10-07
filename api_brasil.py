import requests

cnpj = input("Digite um CNPJ ")

cnpj = cnpj.replace("/", "").replace("-", "")

url = f'https://brasilapi.com.br/api/cnpj/v1/{cnpj}'

response =  requests.get(url)
if response.status_code ==200:
  data = response.json()
  print(data['razao_social']  data['nome_fantasia'])
else:
  print(f"Erro {response.status_code}: Deu erro!!")  