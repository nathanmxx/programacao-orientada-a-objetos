# Programação Orientada a Objetos

Programas em Python da disciplina de Programação Orientada a Objetos, no 2º ano
do ensino médio técnico.

## Programas

### medias-da-turma.py

Recebe a quantidade de alunos e de disciplinas, lê a nota de cada aluno em cada
disciplina validando o intervalo de 0 a 10, e calcula a média da turma, a maior e
a menor média individual.

### campeonato-futebol.py

Cadastra times até o usuário digitar FIM. Cada time informa o resultado de cinco
partidas (0, 1 ou 3 pontos), guardados numa tupla dentro de um dicionário. No
fim, ordena a classificação por pontos e mostra o aproveitamento de cada time, o
time com mais vitórias e o com menos pontos.

### sistema-escolar/

Sistema de gerenciamento escolar ligado a um banco MySQL, com dois módulos.

No módulo de turmas dá para listar todas, cadastrar uma nova escolhendo entre os
seis cursos aceitos, alterar o curso, excluir e listar os alunos vinculados. No
módulo de alunos dá para listar, cadastrar informando a matrícula e a turma,
alterar, excluir e consultar em que turma o aluno está.

As regras de integridade são checadas antes de cada operação: turma com aluno
vinculado não pode ser alterada nem excluída, o ID da turma não muda depois de
criado, e só passam cursos da lista permitida. As tabelas saem formatadas com
PrettyTable.

O arquivo `banco.sql` cria o banco `escola`, as tabelas `turmas` e `alunos` com
a chave estrangeira entre elas, e já insere as 18 turmas dos seis cursos.

## Como executar

Os dois primeiros programas rodam direto, só com Python 3:

    python medias-da-turma.py

    python campeonato-futebol.py

O sistema escolar precisa de MySQL e de duas bibliotecas:

    cd sistema-escolar
    pip install -r requirements.txt
    mysql -u root -p < banco.sql
    python sistema-escolar.py

A conexão lê as variáveis de ambiente `DB_HOST`, `DB_NAME`, `DB_USER` e
`DB_PASSWORD`, e cai em `localhost`, `escola`, `root` e senha vazia quando elas
não estão definidas.

## Tecnologias

Python 3 e MySQL, com mysql-connector-python e PrettyTable no sistema escolar.

Projeto desenvolvido em equipe.
