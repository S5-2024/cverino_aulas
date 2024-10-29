import sqlite3

con = sqlite3.connect('cadastro')
print("Conexao aberta!");


#Criando Aluno no SQLITE 
#con.execute('CREATE TABLE IF NOT  EXISTS alunos(matricula integer PRIMARY KEY AUTOINCREMENT, nome string, CPF integer );')

 
print("Tabela Criada com Sucesso!")

#con.execute('INSERT INTO  alunos(nome,CPF) VALUES ("Gabrielle", 15279181650); ') 

nome = input("Insira um nome: ")
CPF = input("Insira um cpf: ")

con.execute('INSERT INTO  alunos(nome,CPF) VALUES (?,?) ',(nome,CPF))
con.execute(' UPDATE alunos SET nome = ? WHERE matricula = ?', ('fdp',10))
consulta = con.execute('SELECT matricula,nome, CPF FROM alunos;')
linhas = consulta.fetchall()

print(linhas)
con.execute('Delete from alunos where matricula = 8   ')
con.commit()
