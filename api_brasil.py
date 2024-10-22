import requests

# Solicitando o CNPJ e DDD ao usuário
cnpj = "18.715.508/0001-31"
ddd = "31"

# Função para buscar informações do CNPJ
def buscacnpj(cnpj): 
    # Limpando caracteres especiais do CNPJ
    cnpj = cnpj.replace("/", "").replace("-", "").replace(".", "")
    url = f'https://brasilapi.com.br/api/cnpj/v1/{cnpj}'
    
    # Fazendo a requisição GET
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return print(data['razao_social'], " -- ", data['nome_fantasia'])
    else:
        return print(f"Erro {response.status_code}: Deu erro!!")  

# Chamando a função para buscar CNPJ
buscacnpj(cnpj)


# Função para buscar informações do DDD
def buscaddd(ddd):
    url = f'https://brasilapi.com.br/api/ddd/v1/{ddd}'
    
    # Fazendo a requisição GET
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return print(data['state'], " -- ", data['cities'])
    else:
        return print(f"Erro {response.status_code}: Deu erro!!")  

# Chamando a função para buscar DDD
buscaddd(ddd)
