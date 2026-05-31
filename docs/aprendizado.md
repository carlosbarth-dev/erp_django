# Aprendizado do Projeto ERP

Este arquivo guarda explicacoes de conceitos que aparecerem durante o desenvolvimento.

A ideia nao e decorar tudo de uma vez. A ideia e ter um lugar para voltar quando algum termo aparecer de novo.

## Ambiente virtual

O ambiente virtual fica na pasta `.venv`.

Ele isola as dependencias deste projeto. Assim, quando instalamos Django, ele fica dentro do projeto ERP e nao misturado com outros projetos do computador.

Comando usado para criar:

```powershell
python -m venv .venv
```

Comando usado para ativar no PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Quando o terminal mostra `(.venv)`, significa que ele esta usando o Python e o pip do ambiente virtual.

## pip

`pip` e o gerenciador de pacotes do Python.

Usamos ele para instalar bibliotecas externas, como o Django:

```powershell
pip install django
```

Com o ambiente virtual ativado, as dependencias sao instaladas dentro de `.venv/Lib/site-packages`.

## Projeto Django

Criamos o projeto principal com:

```powershell
django-admin startproject config .
```

O ponto final no comando significa: criar o projeto na pasta atual.

Arquivos importantes:

- `manage.py`: arquivo usado para executar comandos do Django.
- `config/settings.py`: configuracoes principais do projeto.
- `config/urls.py`: rotas principais do sistema.
- `config/asgi.py` e `config/wsgi.py`: arquivos usados futuramente para publicar o sistema em servidor.

## App Django

Um app e um modulo do sistema.

Criamos o app `clientes` com:

```powershell
python manage.py startapp clientes
```

No nosso ERP, cada app deve representar uma area do negocio, como clientes, produtos, pedidos e pagamentos.

## INSTALLED_APPS

Criar a pasta de um app nao basta.

Tambem precisamos registrar o app em `INSTALLED_APPS`, dentro de `config/settings.py`.

Isso diz ao Django que aquele modulo faz parte do projeto.

## Model

Um model e uma classe Python que representa uma tabela no banco de dados.

Exemplo conceitual:

```python
class Cliente(models.Model):
    nome = models.CharField(max_length=150)
```

Nesse exemplo, o Django entende que deve existir uma tabela para clientes com uma coluna chamada `nome`.

## CharField

`CharField` e um campo de texto curto.

Ele e usado para dados como nome, telefone, documento e outros textos com tamanho limitado.

## CPF e CNPJ como texto

CPF e CNPJ devem ser guardados como texto, nao como numero.

Motivos:

- podem comecar com zero;
- nao fazemos calculo matematico com eles;
- o objetivo e identificar, nao somar ou multiplicar.

## max_length

`max_length` define o tamanho maximo de um texto.

Exemplo:

```python
documento = models.CharField(max_length=14)
```

CPF tem 11 digitos e CNPJ tem 14 digitos. Por isso, para um campo que guarda CPF ou CNPJ sem mascara, `14` e suficiente.

## unique=True

`unique=True` impede duplicidade no banco.

No caso de documento, evita cadastrar dois clientes com o mesmo CPF ou CNPJ.

## blank=True

`blank=True` permite que um campo fique vazio em formularios.

Exemplo: email pode ser opcional, porque nem todo cliente vai informar email no primeiro cadastro.

## BooleanField

`BooleanField` guarda verdadeiro ou falso.

No campo `ativo`, ele permite marcar se um cliente esta ativo ou inativo.

Isso evita apagar registros importantes do banco.

## auto_now_add

`auto_now_add=True` preenche automaticamente a data e hora quando o registro e criado.

E util para campos como `criado_em`.

## auto_now

`auto_now=True` atualiza automaticamente a data e hora sempre que o registro e salvo.

E util para campos como `atualizado_em`.

## __str__

`__str__` define como um objeto aparece em textos, no admin do Django e em algumas listagens.

Para Cliente, faz sentido retornar o nome.

## Migration

Migration e uma instrucao que ensina o banco de dados a criar ou alterar tabelas.

Fluxo comum:

```powershell
python manage.py makemigrations
python manage.py migrate
```

`makemigrations` cria o arquivo de instrucao.

`migrate` aplica essa instrucao no banco.

## Status de migration

Podemos conferir migrations com:

```powershell
python manage.py showmigrations
```

Quando aparece `[ ]`, a migration existe, mas ainda nao foi aplicada.

Quando aparece `[X]`, a migration ja foi aplicada no banco.

## Git

Git e uma ferramenta de versionamento.

Ele permite registrar pontos importantes do projeto ao longo do tempo.

Um commit e como uma foto organizada do estado do codigo em determinado momento.

Fluxo basico:

```powershell
git status
git add .
git commit -m "mensagem do commit"
```

`git status` mostra o que mudou.

`git add` prepara arquivos para entrar no proximo commit.

`git commit` salva um ponto no historico do projeto.

## GitHub

GitHub e um lugar online para hospedar repositorios Git.

Git e a ferramenta de versionamento.

GitHub e o servico onde podemos guardar uma copia remota do repositorio.

Isso ajuda a proteger o projeto contra perda local e facilita trabalhar em outros computadores no futuro.

## Admin do Django

O admin do Django e um painel pronto para cadastrar, editar e consultar dados do sistema.

Ele e util no inicio do projeto porque permite testar models sem precisar criar telas proprias ainda.

Para um model aparecer no admin, ele precisa ser registrado em `admin.py`.

Exemplo:

```python
admin.site.register(Cliente)
```

## Superuser

Superuser e um usuario administrador do Django.

Ele tem permissao para acessar o painel `/admin/` e gerenciar os dados cadastrados.

Comando usado para criar:

```powershell
python manage.py createsuperuser
```

## ModelAdmin

`ModelAdmin` permite personalizar como um model aparece no admin do Django.

No app `clientes`, usamos isso para melhorar a lista de clientes com colunas, filtros e busca.

Exemplos de configuracao:

- `list_display`: define as colunas da lista.
- `list_filter`: cria filtros laterais.
- `search_fields`: define quais campos podem ser pesquisados.

## ModelForm no admin

`ModelForm` controla como um formulario ligado a um model aparece na tela.

No admin de clientes, usamos um formulario personalizado para mudar detalhes visuais do campo `documento`, sem mudar o nome do campo no banco.

Isso permitiu mostrar `CPF/CNPJ` para o usuario, mantendo `documento` no codigo.

## Placeholder

Placeholder e um texto discreto que aparece dentro de um campo vazio.

Ele serve como dica rapida para quem esta preenchendo.

No campo de documento, usamos:

```text
Somente numeros
```

Isso ajuda a lembrar que CPF e CNPJ devem ser digitados sem pontos, barras ou tracos.

## git diff

`git diff` mostra o que mudou nos arquivos antes do commit.

Ele ajuda a revisar as alteracoes e evitar salvar algo sem perceber.

Exemplo:

```powershell
git diff clientes/admin.py
```

## git push

`git push` envia commits locais para o repositorio remoto no GitHub.

Depois do push, outro computador pode receber essas mudancas usando `git pull`.
