'''Criar um progrma que manipelo os dados do database MySQL
- Cadastrar curso
- Buscar curso
- Alterar curso
- Deletar curso'''
from time import sleep
from ManipulandoDadosMySQL.database import *
from ManipulandoDadosMySQL.functions import *


#Programa principal
while True:
    resposta = menu(['Mostrar Cursos', 'Cadastrar Curso', 'Altualizar Curso', 'Excluir Curso', 'Sair do programa'])
    if resposta == 1:
        lerDados()
    elif resposta == 2:
        cadastro()
    elif resposta == 3:
        atualiza()
    elif resposta == 4:
        deleta()
    elif resposta == 5:
        print('\033[33mSaindo do programa...', end=' ')
        sleep(2)
        print('Até logo!\033[m')
        print(lin())
        break
    else:
        print('\033[31mERRO: Por favor, digite uma opção válida.\033[m')
    sleep(2)




