# Guia de Contribuição

Antes de realizar uma contribuição, conheça um pouco sobre o objetivo do projeto e também sobre o povo Kokama na nossa [documentação](https://fga-eps-mds.github.io/EPS-2020-2-G3/).

## Como contribuir?

Contribuições ao projeto são muito bem-vindas. Para manter um projeto bem organizado, ao contribuir observe as políticas abaixo:

*   Caso seja um contribuidor externo, faça um *fork* do repositório e submeta as modificações através de *pull request*;
*   [Políticas de *issues*](CONTRIBUTING.md#política-de-issues);
*   [Política de *branchs*](CONTRIBUTING.md#política-de-branches);
*   [Política de *commits*](CONTRIBUTING.md#política-de-commits);
*   [Política de *pull request*](CONTRIBUTING.md#política-de-merges-e-pull-requests).

### Política de Issues

Para criação de issue, um [template de issue](.github/ISSUE_TEMPLATE) deve ser seguido.

Caso encontre um bug ou tenha alguma sugestão de melhoria ao projeto, siga os passos abaixo:

1. Verifique se já existe a [issue no repositório](https://github.com/fga-eps-mds/EPS-2020-2-G3/issues);
2. Caso não exista nenhuma issue relacionada, [crie uma issue](https://github.com/fga-eps-mds/EPS-2020-2-G3/issues/new/choose);
   1. Escolha o template de issue;
   2. Preencha a issue de acordo com a orientação do template;
   3. Defina as labels que são pertinentes ao problema ou sugestão;
   4. Se aplicável, defina os responsáveis pela issue, o milestone e o projeto.
3. Retire dúvidas através da issue.

### Gitflow

Para contribuir com o projeto, observe as políticas adotadas em relação a padronização e organização de código e documentação.

#### Documentação

Regras:

1. Novas *branchs* devem ser criadas a partir da *main*;
2. Depois de fazer modificações na *branch*, submete-a por *pull request* para integrar a *branch* principal (*main*);
3. Após aprovado ou recusado o *pull request*, apague a *branch*.

#### Código

1. Novas *branchs* devem ser criadas a partir da *dev*;
2. Depois de fazer modificações na *branch*, submete-a por *pull request* para integrar a *branch* secundária (*dev*);
3. Após aprovado ou recusado o *pull request*, apague a *branch*.

### Política de *Branches*

#### *main*

*main* é a *branch* de produção, onde se encontra a versão que estará disponível para utilização no mercado.

#### *dev*

*dev* é a *branch* de homologação, onde se encontra a versão mais atualizada do projeto.

#### Nome das *Branches*

Crie a *branch* com a seguinte estrutura: 

```bash
[número-da-issue]-<nome-da-branch-separada-por-hífens-com-letras-minusculas-sem-acento>
```

### Política de Commits

Os commits deverão ser feitos em inglês iniciando com um verbo no presente simples, como, por exemplo: "Create a new API entrypoint".

Para commits individuais, use: `git commit -m "Mensagem"`.
Para commits em pares, digite `git commit` e atribua os *co-authoreds* na mensagem:

```
Mensagem do commit


Co-authored-by: Nome e sobrenome do parceiro(a) <email@email.com>
```

*   Observação: quebrar duas linhas após a mensagme do commit.

#### Título dos *Commits*

Commits devem seguir os seguitnes modelos:

*   Commit de correção de *bugs* ou falhas na *main*: `[HOTFIX] Mensagem`;
*   Commits de correção de *bugs* ou falhas gerais: `[FIX] Mensagem`;
*   Os demais commits devem seguir o modelo: `Mensagem`.

### Política de *Merges* e *Pull Requests*

#### *Pull Requests*

Pull requests serão realizados para controle de estabilidade das *branches*:
*   *main*;
*   *dev*.

Quando disponível uma nova *release* ou funcionalidade, esta será integrada através de *pull request* na *branch main*.

Durante a criação de um *pull request*, deve-se observar o [template definido no repositório](https://github.com/fga-eps-mds/EPS-2020-2-G3/compare).

##### *Code Review*

Na revisão de código de *pull request*, observe os pontos abaixo:

*   O *pull request* deve ser aceito por pelo menos um membro da equipe;
*   O revisor deve clonar a *branch* do *pull request* e verificar se as modificações de código ou documentação são coerente;
*   Em caso de aceitação do *pull request*, deve-se fazer a aprovação e realizar o merge;
*   Caso o *pull request* esteja faltando algum requisito, deve-se informar ao contribuidor as mudanças necessárias;
*   Caso o *pull request* não faça sentido, já tenha sido resolvido ou seja duplicado, deve ser fechado e feito um comentário a respeito.
