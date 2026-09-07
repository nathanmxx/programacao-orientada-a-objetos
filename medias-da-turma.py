alunos_total = 0
notas = -1

while alunos_total < 1:
    alunos_total = int(input("me de o numero total de alunos da turma: "))
    if alunos_total < 1:
        print("numero de alunos invalido")

diciplinas_total = 0

while diciplinas_total < 1:
    diciplinas_total = int(input("me de o numero total de diciplinas da turma: "))
    if diciplinas_total < 1:
        print("numero de diciplinas invalido")


soma_medias = 0
maior_media = 0
menor_media = 10

primeiro_aluno_media = 0
ultimo_aluno_media = 0


for c1 in range(alunos_total):

    soma_notas = 0

    for c2 in range(diciplinas_total):

        notas = -1

        while notas < 0 or notas > 10:

            notas = float(input(f"me de a nota do aluno {c1+1} na disciplina {c2+1}: "))

            if notas < 0 or notas > 10:
                print("notas invalidas")

        soma_notas = soma_notas + notas


    media_aluno = soma_notas / diciplinas_total

    soma_medias = soma_medias + media_aluno


    if c1 == 0:
        primeiro_aluno_media = media_aluno
        maior_media = media_aluno
        menor_media = media_aluno


    if media_aluno > maior_media:
        maior_media = media_aluno


    if media_aluno < menor_media:
        menor_media = media_aluno


    if c1 == alunos_total - 1:
        ultimo_aluno_media = media_aluno


media_turma = soma_medias / alunos_total


print("Media da turma:", media_turma)
print("Maior media individual:", maior_media)
print("Menor media individual:", menor_media)