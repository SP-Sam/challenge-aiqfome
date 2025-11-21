# Desafio técnico
Esta é uma API para um sistema de gerenciamento dos produtos favoritos dos clientes.

## ⚙️ Principais funcionalidades
* Gerenciamento de produtos favoritos
* Gerenciamento de clientes
* Autenticação e autorização

## 🛠️ Tecnologias utilizadas
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/stable/)
* [Postgres](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)

## 🌱 Executando o projeto localmente
### 1. Instale e configure o Docker na sua máquina
* [Docker Engine (Linux)](https://docs.docker.com/engine/install)
* [Docker Desktop (Mac)](https://docs.docker.com/desktop/setup/install/mac-install/)
* [Docker Desktop (Windows)](https://docs.docker.com/desktop/setup/install/windows-install/)

### 2. Instale um aplicativo para fazer as requisições e testar as rotas
Opções recomendadas:
* [Postman](https://www.postman.com/downloads/)
* [Insomnia](https://insomnia.rest/download)

### 3. Faça o clone do projeto
```bash
  git clone https://github.com/SP-Sam/challenge-aiqfome.git
```
Se você tem uma chave SSH configurada:
```bash
  git clone git@github.com:SP-Sam/challenge-aiqfome.git
```

### 4. Dentro da pasta do projeto, execute o seguinte comando:
```bash
  docker compose up --build
```
#### O resultado no terminal será parecido com o seguinte:
![img.png](assets/img.png)
### Pode começar a testar!


## Modelagem do banco de dados
![img_1.png](assets/img_1.png)
### Acesse [aqui](https://dbdiagram.io/d/er-aiqfome-challenge-691e7fb9228c5bbc1aa5a1a4) para ver os detalhes da modelagem


## 🚀 Endpoints
### `POST /auth/register` - Cadastrar um novo cliente
- Body da requisição
  ```json
  {
    "name": "Customer name",
    "email": "customer@email.com",
    "password": "customerpassword",
    "is_admin": false | true
  }
- Resposta esperada - status `201`
  ```json
  {
    "data": {
        "email": "customer@email.com",
        "id": 1,
        "is_admin": true,
        "name": "Customer name"
    },
    "message": "Cliente registrado com sucesso",
    "status": "SUCCESS"
  }
### `POST /auth/login` - Realizar login
- Body da requisição
  ```json
  {
    "email": "customer@email.com",
    "password": "customerpassword"
  }
- Resposta esperada - status `200`
  ```json
  {
    "data": {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjgsIm5hbWUiOiJDdXN0b21lciBuYW1lIiwiZW1haWwiOiJjdXN0b21lckBlbWFpbC5jb20iLCJpc19hZG1pbiI6dHJ1ZX0.rViMou4FldRscRNOYHDkI4Th1Cx8VWg_65jvlPzECwg"
    },
    "message": "Login realizado com sucesso",
    "status": "SUCCESS"
  }
---
### `GET /customers` - Buscar todos os clientes (admin)
- Necessário header `Authorization` com o token retornado no login
  ```curl
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjgsIm5hbWUiOiJDdXN0b21lciBuYW1lIiwiZW1haWwiOiJjdXN0b21lckBlbWFpbC5jb20iLCJpc19hZG1pbiI6dHJ1ZX0.rViMou4FldRscRNOYHDkI4Th1Cx8VWg_65jvlPzECwg"
- Resposta esperada - status `200`
  ```json
  {
    "data": [
        {
            "email": "customer@email.com",
            "id": 1,
            "is_admin": true,
            "name": "Customer name"
        },
        {
            "email": "customer2@email.com",
            "id": 2,
            "is_admin": false,
            "name": "Customer name 2"
        }...
    ],
    "message": "Clientes buscados com sucesso",
    "status": "SUCCESS"
  }
### `GET /customers/:id` - Buscar cliente específico (admin)
- Necessário header `Authorization` com o token retornado no login
  ```curl
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjgsIm5hbWUiOiJDdXN0b21lciBuYW1lIiwiZW1haWwiOiJjdXN0b21lckBlbWFpbC5jb20iLCJpc19hZG1pbiI6dHJ1ZX0.rViMou4FldRscRNOYHDkI4Th1Cx8VWg_65jvlPzECwg"
- Resposta esperada - status `200`
  ```json
  {
    "data": {
        "email": "customer@email.com",
        "id": 1,
        "is_admin": true,
        "name": "Customer name"
    },
    "message": "Cliente encontrado com sucesso",
    "status": "SUCCESS"
  }

### `PATCH /customers/:id` - Atualizar informações do cliente (admin)
- Necessário header `Authorization` com o token retornado no login
  ```curl
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjgsIm5hbWUiOiJDdXN0b21lciBuYW1lIiwiZW1haWwiOiJjdXN0b21lckBlbWFpbC5jb20iLCJpc19hZG1pbiI6dHJ1ZX0.rViMou4FldRscRNOYHDkI4Th1Cx8VWg_65jvlPzECwg"
- Body da requisição
  ```json
  {
    "name": "Novo nome", // opcional
    "email": "customer@email.com", // opcional
    "password": "customerpassword", // opcional
    "is_admin": true // opcional
  }
- Resposta esperada - status `200`
  ```json
  {
    "data": {
        "email": "customer@email.com",
        "id": 1,
        "is_admin": true,
        "name": "Novo nome"
    },
    "message": "Informações do cliente atualizadas com sucesso",
    "status": "SUCCESS"
  }

### `DELETE /customers/:id` - Remover cliente (admin)
- Necessário header `Authorization` com o token retornado no login
  ```curl
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjgsIm5hbWUiOiJDdXN0b21lciBuYW1lIiwiZW1haWwiOiJjdXN0b21lckBlbWFpbC5jb20iLCJpc19hZG1pbiI6dHJ1ZX0.rViMou4FldRscRNOYHDkI4Th1Cx8VWg_65jvlPzECwg"
- Resposta esperada - status `200`
  ```json
  {
    "message": "Cliente removido com sucesso",
    "status": "SUCCESS"
  }
---
### `POST /customer_products` - Favoritar produto
- Necessário header `Authorization` com o token retornado no login
  ```curl
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjgsIm5hbWUiOiJDdXN0b21lciBuYW1lIiwiZW1haWwiOiJjdXN0b21lckBlbWFpbC5jb20iLCJpc19hZG1pbiI6dHJ1ZX0.rViMou4FldRscRNOYHDkI4Th1Cx8VWg_65jvlPzECwg"
- Body da requisição
  ```json
  {
    "product_id": 10
  }
- Resposta esperada - status `200`
  ```json
  {
    "message": "Produto favoritado com sucesso",
    "status": "SUCCESS"
  }

### `GET /customer_products` - Buscar produtos favoritados
- Necessário header `Authorization` com o token retornado no login
  ```curl
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjgsIm5hbWUiOiJDdXN0b21lciBuYW1lIiwiZW1haWwiOiJjdXN0b21lckBlbWFpbC5jb20iLCJpc19hZG1pbiI6dHJ1ZX0.rViMou4FldRscRNOYHDkI4Th1Cx8VWg_65jvlPzECwg"
- Resposta esperada - status `200`
  ```json
  {
    "data": [
        {
            "created_at": "Fri, 21 Nov 2025 02:46:41 GMT",
            "id": 10,
            "image": "https://fakestoreapi.com/img/61U7T1koQqL._AC_SX679_t.png",
            "price": "109.00",
            "review": "2.9",
            "title": "SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s"
        },
        {
            "created_at": "Fri, 21 Nov 2025 02:47:28 GMT",
            "id": 15,
            "image": "https://fakestoreapi.com/img/51Y5NI-I5jL._AC_UX679_t.png",
            "price": "56.99",
            "review": "2.6",
            "title": "BIYLACLESEN Women's 3-in-1 Snowboard Jacket Winter Coats"
        }
    ],
    "message": "Produtos favoritos buscados com sucesso",
    "status": "SUCCESS"
  }

## 🖋️ Licença
Este projeto é um desafio técnico para um processo seletivo da [aiqfome](https://aiqfome.com/), não possui fins lucrativos e não está licenciado.

[⬆️ Voltar ao topo](#Desafio-técnico)
