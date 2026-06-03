# ERP Modular em Django

Projeto de estudo e evolucao gradual de um ERP modular usando Python e Django.

O objetivo principal e aprender desenvolvimento de software, arquitetura de sistemas, banco de dados e boas praticas enquanto construimos uma base realista para um sistema de gestao.

## Objetivo inicial

Criar uma fundacao simples e organizada para um ERP que possa crescer com o tempo.

Modulos iniciais planejados:

- Clientes
- Produtos
- Pedidos
- Pagamentos

## Estado atual

- Projeto Django criado com pasta principal `config`.
- Banco SQLite configurado para desenvolvimento local.
- App `clientes` criado e registrado.
- Model `Cliente` criado.
- Primeira migration de `clientes` aplicada.
- Admin de clientes configurado para cadastro, busca e filtros.
- Validacao simples de CPF/CNPJ no admin de clientes.
- App `produtos` criado e registrado.
- Model `Produto` criado para itens vendaveis.
- Admin de produtos configurado para cadastro, busca e filtros.
- App `pedidos` criado e registrado.
- Models `PedidoVenda` e `ItemPedidoVenda` criados.
- Admin de pedidos configurado com itens em linha.
- Documentacao inicial criada na pasta `docs`.

## Tecnologias

- Python
- Django
- SQLite no desenvolvimento inicial
- Git e GitHub para versionamento

## Como rodar localmente

Ativar o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Rodar as migrations:

```powershell
python manage.py migrate
```

Iniciar o servidor de desenvolvimento:

```powershell
python manage.py runserver
```

Abrir no navegador:

```text
http://127.0.0.1:8000/
```

## Documentacao

- `docs/aprendizado.md`: conceitos aprendidos durante o desenvolvimento.
- `docs/decisoes_tecnicas.md`: decisoes tecnicas e seus motivos.
