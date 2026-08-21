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

## Usar o admin do Django no inicio

Decidimos usar o painel administrativo do Django como primeira forma de cadastrar e testar clientes.

Motivo:

- o admin ja vem pronto no Django;
- permite testar o model `Cliente` sem criar telas proprias agora;
- ajuda a validar se banco, migrations e cadastro estao funcionando;
- evita criar interface antes de termos a base do modulo bem entendida.

Essa escolha nao substitui uma interface propria no futuro. Ela apenas ajuda no desenvolvimento inicial.

## Mostrar documento como CPF/CNPJ no admin

Decidimos manter o campo tecnico como:

```text
documento
```

Mas mostrar no admin como:

```text
CPF/CNPJ
```

Tambem adicionamos placeholder:

```text
Somente numeros
```

Motivo:

- `documento` continua sendo um nome simples e flexivel no codigo;
- `CPF/CNPJ` fica mais claro para quem esta cadastrando;
- o placeholder orienta sem deixar a tela muito poluida;
- ainda nao precisamos usar JavaScript para mudar o campo dinamicamente.

Validacoes mais avancadas de CPF e CNPJ ficam para uma etapa futura.

## Validar documento no admin de clientes

Decidimos adicionar uma validacao simples no formulario do admin de clientes.

Regras atuais:

- pessoa fisica deve informar 11 numeros;
- pessoa juridica deve informar 14 numeros;
- documento deve conter somente numeros.

Motivo:

- evita salvar dados claramente incorretos;
- mantem a regra simples para esta fase do projeto;
- nao adiciona biblioteca externa ainda;
- deixa validacoes completas de CPF e CNPJ para uma etapa futura.

## Criar modulo produtos

Decidimos criar o app `produtos` depois de fechar o primeiro ciclo do modulo `clientes`.

Motivo:

Pedidos futuramente dependem de dois cadastros basicos:

```text
cliente
produto
```

Por isso, antes de criar pedidos, faz sentido permitir cadastrar produtos vendaveis.

## Produto representa item vendavel

Decidimos que `Produto` representa algo vendido ao cliente.

Exemplos:

```text
Laje H8
Manilha 60cm
Piso intertravado
Meio-fio de concreto
```

Motivo:

Produto vendido, estoque, insumo, lote e producao sao conceitos relacionados, mas nao sao a mesma coisa.

Nesta fase, evitamos colocar regras de estoque, materia-prima ou lote dentro do model `Produto`.

## Produto com codigo interno

Decidimos adicionar o campo:

```python
codigo = models.CharField(max_length=30, unique=True)
```

Motivo:

- nomes de produtos podem ser parecidos;
- codigo ajuda na busca e na rotina operacional;
- codigo pode conter letras, numeros e tracos;
- `unique=True` evita dois produtos com o mesmo codigo.

## Ordenar produtos por codigo

Decidimos ordenar produtos por `codigo`.

Motivo:

Em um ERP, codigo tende a ser mais estavel e mais operacional do que o nome.

Exemplo:

```text
LAJ-H8
MAN-060
MAN-080
```

## Historico basico do admin

Decidimos nao adicionar `criado_por` e `atualizado_por` agora.

Motivo:

O admin do Django ja registra historico basico de acoes feitas pelo painel administrativo, incluindo usuario, data e tipo de alteracao.

Campos de auditoria no model podem ser uteis no futuro, mas devem ser pensados como um padrao para varios models, nao como uma decisao isolada no primeiro cadastro de produtos.

## Criar modulo pedidos

Decidimos criar o app `pedidos` depois dos cadastros de clientes e produtos.

Motivo:

Pedido de venda depende de:

```text
cliente
produto
```

Assim, fazia sentido construir primeiro os cadastros base.

## Usar PedidoVenda em vez de Pedido

Decidimos nomear o model como `PedidoVenda`.

Motivo:

No futuro o sistema pode ter outros tipos de pedido, como:

- pedido de compra de materia-prima;
- ordem de producao;
- solicitacao interna.

O nome `PedidoVenda` deixa claro que este model representa venda para cliente.

## Separar PedidoVenda e ItemPedidoVenda

Decidimos criar:

```text
PedidoVenda
ItemPedidoVenda
```

Motivo:

Um pedido pode ter varios produtos.

`PedidoVenda` guarda o cabecalho do pedido.

`ItemPedidoVenda` guarda cada linha de produto, quantidade e preco.

## Numero do pedido de venda

Decidimos criar o campo `numero_pedido` como identificador de negocio do pedido.

Motivo:

O `id` do banco e tecnico. O `numero_pedido` e melhor para conversas, admin, telas e documentos.

Nesta primeira etapa, o numero sera preenchido manualmente.

Proximo refinamento planejado:

Criar uma sequencia propria para gerar automaticamente numeros de pedidos de venda.

## Criar testes junto com as regras

Decidimos adicionar testes automatizados junto com as regras importantes de cada modulo.

Motivos:

- evita acumular testes para o fim do projeto;
- permite verificar rapidamente se uma alteracao quebrou uma regra existente;
- registra no codigo o comportamento esperado;
- mantém os testes organizados por app;
- preserva os testes manuais no admin para validar a experiencia de uso.

Nesta fase, os testes cobrem apenas comportamentos que ja existem nos models e formularios.

Regras futuras devem receber seus testes quando forem implementadas, sem antecipar regras que ainda nao foram decididas.

Os testes usam o banco temporario do `TestCase`, para nao alterar o banco local de desenvolvimento.
