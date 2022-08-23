'''
Não esquecer de instalar o Mysql connector no projeto
pip install mysql-connector-python
'''
import mysql.connector

# Dados que nos permite acessar o database de dados / database com o database de dados
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database= 'api',
)

# Para conseguir rodar comando no SQL é necessário criar um cursos
# O cursor é quem vai executar os seus comando no database de dados
cursor = conexao.cursor()


#CRUD
#CREATE
def cadastrarDados(nomeCurso, valorCurso):
    comando = f'insert into cursos (nomeCurso, valorCurso) values ("{nomeCurso}", {valorCurso})'
    cursor.execute(comando)
    conexao.commit() # edita o database de dados
    cursor.close() # Encerrar o database
    conexao.close() # Encerrar a database


#READ
def lerDados():
    comando = f'select * from cursos'
    cursor.execute(comando)
    resultado = cursor.fetchall() # Ler o database de dados
    print(resultado)
    cursor.close() # Encerrar o database
    conexao.close() # Encerrar a database


#UPDATE
def atualizarDados(nomeCurso, valorCurso):
    comando = f'update cursos set valorCurso = {valorCurso} where nomeCurso = "{nomeCurso}"'
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados
    cursor.close() # Encerrar o banco
    conexao.close() # Encerrar a conexão



#DELETE
def deletarDados(nomeCurso):
    comando = f'delete from cursos where nomeCurso = "{nomeCurso}"'
    cursor.execute(comando)
    conexao.commit() # edita o database de dados
    cursor.close() # Encerrar o database
    conexao.close() # Encerrar a database

