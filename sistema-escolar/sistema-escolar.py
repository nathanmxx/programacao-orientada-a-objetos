from os import environ
from prettytable import PrettyTable
import mysql.connector

CURSOS = ['INFORMATICA', 'ELETRONICA', 'PUBLICIDADE',
          'ANALISE CLINICA', 'ADMINISTRACAO', 'QUIMICA']

def abrebanco():
    try:
        global conexao
        conexao = mysql.connector.Connect(host=environ.get('DB_HOST', 'localhost'),
                                          database=environ.get('DB_NAME', 'escola'),
                                          user=environ.get('DB_USER', 'root'),
                                          password=environ.get('DB_PASSWORD', ''))

        if conexao.is_connected():
            global comandosql
            comandosql = conexao.cursor()
            print('Conexao com o banco de dados realizada com sucesso!')
            return 1
        else:
            print('Nao foi possivel conectar ao banco de dados.')
            return 0

    except Exception as erro:
        print(f'Erro na conexao: {erro}')
        return 0

def cursovalido(curso=''):
    if curso in CURSOS:
        return True
    else:
        return False

def nomevalido(nome=''):
    if nome.strip() == '':
        return False
    else:
        return True

def lernumero(mensagem=''):
    while True:
        valor = input(mensagem)
        if valor.isnumeric():
            return int(valor)
        print('ERRO! Digite apenas numeros.')

def mostratodasturmas():
    grid = PrettyTable(['ID DA TURMA', 'CURSO'])
    try:
        comandosql = conexao.cursor()
        comandosql.execute('select * from turmas order by id_turma;')
        tabela = comandosql.fetchall()

        if comandosql.rowcount > 0:
            for registro in tabela:
                grid.add_row([registro[0], registro[1]])
            print(grid)
        else:
            print('Nao existem turmas cadastradas!!!')

    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')

def consultarturma(idt=0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from turmas where id_turma = {idt};')
        tabela = comandosql.fetchall()

        if comandosql.rowcount > 0:
            for registro in tabela:
                print(f'Turma {registro[0]} - Curso: {registro[1]}')
            return 'c'
        else:
            return 'nc'

    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')
        return 'nc'

def cadastrarturma(idt=0, curso=''):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'insert into turmas (id_turma, curso) '
                           f'values ({idt}, "{curso}");')
        conexao.commit()
        return 'Turma cadastrada com sucesso!!!'

    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Nao foi possivel cadastrar esta turma!!!'

def turmatemalunos(idt=0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from alunos where id_turma = {idt};')
        comandosql.fetchall()

        if comandosql.rowcount > 0:
            return True
        else:
            return False

    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')
        return True

def alterarturma(idt=0, curso=''):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'update turmas set curso = "{curso}" '
                           f'where id_turma = {idt};')
        conexao.commit()
        return 'Turma alterada com sucesso!!!'

    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Nao foi possivel alterar esta turma!!!'

def excluirturma(idt=0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'delete from turmas where id_turma = {idt};')
        conexao.commit()
        return 'Turma excluida com sucesso!!!'

    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Nao foi possivel excluir esta turma!!!'

def mostratodosalunos():
    grid = PrettyTable(['MATRICULA', 'NOME', 'TURMA', 'CURSO'])
    try:
        comandosql = conexao.cursor()
        comandosql.execute('select alunos.matricula, alunos.nome, '
                           'alunos.id_turma, turmas.curso '
                           'from alunos, turmas '
                           'where alunos.id_turma = turmas.id_turma '
                           'order by alunos.matricula;')
        tabela = comandosql.fetchall()

        if comandosql.rowcount > 0:
            for registro in tabela:
                grid.add_row([registro[0], registro[1],
                              registro[2], registro[3]])
            print(grid)
        else:
            print('Nao existem alunos cadastrados!!!')

    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')

