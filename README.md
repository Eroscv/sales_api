# 🚀 Sales API — FastAPI + SQLite + MongoDB

API backend desenvolvida em **Python + FastAPI** para ingestão, armazenamento e consulta de dados de vendas, utilizando **SQLite** para dados estruturados e **MongoDB** para textos associados às vendas.

Este projeto atende aos requisitos do desafio técnico, incluindo CRUD completo, busca textual, agregações analíticas e documentação clara.
⚠️ IMPORTANTE: Este projeto é configurado para EXECUÇÃO LOCAL
---

## 📌 Visão Geral da Solução

A aplicação permite:

* Cadastro, consulta, atualização e exclusão de vendas (SQLite)
* Armazenamento de comentários e textos relacionados às vendas (MongoDB)
* Busca textual por termos em documentos
* Consulta analítica (faturamento, vendas por categoria, ticket médio)
* Integração entre dados relacionais e documentos NoSQL
* Documentação automática via Swagger

---

## 🧠 Arquitetura

| Camada           | Tecnologia        |
| ---------------- | ----------------- |
| API              | FastAPI           |
| Banco relacional | SQLite            |
| Banco NoSQL      | MongoDB           |
| ORM              | SQLAlchemy        |
| Documentação     | Swagger / Postman |

---

## 📂 Estrutura do Projeto

```
project/
│
├── core/               # Conexão SQLite
├── models/             # Modelos SQLAlchemy
├── schemas/            # Validações Pydantic
├── services/           # Regras de negócio
├── routes/             # Endpoints FastAPI
├── mongo/              # Cliente MongoDB
├── main.py             # Inicialização da API
├── requirements.txt    # Dependências
└── README.md           # Documentação
```

---

## 🗄️ Modelo Relacional (SQLite)

Campos principais da venda:

| Campo        | Tipo   |
| ------------ | ------ |
| id           | int    |
| product_name | string |
| category     | string |
| quantity     | int    |
| unit_price   | float  |
| sale_date    | date   |

---

## 🍃 Modelo NoSQL (MongoDB)

Exemplo de documento:

```json
{
  "sale_id": 1,
  "text": "Cliente elogiou o atendimento"
}
```

---

## ⚙️ Pré-requisitos

* Python 3.10+
* MongoDB local ou MongoDB Atlas
* Git (opcional)
* Postman (para testes)

---

## ▶️ Como Executar o Projeto Localmente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/Eroscv/sales-api.git
cd sales-api
```

---

### 2️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

#### Ativar

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configurar MongoDB

#### Local

```python
MongoClient("mongodb://localhost:27017")
```

#### MongoDB Atlas

```python
MongoClient("mongodb+srv://USER:PASSWORD@cluster.mongodb.net/")
```

Arquivo: `mongo/mongo_client.py`

---

### 5️⃣ Executar a API

```bash
uvicorn main:app --reload
```

A API ficará disponível em:

```
http://127.0.0.1:8000
```

---

## 📘 Documentação Swagger

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Endpoints Principais

### 📌 CRUD Vendas (SQLite)

| Método | Rota        | Descrição       |
| ------ | ----------- | --------------- |
| POST   | /sales/     | Criar venda     |
| GET    | /sales/     | Listar vendas   |
| GET    | /sales/{id} | Buscar venda    |
| PUT    | /sales/{id} | Atualizar venda |
| DELETE | /sales/{id} | Excluir venda   |

---

### 📌 Textos MongoDB

| Método | Rota          | Descrição     |
| ------ | ------------- | ------------- |
| POST   | /texts/       | Inserir texto |
| GET    | /texts/search | Buscar texto  |

---

### 📌 Analytics

| Método | Rota                        | Descrição                         |
| ------ | --------------------------- | --------------------------------- |
| GET    | /analytics/sales-with-texts | Retorna vendas + textos           |
| GET    | /analytics/search-sales     | Busca textual com dados completos |

---

## 🧪 Testes no Postman

Coleção pronta disponível:

📥 `colecao_endpoints.json`

Importar no Postman → Executar requests

---

## 🧠 Decisões Técnicas

* SQLite escolhido por simplicidade local
* MongoDB usado para dados textuais não estruturados
* FastAPI para alta performance e documentação automática
* Arquitetura modular para escalabilidade

---

## 🎯 Status do Projeto

✅ CRUD completo
✅ SQLite estruturado
✅ MongoDB textual
✅ Busca avançada
✅ Analytics
✅ Postman
✅ Swagger
✅ Pronto para entrega técnica

---

## 👨‍💻 Autor

**Eros Cesar**

Projeto desenvolvido para desafio técnico backend.

---
