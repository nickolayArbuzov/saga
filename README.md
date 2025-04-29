**Microservice-ready template** with **Saga pattern**, **Outbox & Inbox**, and **RabbitMQ** for async processing.

---

## 🚀 Features

- ⚙️ **Saga Pattern** for distributed transactions
- 📬 **Outbox / Inbox** patterns for reliable messaging
- 🐇 **RabbitMQ** as message broker
- 🐳 **Docker Compose** for easy local setup

---

## 🛠️ Tech Stack

- 🐍 Python / FastAPI
- 🐘 PostgreSQL
- 🐇 RabbitMQ
- 🛠️ SQLAlchemy (async)
- 🐳 Docker / docker-compose

---

## ▶️ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/nickolayArbuzov/saga.git
cd saga
```

### 2. Start the project

```bash
docker-compose up
```

## 🚀 What Will Be Launched

- 🐍 **FastAPI order-service** — [http://localhost:8001](http://localhost:8001)
- 🐍 **FastAPI payment-service** — [http://localhost:8002](http://localhost:8002)
- 🐍 **FastAPI delivery-service** — [http://localhost:8003](http://localhost:8003)
- 🐘 **PostgreSQL database** — accessible on port `5432`
- 🧭 **pgAdmin dashboard** — [http://localhost:5050](http://localhost:5050)
- 🐇 **RabbitMQ Broker** - 🖥 [http://localhost:15672](http://localhost:15672)

> 📌 **Make sure ports** `8001`, `8002`, `8003`, `5432`, `5050`, `5672`, and `15672` are available on your machine.

## 📘 API Documentation of entry-point order

- **Swagger UI** → [http://localhost:8001/docs](http://localhost:8001/docs)
- **ReDoc** → [http://localhost:8001/redoc](http://localhost:8001/redoc)

## 📘 API Documentation of webhook payment

- **Swagger UI** → [http://localhost:8002/docs](http://localhost:8002/docs)
- **ReDoc** → [http://localhost:8002/redoc](http://localhost:8002/redoc)

## 📘 API Documentation of webhook delivery

- **Swagger UI** → [http://localhost:8003/docs](http://localhost:8003/docs)
- **ReDoc** → [http://localhost:8003/redoc](http://localhost:8003/redoc)

---

## 🧮 pgAdmin Access

- **URL**: [http://localhost:5050](http://localhost:5050)

### 🔐 Default Credentials

| Field    | Value             |
| -------- | ----------------- |
| Email    | `admin@admin.com` |
| Password | `admin`           |

### ➕ How to Add a PostgreSQL Server in pgAdmin

1. Open pgAdmin in your browser: [http://localhost:5050](http://localhost:5050)
2. Click **"Add New Server"**
3. Go to the **"Connection"** tab and enter:

| Field     | Value             |
| --------- | ----------------- |
| Name      | `saga-postgres-1` |
| Host name | `db`              |
| Port      | `5432`            |
| Username  | `postgres`        |
| Password  | `postgres`        |

## 🐇 RabbitMQ Broker Managment Access

- **URL**: [http://localhost:15672](http://localhost:15672)

### 🔐 Default Credentials

| Field | Value   |
| ----- | ------- |
| User  | `guest` |
| Pass  | `guest` |

## 🧠 Architectural Patterns

### 📤 Outbox Pattern

Events are first **persisted in the database**, then **published asynchronously** by a background worker.  
This ensures **reliability** and **exact-once delivery**, even in case of failures.

---

### 📥 Inbox Pattern

Inbound messages are tracked using a unique `event_id`, enabling:

- **Idempotent processing**
- **Safe retries**
- **Deduplication of messages**

---

### 🔁 Saga Pattern

Implements **distributed transactions** through a series of coordinated **local operations**, each with an optional:

- **Compensating action** in case of failure
- **Rollback capability** to ensure eventual consistency