def consultaraluno(mat=0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from alunos where matricula = {mat};')
        tabela = comandosql.fetchall()

        if comandosql.rowcount > 0:
            for registro in tabela:
                print(f'Matricula: {registro[0]} - Nome: {registro[1]} '
                      f'- Turma: {registro[2]}')
            return 'c'
        else:
            return 'nc'

    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')
        return 'nc'

def cadastraraluno(mat=0, nome='', idt=0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'insert into alunos (matricula, nome, id_turma) '
                           f'values ({mat}, "{nome}", {idt});')
        conexao.commit()
        return 'Aluno cadastrado com sucesso!!!'

    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Nao foi possivel cadastrar este aluno!!!'

def alteraraluno(mat=0, nome='', idt=0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'update alunos set nome = "{nome}", '
                           f'id_turma = {idt} where matricula = {mat};')
        conexao.commit()
        return 'Aluno alterado com sucesso!!!'

    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Nao foi possivel alterar este aluno!!!'

def excluiraluno(mat=0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'delete from alunos where matricula = {mat};')
        conexao.commit()
        return 'Aluno excluido com sucesso!!!'

    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Nao foi possivel excluir este aluno!!!'

def turmadoaluno(mat=0):
    grid = PrettyTable(['MATRICULA', 'NOME DO ALUNO', 'TURMA', 'CURSO'])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select alunos.matricula, alunos.nome, '
                           f'turmas.id_turma, turmas.curso '
                           f'from alunos, turmas '
                           f'where alunos.id_turma = turmas.id_turma '
                           f'and alunos.matricula = {mat};')
        tabela = comandosql.fetchall()

        if comandosql.rowcount > 0:
            for registro in tabela:
                grid.add_row([registro[0], registro[1],
                              registro[2], registro[3]])
            print(grid)
        else:
            print('ALUNO NAO ENCONTRADO!!!')

    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')

def alunosdaturma(idt=0):
    grid = PrettyTable(['MATRICULA', 'NOME DO ALUNO'])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select matricula, nome from alunos '
                           f'where id_turma = {idt} order by nome;')
        tabela = comandosql.fetchall()

        if comandosql.rowcount > 0:
            for registro in tabela:
                grid.add_row([registro[0], registro[1]])
            print(grid)
        else:
            print('NAO EXISTEM ALUNOS NESTA TURMA!!!')

    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')

def menuturmas():
    while True:
        print('=' * 60)
        print('{:^60}'.format('SISTEMA ESCOLAR - MODULO DE TURMAS'))
        print('=' * 60)

        idturma = lernumero('ID da Turma (0 - Mostra todas): ')

        if idturma == 0:
            mostratodasturmas()
            continue

        if consultarturma(idturma) == 'nc':
            print('Esta turma nao esta cadastrada. Vamos cadastra-la!')
            print(f'Cursos permitidos: {CURSOS}')
            curso = input('Curso da turma: ').upper()

            if cursovalido(curso):
                print(cadastrarturma(idturma, curso))
            else:
                print('CURSO INVALIDO! Nao foi possivel cadastrar a turma.')

        else:
            op = input('Escolha: [A]-Alterar [E]-Excluir '
                       '[L]-Listar alunos [C]-Cancelar ==> ').upper()
            while op != 'A' and op != 'E' and op != 'L' and op != 'C':
                op = input('ERRO!!! Escolha CORRETAMENTE: [A] [E] [L] [C] ==> ').upper()

            if op == 'A':
                if turmatemalunos(idturma):
                    print('NAO PERMITIDA ACAO - ALUNOS VINCULADOS A ESTA TURMA')
                else:
                    print('Atencao: o ID da turma nao pode ser alterado.')
                    print(f'Cursos permitidos: {CURSOS}')
                    curso = input('Novo curso da turma: ').upper()
                    if cursovalido(curso):
                        print(alterarturma(idturma, curso))
                    else:
                        print('CURSO INVALIDO! Nao foi possivel alterar a turma.')

            elif op == 'E':
                if turmatemalunos(idturma):
                    print('NAO PERMITIDA ACAO - ALUNOS VINCULADOS A ESTA TURMA')
                else:
                    confirma = input('ATENCAO!!! CONFIRMA EXCLUSAO? '
                                     'S-SIM ou N-NAO: ')
                    while confirma != 'S' and confirma != 'N':
                        confirma = input('RESPOSTA INEXISTENTE!!! '
                                         'CONFIRMA EXCLUSAO? S-SIM ou N-NAO: ')
                    if confirma == 'S':
                        print(excluirturma(idturma))
                    else:
                        print('Exclusao cancelada pelo usuario.')

            elif op == 'L':
                alunosdaturma(idturma)

            else:
                print('Operacao cancelada pelo usuario.')

        print('\n')
        print('=' * 60)
        if input('Continuar no modulo de TURMAS? '
                 '1-Sim ou qualquer tecla para voltar: ') == '1':
            continue
        else:
            break

