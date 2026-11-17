import pandas as pd
from reportlab.pdfgen import canvas


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


def gerarhtml(classificacao):
    try:
        arquivo = open('classificacao.html', 'w', encoding='utf-8')

        arquivo.write('<!DOCTYPE html>\n')
        arquivo.write('<html lang="pt-br">\n')
        arquivo.write('<head>\n')
        arquivo.write('<meta charset="utf-8">\n')
        arquivo.write('<title>Campeonato Brasileiro 2026</title>\n')
        arquivo.write('</head>\n')
        arquivo.write('<body>\n')

        arquivo.write('<h1 align="center">CAMPEONATO BRASILEIRO SÉRIE A - 2026</h1>\n')
        arquivo.write('<p align="center">Classificação gerada pelo programa Python a partir da planilha da CBF</p>\n')

        arquivo.write('<p align="center">\n')
        arquivo.write('<a href="classificacao.pdf" target="_blank">VER TABELA EM PDF</a>\n')
        arquivo.write('</p>\n')

        arquivo.write('<table align="center" border="1" cellpadding="6">\n')
        arquivo.write('<tr>\n')
        arquivo.write('<th>POS</th><th>TIME</th><th>PTS</th><th>J</th>')
        arquivo.write('<th>V</th><th>E</th><th>D</th>\n')
        arquivo.write('</tr>\n')

        for linha in range(0, len(classificacao)):
            time = classificacao[linha]

            cor = ''
            if linha < 4:
                cor = ' bgcolor="#bff0c8"'
            if linha >= len(classificacao) - 4:
                cor = ' bgcolor="#f5bdbd"'

            arquivo.write(f'<tr{cor}>\n')
            arquivo.write(f'<td align="center">{time[0]}º</td>\n')
            arquivo.write(f'<td>{time[1]}</td>\n')
            arquivo.write(f'<td align="center"><b>{time[6]}</b></td>\n')
            arquivo.write(f'<td align="center">{time[2]}</td>\n')
            arquivo.write(f'<td align="center">{time[3]}</td>\n')
            arquivo.write(f'<td align="center">{time[4]}</td>\n')
            arquivo.write(f'<td align="center">{time[5]}</td>\n')
            arquivo.write('</tr>\n')

        arquivo.write('</table>\n')

        arquivo.write('<p align="center">Verde: 4 melhores times | Vermelho: 4 piores times</p>\n')
        arquivo.write('<p align="center">Vitória = 3 pontos | Empate = 1 ponto | Derrota = 0 ponto</p>\n')

        arquivo.write('</body>\n')
        arquivo.write('</html>\n')

        arquivo.close()
        print('Arquivo classificacao.html gerado com sucesso!')

    except Exception as erro:
        print(f'Erro ao gerar o arquivo html: {erro}')


def gerarpdf(classificacao):
    try:
        pdf = canvas.Canvas('classificacao.pdf')

        pdf.setTitle('Campeonato Brasileiro Serie A 2026')

        pdf.setFillColor('black')
        pdf.setFont("Helvetica-Bold", 17)
        pdf.drawString(120, 795, 'CAMPEONATO BRASILEIRO SÉRIE A - 2026')

        pdf.setFont("Helvetica-Oblique", 10)
        pdf.drawString(170, 778, 'Classificação gerada pelo programa Python a partir da planilha da CBF')

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(55, 745, 'POS')
        pdf.drawString(110, 745, 'TIME')
        pdf.drawString(330, 745, 'PTS')
        pdf.drawString(390, 745, 'J')
        pdf.drawString(440, 745, 'V')
        pdf.drawString(480, 745, 'E')
        pdf.drawString(520, 745, 'D')

        pdf.setFont("Helvetica", 12)
        pdf.drawString(55, 737, '_' * 85)

        espaco = int(640 / len(classificacao))
        if espaco > 24:
            espaco = 24

        x = 745 - espaco - 10

        for linha in range(0, len(classificacao)):
            time = classificacao[linha]

            pdf.setFillColor('black')
            if linha < 4:
                pdf.setFillColor('green')
            if linha >= len(classificacao) - 4:
                pdf.setFillColor('red')

            pdf.setFont("Helvetica-Bold", 11)
            pdf.drawString(55, x, f'{time[0]}º')
            pdf.drawString(110, x, f'{time[1]}')
            pdf.drawString(330, x, f'{time[6]}')

            pdf.setFont("Helvetica", 11)
            pdf.drawString(390, x, f'{time[2]}')
            pdf.drawString(440, x, f'{time[3]}')
            pdf.drawString(480, x, f'{time[4]}')
            pdf.drawString(520, x, f'{time[5]}')

            x -= espaco

        pdf.setFillColor('black')
        pdf.setFont("Helvetica", 12)
        pdf.drawString(55, x + 10, '_' * 85)

        pdf.setFont("Helvetica-Oblique", 9)
        pdf.drawString(55, x - 10, 'J = jogos | V = vitórias | E = empates | D = derrotas | PTS = pontos')
        pdf.drawString(55, x - 24, 'Vitória = 3 pontos | Empate = 1 ponto | Derrota = 0 ponto')
        pdf.drawString(55, x - 38, 'Em verde os 4 melhores times e em vermelho os 4 piores times')

        pdf.save()
        print('Arquivo classificacao.pdf gerado com sucesso!')

    except Exception as erro:
        print(f'Erro ao gerar o arquivo pdf: {erro}')


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
    gerarhtml(classificacao)
    gerarpdf(classificacao)
    print('=' * 70)
    print('Abra o arquivo classificacao.html para ver a pagina web.')
    print('Na pagina existe um botao que abre o classificacao.pdf.')
    print('=' * 70)
