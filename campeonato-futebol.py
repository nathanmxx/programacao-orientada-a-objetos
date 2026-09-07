times = []

print('=' * 55)
print('  BEM-VINDO AO SISTEMA DE CAMPEONATO DE FUTEBOL')
print('=' * 55)
print('  Digite FIM no nome do time para encerrar.')
print('=' * 55)

print('\n--- CADASTRO DE TIME ---')
nome_time = input('Digite o nome do time: ')

while nome_time != 'FIM' and nome_time != 'fim':

    pontos_lista = []

    for partida in range(1, 6):

        ponto_valido = False

        while ponto_valido == False:

            ponto = input(f'  Pontos da partida {partida} (0, 1 ou 3): ')

            if ponto == '0' or ponto == '1' or ponto == '3':

                pontos_lista.append(int(ponto))

                ponto_valido = True

            else:
                print('  ERRO! Valor invalido. Digite apenas 0, 1 ou 3.')

    pontos_tupla = (
        pontos_lista[0],
        pontos_lista[1],
        pontos_lista[2],
        pontos_lista[3],
        pontos_lista[4]
    )

    total_pontos = 0

    for p in pontos_tupla:
        total_pontos = total_pontos + p

    dados_time = {
        'nome': nome_time,
        'pontos_partidas': pontos_tupla,
        'total': total_pontos
    }

    times.append(dados_time)

    print(f'\n  Time {nome_time} cadastrado! Total de pontos: {total_pontos}')

    print('\n--- CADASTRO DE TIME ---')
    nome_time = input('Digite o nome do time (ou FIM para encerrar): ')

print('\n')
print('=' * 55)
print('    ESTRUTURA COMPLETA DOS DADOS ARMAZENADOS')
print('=' * 55)
print(f'times = {times}')

for i in range(0, len(times)):

    for j in range(i + 1, len(times)):

        if times[j]['total'] > times[i]['total']:

            aux = times[i]
            times[i] = times[j]
            times[j] = aux

print('\n')
print('=' * 55)
print('         CLASSIFICACAO FINAL DO CAMPEONATO')
print('=' * 55)

for posicao, t in enumerate(times):

    vitorias = 0

    for ponto in t['pontos_partidas']:

        if ponto == 3:
            vitorias = vitorias + 1

    aproveitamento = (t['total'] * 100) / 15

    print(f'\n{posicao + 1} lugar - Time: {t["nome"]}')
    print(f'  Pontos por partida: {t["pontos_partidas"]}')
    print(f'  Total de pontos:    {t["total"]}')
    print(f'  Vitorias:           {vitorias}')
    print(f'  Aproveitamento:     {aproveitamento:.2f}%')

print('\n')
print('=' * 55)
print('            DESTAQUES DO CAMPEONATO')
print('=' * 55)

if len(times) > 0:

    print(f'\nCAMPEAO:      {times[0]["nome"]} com {times[0]["total"]} pontos')

    if len(times) >= 2:
        print(f'VICE CAMPEAO: {times[1]["nome"]} com {times[1]["total"]} pontos')

    maior_vitorias = -1
    nome_mais_vitorias = ''

    for t in times:

        vitorias = 0

        for ponto in t['pontos_partidas']:

            if ponto == 3:
                vitorias = vitorias + 1

        if vitorias > maior_vitorias:

            maior_vitorias = vitorias
            nome_mais_vitorias = t['nome']

    print(f'\nTIME COM MAIS VITORIAS: {nome_mais_vitorias} ({maior_vitorias} vitorias)')

    menor_pontos = times[0]['total']
    nome_menos_pontos = times[0]['nome']

    for t in times:

        if t['total'] < menor_pontos:

            menor_pontos = t['total']
            nome_menos_pontos = t['nome']

    print(f'\nTIME COM MENOS PONTOS: {nome_menos_pontos} ({menor_pontos} pontos)')

    print('\n')
    print('=' * 55)
    print('         VITORIAS E APROVEITAMENTO POR TIME')
    print('=' * 55)

    for t in times:

        vitorias = 0

        for ponto in t['pontos_partidas']:

            if ponto == 3:
                vitorias = vitorias + 1

        aproveitamento = (t['total'] * 100) / 15

        print(f'  {t["nome"]}: {vitorias} vitoria(s) - aproveitamento: {aproveitamento:.2f}%')

else:
    print('\nNenhum time foi cadastrado.')

print('\n' + '=' * 55)
print('         FIM DO CAMPEONATO - OBRIGADO!')
print('=' * 55)
