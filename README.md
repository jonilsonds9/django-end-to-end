# Projeto cadastro de cliente do módulo Django

Este projeto é para criação de um sistema de gerenciamento de cadastro de clientes 
usando o Django.

## Guias

- **[Django: End-to-end parte 1](https://gitlab.com/jonilsonds9/django-end-to-end/-/snippets/2535545)**
- **[Django: End-to-end parte 2](https://gitlab.com/jonilsonds9/django-end-to-end/-/snippets/2538203)**
- **[Django: End-to-end parte 3](https://gitlab.com/jonilsonds9/django-end-to-end/-/snippets/2538213)**

## Primeiros passos

### Clone o projeto

Faça o clone do projeto para a sua máquina, se ainda não fez:
```shell
git clone https://github.com/jonilsonds9/django-end-to-end.git
```

### Criando ambiente virtual

Para não poluir todo o seu ambiente com várias dependências, você deve entrar na pasta do 
projeto no terminal:
```shell
cd django-end-to-end
```
E criar uma ambiente virtual usando o seguinte comando:
```shell
python -m venv venv
```
Em seguida ative o ambiente virtual recém-criado:
- No Linux/Mac use o seguinte comando:
```shell
source venv/bin/activate
```
- No Windows
```shell
venv\Scripts\activate
```

### Instalando dependências

Para tudo funcionar precisamos instalar as dependências (libs) entre elas o próprio django 
no nosso ambiente recém-criado, para isso use o seguinte comando:
```shell
pip install -r requirements.txt
```

### Configurando variáveis de ambiente

Todo projeto precisa de variáveis para funcionar, como nome do banco
de dados, porta de acesso ao banco de dados, hosts, qual ENV, e esse 
projeto não é diferente, e o correto é cada dev ter suas próprias 
variáveis de ambiente, por isso precisamos criar um arquivo na raiz
do projeto com o nome `.env`, você pode usar o arquivo `.env.example`
para fazer isso usando o comando:
```shell
cp .env.example .env
```
E alterar os valores das variáveis dentro do `.env` de acordo com 
seu ambiente.

Você pode usar a plataforma **[Neon tech](https://neon.tech/)** pro banco de dados postgres.

### Execute as migrations

Antes de tudo precisamos executar as migrations, para criarmos as 
tabelas no banco de dados, como já estamos com tudo configurado,
podemos apenas usar o comando:
```sh
python manage.py migrate
```

### Executando a aplicação

Por fim, você pode executar a aplicação com o seguinte comando:
```sh
python manage.py runserver
```
E ver o resultado em http://127.0.0.1:8000/.