# 🚀 Social Media Backend API (FastAPI)

A production-ready backend API for a social media application built using **FastAPI**.  
Implements secure authentication, ownership-based authorization, database migrations, Dockerized deployment, and cloud hosting.

This project is designed to reflect **real-world backend development practices**.

---

## 🔥 Project Status

✅ Backend features complete  
✅ PostgreSQL integration  
✅ Alembic migrations created and applied  
✅ Dockerized and deployed  
✅ Tested via Swagger & live API calls  
✅ Ownership-based authorization enforced


**Project is complete and deployed.**

## 🌐 Live API Documentation

Swagger UI (Live):
👉 https://fastapi-social-backend-ivjy.onrender.com/docs

The API is fully deployed and publicly accessible.  
All endpoints can be tested directly via the live Swagger interface.

---

## Live Demo
Watch a short demo: https://www.loom.com/share/88107d4d032047a78b65e2ef4b7ddc4a

## Live API Testing (Postman)

Public Postman collection:
👉 https://www.postman.com/technical-participant-84645882/social-media-backend-fastapi/collection/40622863-8a748c04-e1bf-4410-a82e-10ad5700c67d/

### How to use
1. Open the Postman link above
2. Click **Run in Postman** or **Fork Collection**
3. Set environment variable:
   - `url = http://127.0.0.1:8000`
4. Run **Login** API (JWT token is auto-saved)
5. Test authenticated endpoints (Create Post, Get Posts, Update/Delete)

## 🛠 Features

### 🔐 Authentication & Security
- User registration and login
- JWT-based authentication
- Secure password hashing (Argon2)
- Token expiration handling
- Protected routes via dependency injection

### 👤 User Management
- Create user accounts
- Fetch authenticated user profile (`/auth/me`)
- Passwords never exposed in API responses

### 📝 Posts System
- Create posts (authenticated users only)
- Fetch all posts
- Fetch only logged-in user’s posts
- Update posts (ownership enforced)
- Delete posts (ownership enforced)

### 🛡 Authorization Rules
- Users can only update or delete **their own posts**
- Unauthorized actions return proper HTTP errors

---

## 🏗 Tech Stack

- **Backend:** FastAPI (Python 3.11)
- **ORM:** SQLAlchemy
- **Database:** PostgreSQL
- **Migrations:** Alembic
- **Authentication:** JWT (python-jose)
- **Password Hashing:** Argon2
- **Validation:** Pydantic v2
- **Server:** Uvicorn
- **Containerization:** Docker

---

# ⚡ 5-Minute Local Setup (Docker Recommended)

This project is fully Dockerized and can be run locally without installing PostgreSQL.

## 🚀 Quick Start (Recommended)

```bash
git clone https://github.com/Anishbh06/fastapi-social-backend.git
cd fastapi-social-backend
cp .env.example .env
docker-compose up --build
````
---
## 📂 Project Structure

```text
app/
├── main.py               # App entry point
├── core/
│   ├── config.py         # Environment & settings
│   └── security.py       # Auth & hashing logic
├── database/
│   ├── database.py       # SQLAlchemy engine & session
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
└── alembic/              # Database migrations
````

## 🔑 Authentication Flow

1. User logs in using `/auth/login`
2. Server issues a JWT access token
3. Client sends the token in the request header:

```http
Authorization: Bearer <token>
```

4. Token is validated and the user is loaded via dependency injection
5. Protected routes automatically receive the authenticated user


## ▶️ Running Locally (Without Docker)

### 1️⃣ Clone repository

```bash
git clone https://github.com/Anishbh06/fastapi-social-backend.git
cd fastapi-social-backend
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://user:password@host:port/dbname
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5️⃣ Run database migrations

```bash
alembic upgrade head
```

### 6️⃣ Start the server

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🐳 Docker Usage

### Build image

```bash
docker build -t fastapi-social-backend .
```

### Run container

```bash
docker run -d -p 8000:8000 --env-file .env fastapi-social-backend
```

### Apply migrations inside container

```bash
docker exec -it <container_name> alembic upgrade head
```

---

## 📌 API Endpoints

| Method | Endpoint      | Description          | Auth |
| ------ | ------------- | -------------------- | ---- |
| POST   | `/users`      | Register user        | ❌    |
| POST   | `/auth/login` | Login                | ❌    |
| GET    | `/auth/me`    | Current user profile | ✅    |
| POST   | `/posts`      | Create post          | ✅    |
| GET    | `/posts`      | Get all posts        | ❌    |
| GET    | `/posts/me`   | Get my posts         | ✅    |
| PUT    | `/posts/{id}` | Update own post      | ✅    |
| DELETE | `/posts/{id}` | Delete own post      | ✅    |

---

## 🧠 Why This Project Matters

This backend demonstrates:

* Clean architecture
* Secure authentication
* Ownership-based authorization
* Database migrations using Alembic
* Dockerized deployment
* Cloud hosting readiness

Built as a portfolio-grade backend project.

---

## 👤 Author

**Anish**
Software Engineer


