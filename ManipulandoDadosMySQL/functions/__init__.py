from ManipulandoDadosMySQL.database import *


def leiaInt(msg):
    '''
    -> Valida se o valor digitado pelo usuario é um número inteiro
    :param msg: Mensagem de solicitação de parâmetro
    :return: retorna o número inteiro digitado pelo usuário
    '''
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite uma opção válida.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[33mO usuário preferio sair sem digitar um valor.\033[m')
            break
        else:
            return n


def leiaFloat(msg):
    '''
    -> Valida se o valor digitado pelo usuario é um número real
    :param msg: Mensagem de solicitação de parâmetro
    :return: retorna o número real digitado pelo usuário
    '''
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[33mO usuário preferio sair sem digitar um valor.\033[m')
            break
        else:
            return n


def lin(tam=42):
    '''
    -> Cria linha do tamanho o parâmetro recebido
    :param tam: comprimento da linha
    :return: a linha no tamnho do paâmetro
    '''
    return '-' * tam


def cabeçalho(msg):
    '''
    -> Recebe uma mensagem e cria um cabeçalho formatado
    :param msg: mensagem recebida
    :return: retorna um cabeça~ho formatado
    '''
    print(lin())
    print(msg.center(42))
    print(lin())


def menu(lista):
    '''
    -> Cria um menu apartir de uma lista recebida
    e recebe a opção digitada.
    Após validar, retorna para o sistema.
    :param lista: lista contendo as opções do menu.
    :return: a opção do menu.
    '''
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(lin())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc


def cadastro():
    nome = str(input('Digite o Nome do Curso: ')).capitalize()
    valor = float(input('Digite o valor do curso: R$'))
    cadastrarDados(nome, valor)

def atualiza():
    print('Digite o nome do curso que você quer alterar o valor.')
    nome = str(input('Nome do Curso: '))
    valor = float(input('Novo valor: R$'))
    atualizarDados(nome, valor)


def deleta():
    print('Digite o Nome do Curso que deseja excluir')
    nome = str(input('Nome do Curso: '))
    deletarDados(nome)


