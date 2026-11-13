import pandas as pd


def lerplanilha(nomearquivo):
    times = []
    try:
        arquivo = pd.ExcelFile(nomearquivo)
        nomeplanilha = arquivo.sheet_names[0]
        print(f'Planilhas do arquivo ==>> {arquivo.sheet_names}')
        print(f'Lendo a planilha: {nomeplanilha}')
        df = pd.read_excel(nomearquivo, sheet_name=nomeplanilha)

        for linha in range(0, len(df)):
            jogos = str(df.iloc[linha, 1])
            if jogos.isnumeric():
                nome = df.iloc[linha, 0]
                vitorias = int(df.iloc[linha, 2])
                empates = int(df.iloc[linha, 3])
                derrotas = int(df.iloc[linha, 4])

                pontos = vitorias * 3 + empates * 1

                times.append([pontos, nome, int(jogos), vitorias, empates, derrotas])

        return times

    except Exception as erro:
        print(f'Erro ao ler a planilha: {erro}')
        return times


def classificar(times):
    times.sort(reverse=True)

    classificacao = []

    for linha in range(0, len(times)):
        time = times[linha]
        pontos = time[0]

        colocacao = 1
        for outro in range(0, len(times)):
            if times[outro][0] > pontos:
                colocacao = colocacao + 1

        classificacao.append([colocacao, time[1], time[2], time[3], time[4], time[5], pontos])

    return classificacao


print('=' * 70)
print('{:^70}'.format('CAMPEONATO BRASILEIRO SERIE A - 2026'))
print('{:^70}'.format('Leitura da planilha da CBF e geracao da classificacao'))
print('=' * 70)

nomearquivo = input('Informe o nome do arquivo excel da CBF: ')
times = lerplanilha(nomearquivo)

if len(times) == 0:
    print('=' * 70)
    print('NENHUM TIME FOI LIDO!')
    print('Confira se o nome do arquivo esta correto e se ele esta na pasta do programa.')
    print('=' * 70)
else:
    classificacao = classificar(times)

    print('=' * 70)
    print('{:^70}'.format(f'CLASSIFICACAO - {len(classificacao)} TIMES'))
    print('=' * 70)
    print('{:<6}{:<24}{:>5}{:>6}{:>5}{:>5}{:>5}'.format('POS', 'TIME', 'PTS', 'J', 'V', 'E', 'D'))
    print('-' * 70)

    for time in classificacao:
        print('{:<6}{:<24}{:>5}{:>6}{:>5}{:>5}{:>5}'.format(f'{time[0]}º', time[1], time[6], time[2], time[3], time[4], time[5]))

    print('=' * 70)
