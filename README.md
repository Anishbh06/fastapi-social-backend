## 🧠 Social Media Backend API (FastAPI)

A **production-grade backend API** for a social media platform built using **FastAPI**, implementing **JWT authentication**, **role-safe CRUD operations**, and **ownership-based access control**.

This project demonstrates **real-world backend engineering practices**, not tutorial-level code.

---

## 🚀 Features

### 🔐 Authentication & Security

* User registration and login
* JWT-based authentication
* Secure password hashing (Argon2)
* Protected routes using dependency injection
* Token validation and expiration handling

### 👤 User Management

* Create user accounts
* Fetch authenticated user profile (`/auth/me`)
* Passwords never exposed in responses

### 📝 Posts System

* Create posts (authenticated users only)
* Fetch all posts (pagination supported)
* Fetch only **my posts**
* Update posts (ownership enforced)
* Delete posts (ownership enforced)

### 🛡 Authorization Rules

* Users can **only modify or delete their own posts**
* Unauthorized access returns proper HTTP errors

---

## 🏗 Tech Stack

* **Backend Framework:** FastAPI
* **Language:** Python 3.11
* **ORM:** SQLAlchemy
* **Database:** SQL Server (via pyodbc)
* **Auth:** JWT (python-jose)
* **Password Hashing:** Argon2
* **Validation:** Pydantic v2
* **Server:** Uvicorn

---

## 📂 Project Structure

```text
app/
├── main.py               # App entry point & router registration
├── core/
│   ├── config.py         # Environment & settings
│   └── security.py       # JWT, hashing, auth logic
├── database/
│   ├── database.py       # DB connection & engine
│   └── deps.py           # DB dependency
├── models/
│   ├── user.py
│   └── post.py
├── schemas/
│   ├── user.py
│   ├── auth.py
│   └── post.py
├── crud/
│   ├── user.py
│   └── post.py
├── routers/
│   ├── auth.py
│   ├── user.py
│   └── post.py
└── __init__.py
```

---

## 🔑 Authentication Flow (High Level)

1. User logs in using `/auth/login`
2. Server issues a **JWT access token**
3. Client sends token in `Authorization: Bearer <token>`
4. `get_current_user` dependency:

   * Decodes JWT
   * Validates signature & expiry
   * Fetches user from database
5. Protected routes receive the authenticated user automatically

---

## 🧩 Ownership Enforcement

* Post ownership is enforced using the authenticated user ID
* Update/Delete operations verify:

  ```text
  post.owner_id == current_user.id
  ```
* Prevents horizontal privilege escalation

---

## ▶️ Running Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Anishbh06/fastapi-social-backend.git
cd fastapi-social-backend
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file:

```env
DB_SERVER=your_server
DB_NAME=your_db
DB_USERNAME=your_username
DB_PASSWORD=your_password
DB_DRIVER=ODBC Driver 17 for SQL Server

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5️⃣ Run the application

```bash
uvicorn app.main:app --reload
```

Open:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📌 API Highlights

| Method | Endpoint    | Description     | Auth |
| ------ | ----------- | --------------- | ---- |
| POST   | /users      | Register user   | ❌    |
| POST   | /auth/login | Login           | ❌    |
| GET    | /auth/me    | Current user    | ✅    |
| POST   | /posts      | Create post     | ✅    |
| GET    | /posts      | Get all posts   | ❌    |
| GET    | /posts/me   | Get my posts    | ✅    |
| PUT    | /posts/{id} | Update own post | ✅    |
| DELETE | /posts/{id} | Delete own post | ✅    |

---

## 🧪 Status

✅ Phase 1 Complete
🚧 Deployment (Docker + Cloud hosting) in progress

---

## 🧠 Why This Project Matters

This backend focuses on:

* Clean architecture
* Real-world authorization rules
* Secure authentication flows
* Scalable project structure

Built as a **portfolio-ready backend**, not a demo app.

---

## 👤 Author

**Anish**
Software Engineer

---
