import json
import sys
import datetime


class GithubUser:
    """Represent a github user from team 03
    User is identified by a number, github username and name
    """

    def __init__(self, number, username, name):
        self.number = number
        self.username = username
        self.name = name


member_username_name = [
    GithubUser(1, 'aluzianobriceno', 'Ana Júlia'),
    GithubUser(2, 'andrelucax', 'André Lucas'),
    GithubUser(3, 'SFernandoS', 'Fernando Vargas'),
    GithubUser(4, 'laispa', 'Lais Portela'),
    GithubUser(5, 'leomedeiros1', 'Leonardo Medeiros'),
    GithubUser(6, 'lievertom', 'Lieverton Silva'),
    GithubUser(7, 'nickby2', 'Lucas Rodrigues'),
    GithubUser(8, 'luisgaboardi', 'Luís Guilherme'),
    GithubUser(9, 'LightZX', 'Luiz Gustavo'),
    GithubUser(10, 'WelisonR', 'Welison Regis')
]


class ScrumDocuments:
    """Automatically generate the planning document from scrum based on questions
    Ask the user about the sprint information and generate a full report of the sprint
    It is necessary that a file "issues.json" exists in the same directory, this file can be
    generated running the script "issues_crawler.js" in the browser console
    """

    def __init__(self):
        self.issues = self.get_issues()
        self.sprint = int(input('Digite o número da sprint: '))
        self.sprint_start = input(
            'Digite a data de início da sprint (dd/mm/yyyy): ')
        self.sprint_end = input(
            'Digite a data de fim da sprint (dd/mm/yyyy): ')
        self.sprint_duration = input(
            'Digite a duração (número) da sprint em dias: ')
        self.show_members()
        print('Digite o número do autor do documento: ', end='')
        self.author = self.get_author()
        self.sprint_pairs = self.get_sprint_pairs()
        self.f = open('../docs/management/sprints/sprint-'+str(self.sprint)+'-planning.md', 'w+')

    def get_issues(self):
        try:
            with open('issues.json') as json_file:
                issues = json.load(json_file)
        except IOError:
            print('Não foi possível encontrar o arquivo json com a issues.')
            print('Renomeie o arquivo com as issues para "issues.json"')
            sys.exit()

        return issues

    def get_sprint_pairs(self):
        pairs = []
        while True:
            self.show_members()
            print('Escolha o primeiro integrante da dupla (0 para sair): ', end='')
            member1 = self.get_author()
            if member1 == 0:
                break

            self.show_members()
            print('Escolha o segundo integrante da dupla: ', end='')
            member2 = self.get_author()
            if member2 == 0:
                break

            pair = f'{member1} e {member2}'

            pairs.append(pair)

        return pairs

    def show_members(self):
        print('\n')
        for member_data in member_username_name:
            print(f'{member_data.number} - {member_data.name}')
        print('\n')

    def get_author(self):
        member_position = int(input())

        if member_position == 0:
            return 0
        if member_position < 0 or member_position >= 11:
            print('Número de usuário inválido. Abortando...')
            sys.exit()

        member = list(filter(lambda member: member.number == member_position, member_username_name))[0]
        author_text = f'[{member.name}](http://www.github.com/{member.username})'

        return author_text

    def generate_planning(self):
        self.f.write(f'# Planejamento da sprint {self.sprint}\n\n')

        self.print_history()
        self.print_sprint_time()
        self.print_pairs()
        self.print_sprint_backlog()
        self.print_roles()

    def print_history(self):
        today = datetime.date.today()
        date = today.strftime("%d/%m/%Y")

        self.f.write('## Histórico de revisão\n\n')
        self.f.write('| Data | Autor | Modificações | Versão |\n')
        self.f.write(f'|:---:|---|---|:---:|\n')
        self.f.write(f'| {date} | {self.author} | Adiciona planejamento da sprint {self.sprint} | 1.0 |\n')
        self.f.write('\n')

    def print_sprint_time(self):
        self.f.write('## Tamanho da sprint\n\n')
        self.f.write('| Início da sprint | Término da Sprint | Duração |\n')
        self.f.write('|:---:|:---:|:---:|\n')
        self.f.write(f'| {self.sprint_start} | {self.sprint_end} | {self.sprint_duration} dias |\n')
        self.f.write('\n')

    def print_pairs(self):
        self.f.write('## Pareamentos\n\n')
        self.f.write('| Paramento | Integrantes |\n')
        self.f.write('|:---:|---|\n')

        for i, pair in enumerate(self.sprint_pairs):
            self.f.write(f'| {i+1} | {pair} |\n')
        self.f.write('\n')

    def print_sprint_backlog(self):
        self.f.write('## Sprint Backlog\n\n')
        self.f.write('| Issue | Pontos | Responsáveis |\n')
        self.f.write('|---|:---:|---|\n')

        for issue in self.issues:
            issue_text = issue['text']
            issue_url = issue['url']
            issue_points = issue['points']

            self.f.write(f'| [{issue_text}]({issue_url}) | {issue_points} | ')

            for i, assign in enumerate(issue['assigns']):
                name = assign['name']
                assign = assign['assign']

                if (name == 'Não definido'):
                    name = 'Todos'
                    assign = 'fga-eps-mds/2020.2-Projeto-Kokama-Wiki'

                if i == 0:
                    self.f.write(f'[{name}](https://github.com/{assign})')
                elif i == len(issue['assigns'])-1:
                    self.f.write(f' e [{name}](https://github.com/{assign})')
                else:
                    self.f.write(f', [{name}](https://github.com/{assign})')
            self.f.write(' |\n')
        self.f.write('\n')

    def print_roles(self):
        self.f.write('## Papéis\n\n')
        self.f.write('| Papel | Integrante |\n')
        self.f.write('|:---:|---|\n')
        self.f.write('| **Scrum Master** | Welison Regis |\n')
        self.f.write('| **DevOps** | Leonardo Medeiros |\n')
        self.f.write('| **Arquiteto** | Lieverton Santos |\n')
        self.f.write('| **Analista de dados** | André Pinto |\n')


if __name__ == '__main__':
    sprint = ScrumDocuments()
    sprint.generate_planning()
