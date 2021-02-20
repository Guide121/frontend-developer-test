# Simulador para servir avaliações para a aplicação

Aplicação feita com Flask e Python.

Possui apenas uma rota com duas funções principais: criar avaliações aleatórias, adicionando essas avaliações em um arquivo csv e retornar essas avaliações.
Para gerar os comentários, foi utilizado a lib Faker, que fornece dados fake, apenas para mockar.

## Como instalar e rodar

Para instalar, é necessário abrir um terminal na pasta deste projeto e criar um ambiente virtual e ativar este ambiente, com:

```
python -m venv venv
source venv/bin/activate
```

Então, é necessário instalar as dependências, pelo pip:

```
pip install -r requirements.txt
```

Para rodar, basta dar o seguinte comando:

```
flask run
```

E então, a aplicação estará rodando em [localhost:5000](http://localhostt:5000)
