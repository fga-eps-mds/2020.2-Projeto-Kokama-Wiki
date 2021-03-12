# Guia de Contribuição

Antes de realizar uma contribuição, conheça um pouco sobre o objetivo do projeto e também sobre o povo Kokama na nossa [documentação](https://fga-eps-mds.github.io/2020.2-Projeto-Kokama-Wiki/).

## Como contribuir?

Contribuições ao projeto são muito bem-vindas. Para manter um projeto bem organizado, ao contribuir observe as políticas abaixo:

- Caso seja um contribuidor externo, faça um _fork_ do repositório e submeta as modificações através de _pull request_;
- [Políticas de _issues_](CONTRIBUTING.md#política-de-issues);
- [Política de _branchs_](CONTRIBUTING.md#política-de-branches);
- [Política de _commits_](CONTRIBUTING.md#política-de-commits);
- [Política de _merges_ e _pull request_](CONTRIBUTING.md#política-de-merges-e-pull-requests).

### Política de Issues

Para criação de issue, um [template de issue](https://github.com/fga-eps-mds/2020.2-Projeto-Kokama-Wiki/issues/new/choose) deve ser seguido.

Caso encontre um bug ou tenha alguma sugestão de melhoria ao projeto, siga os passos abaixo:

1. Verifique se já existe a [issue no repositório](https://github.com/fga-eps-mds/2020.2-Projeto-Kokama-Wiki/issues);
2. Caso não exista nenhuma issue relacionada, [crie uma issue](https://github.com/fga-eps-mds/2020.2-Projeto-Kokama-Wiki/issues/new/choose);
   1. Escolha o template de issue;
   2. Preencha a issue de acordo com a orientação do template;
   3. Defina as labels que são pertinentes ao problema ou sugestão;
   4. Se aplicável, defina os responsáveis pela issue, o milestone e o projeto.
3. Retire dúvidas através da issue.

### Gitflow

Para contribuir com o projeto, observe as políticas adotadas em relação a padronização e organização de código e documentação.

#### Documentação

Regras:

1. Novas _branchs_ devem ser criadas a partir da _main_;
2. Depois de fazer modificações na _branch_, submete-a por _pull request_ para integrar a _branch_ principal (_main_);
3. Após aprovado ou recusado o _pull request_, apague a _branch_.

#### Código

1. Novas _branchs_ devem ser criadas a partir da _dev_;
2. Depois de fazer modificações na _branch_, submete-a por _pull request_ para integrar a _branch_ secundária (_dev_);
3. Após aprovado ou recusado o _pull request_, apague a _branch_.

### Política de _Branches_

#### _main_

_main_ é a _branch_ de produção, onde se encontra a versão que estará disponível para utilização no mercado.

#### _dev_

_dev_ é a _branch_ de homologação, onde se encontra a versão mais atualizada do projeto.

#### Nome das _Branches_

Crie a _branch_ com a seguinte estrutura:

```bash
[número-da-issue]-<nome-significativo-da-branch-separada-por-hífens-com-letras-minusculas-sem-acento>
```

### Política de Commits

Os commits deverão ser feitos em inglês iniciando com um verbo no presente simples, como, por exemplo: "Create a new API entrypoint".

Para commits individuais, use: `git commit -m "Mensagem"`.
Para commits em pares, digite `git commit` e atribua os _co-authoreds_ na mensagem:

```bash
Mensagem do commit


Co-authored-by: Nome e sobrenome do parceiro(a) <email@email.com>
```

- Observação: quebrar duas linhas após a mensagme do commit.

#### Título dos _Commits_

Commits devem seguir os seguitnes modelos:

- Commit de correção de _bugs_ ou falhas na _main_: `[HOTFIX] Mensagem`;
- Commits de correção de _bugs_ ou falhas gerais: `[FIX] Mensagem`;
- Os demais commits devem seguir o modelo: `Mensagem`.

### Política de _Merges_ e _Pull Requests_

#### _Pull Requests_

Pull requests serão realizados para controle de estabilidade das _branches_:

- _main_;
- _dev_.

Quando disponível uma nova _release_ ou funcionalidade, esta será integrada através de _pull request_ na _branch main_.

Caso um _pull request_ já estava aberto e atualmente está em progresso, o título deve seguir o padrão `[WIP] Título`.

Durante a criação de um _pull request_, deve-se observar o [template definido no repositório](https://github.com/fga-eps-mds/2020.2-Projeto-Kokama-Wiki/compare).

##### _Code Review_

Na revisão de código de _pull request_, observe os pontos abaixo:

- O _pull request_ deve ser aceito por pelo menos um membro da equipe;
- O revisor deve clonar a _branch_ do _pull request_ e verificar se as modificações de código ou documentação são coerente;
- Em caso de aceitação do _pull request_, deve-se fazer a aprovação e realizar o merge;
- Caso o _pull request_ esteja faltando algum requisito, deve-se informar ao contribuidor as mudanças necessárias;
- Caso o _pull request_ não faça sentido, já tenha sido resolvido ou seja duplicado, deve ser fechado e feito um comentário a respeito.