def menualunos():
    while True:
        print('=' * 60)
        print('{:^60}'.format('SISTEMA ESCOLAR - MODULO DE ALUNOS'))
        print('=' * 60)

        matricula = lernumero('Matricula do Aluno (0 - Mostra todos): ')

        if matricula == 0:
            mostratodosalunos()
            continue

        if consultaraluno(matricula) == 'nc':
            print('Este aluno nao esta cadastrado. Vamos cadastra-lo!')
            nome = input('Nome do aluno: ').upper()

            if nomevalido(nome):
                mostratodasturmas()
                idturma = lernumero('ID da turma do aluno: ')

                if consultarturma(idturma) == 'nc':
                    print('TURMA INEXISTENTE')
                else:
                    print(cadastraraluno(matricula, nome, idturma))
            else:
                print('NOME INVALIDO! O nome nao pode ser vazio.')

        else:
            print('ALUNO JA CADASTRADO')
            op = input('Escolha: [A]-Alterar [E]-Excluir '
                       '[T]-Turma do aluno [C]-Cancelar ==> ').upper()
            while op != 'A' and op != 'E' and op != 'T' and op != 'C':
                op = input('ERRO!!! Escolha CORRETAMENTE: [A] [E] [T] [C] ==> ').upper()

            if op == 'A':
                print('Atencao: a matricula nao pode ser alterada.')
                nome = input('Novo nome do aluno: ').upper()

                if nomevalido(nome):
                    mostratodasturmas()
                    idturma = lernumero('Nova turma do aluno: ')

                    if consultarturma(idturma) == 'nc':
                        print('TURMA INEXISTENTE')
                    else:
                        print(alteraraluno(matricula, nome, idturma))
                else:
                    print('NOME INVALIDO! O nome nao pode ser vazio.')

            elif op == 'E':
                confirma = input('ATENCAO!!! CONFIRMA EXCLUSAO? '
                                 'S-SIM ou N-NAO: ')
                while confirma != 'S' and confirma != 'N':
                    confirma = input('RESPOSTA INEXISTENTE!!! '
                                     'CONFIRMA EXCLUSAO? S-SIM ou N-NAO: ')
                if confirma == 'S':
                    print(excluiraluno(matricula))
                else:
                    print('Exclusao cancelada pelo usuario.')

            elif op == 'T':
                turmadoaluno(matricula)

            else:
                print('Operacao cancelada pelo usuario.')

        print('\n')
        print('=' * 60)
        if input('Continuar no modulo de ALUNOS? '
                 '1-Sim ou qualquer tecla para voltar: ') == '1':
            continue
        else:
            break

if abrebanco() == 1:

    while True:
        print('\n')
        print('=' * 60)
        print('{:^60}'.format('SISTEMA DE GERENCIAMENTO ESCOLAR'))
        print('=' * 60)
        print('1 - TURMAS')
        print('2 - ALUNOS')
        print('Qualquer outra tecla - SAIR DO PROGRAMA')
        print('=' * 60)

        opcao = input('O que deseja rodar? ==> ')

        if opcao == '1':
            menuturmas()
        elif opcao == '2':
            menualunos()
        else:
            break

    comandosql.close()
    conexao.close()
    print('Banco de dados fechado. FIM DO PROGRAMA!')

else:
    print('FIM DO PROGRAMA!!! Problema na conexao com o banco de dados.')