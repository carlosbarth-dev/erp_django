# Decisoes Tecnicas do Projeto ERP

Este arquivo registra decisoes importantes tomadas durante o desenvolvimento.

O objetivo e guardar o motivo das escolhas, nao apenas o resultado final.

## Usar Python e Django

Decidimos usar Python com Django para construir o ERP.

Motivos:

- Django ja traz uma base solida para sistemas web;
- possui ORM para trabalhar com banco de dados usando Python;
- inclui painel administrativo;
- ajuda a organizar o projeto em apps;
- e uma boa escolha para aprender desenvolvimento web com estrutura profissional.

## Comecar com SQLite

Decidimos comecar com SQLite.

Motivos:

- e simples para desenvolvimento local;
- nao exige instalar e configurar um servidor de banco agora;
- permite focar primeiro em Django, models e arquitetura;
- pode ser trocado por PostgreSQL no futuro.

Alternativa futura: PostgreSQL.

Motivo para nao usar agora: adicionaria complexidade antes de termos a base do sistema funcionando.

## Nomear o projeto principal como config

Criamos o projeto Django principal com o nome `config`.

Motivo:

`config` deixa claro que essa pasta guarda configuracoes centrais do sistema, e nao um modulo de negocio.

Isso evita confundir a pasta principal com apps como `clientes`, `produtos`, `pedidos` ou `pagamentos`.

## Usar apps separados por area do negocio

Decidimos criar apps separados para os modulos do ERP.

Primeiro app criado:

```text
clientes
```

Motivo:

Clientes sao uma parte central do sistema e futuramente se relacionam com pedidos, pagamentos, entregas e relatorios.

Essa separacao ajuda a manter o projeto modular e mais facil de expandir.

## Configurar idioma e fuso horario

Configuramos:

```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Cuiaba'
```

Motivos:

- o sistema sera usado no Brasil;
- mensagens internas e formatos devem seguir portugues do Brasil;
- datas e horarios devem considerar o fuso local da operacao.

## Cliente com tipo_pessoa + documento

Decidimos modelar cliente com:

```text
tipo_pessoa
documento
```

Em vez de criar campos separados `cpf` e `cnpj`.

Motivo:

Para o ERP, o mais importante e identificar quem esta comprando: pessoa fisica ou pessoa juridica.

Se uma pessoa fisica tambem tem uma empresa, isso normalmente representa dois clientes diferentes:

- cliente pessoa fisica com CPF;
- cliente pessoa juridica com CNPJ.

Isso evita misturar historico, pedidos, pagamentos, endereco fiscal e responsabilidades.

Alternativa considerada:

```text
cpf
cnpj
```

Motivo para nao usar agora:

Essa alternativa criaria campos vazios e exigiria regras extras para impedir que os dois fossem preenchidos ao mesmo tempo.

## Guardar CPF/CNPJ sem mascara

Decidimos guardar documento sem pontos, barras ou tracos.

Exemplo:

```text
12345678900
12345678000199
```

Motivos:

- facilita busca;
- evita duplicidade causada por formatos diferentes;
- deixa a formatacao para a interface;
- mantem o valor consistente no banco.

## Nao apagar clientes por padrao

Decidimos usar um campo `ativo`.

Motivo:

Em sistemas de gestao, apagar registros pode causar perda de historico.

Um cliente inativo pode continuar existindo para preservar pedidos, pagamentos e relatorios antigos.

## Documentar aprendizado fora do codigo

Decidimos criar a pasta `docs` com arquivos Markdown.

Arquivos iniciais:

```text
docs/aprendizado.md
docs/decisoes_tecnicas.md
```

Motivo:

Explicacoes longas dentro do codigo deixam os arquivos Python poluidos.

Comentarios no codigo devem ser curtos e explicar regras ou decisoes locais.

Explicacoes maiores ficam melhor em documentacao.

## Campo cadastrado_em no Cliente

Decidimos usar:

```python
cadastrado_em = models.DateTimeField(auto_now_add=True)
```

Em vez de `criado_em`.

Motivo:

No contexto do ERP, "cadastrado" comunica melhor a ideia de que o cliente foi registrado no sistema.

`criado_em` tambem seria tecnicamente correto, mas e mais generico.

## Primeira tabela de negocio

Criamos o model `Cliente` como primeira entidade de negocio do ERP.

Campos iniciais:

```text
tipo_pessoa
nome
documento
telefone
email
endereco
ativo
cadastrado_em
atualizado_em
```

Motivo:

Esse conjunto e pequeno o bastante para aprender e testar, mas ja cobre a base de um cadastro real de clientes.

Decidimos deixar validacoes mais avancadas de CPF/CNPJ para uma etapa futura.

## Preparar Git antes de crescer o projeto

Decidimos preparar o projeto para Git antes de criar muitos outros modulos.

Motivo:

Versionamento deve entrar cedo para proteger o historico do projeto e facilitar voltar a estados anteriores se algo quebrar.

Arquivos importantes:

```text
.gitignore
README.md
```

`.gitignore` evita versionar arquivos locais, ambiente virtual e banco SQLite.

`README.md` explica o objetivo e o estado inicial do projeto.
