import sqlite3
import requests 
from datetime import datetime

def conexao(): 
  url = f"https://api.hgbrasil.com/finance?key=b6ce9a45"
  response = request.get(url)
  dados = response.json()

  dolar = dados['results']['currencies']['USD']['buy']
  euro = dados['results']['currencies']['EUR']['buy']
  return dolar, euro 
  


def criar_banco():
  conexao = sqlite3.connect('bdcotacoes')
  con = conexao.cursor()
  con.execute('''CREATE TABLE IF NOT EXISTS moedas( 
      Data TEXT,
      Dolar REAL,
      Euro REAL)'''
      )
  #Fechar a conexão
  con.commit()
  con.close()

# função para inserir dados na tabela "moedas"
 
   
 

def inserir_dados(dolar,euro):
  #Conectar ao banco de dados
  conexao = sqlite3.connect('bdcotacoes.db')
  cursor = conexao.cursor()

  # Obter a data atual
  data_atual = datetime.now().strtime("%Y-%n-%d %H:%M:%S")

  #Inserir dados 




