# 🚀 Social Media Backend API (FastAPI)

A production-ready backend API for a social media application built using **FastAPI**.  
Implements secure authentication, ownership-based authorization, database migrations, Dockerized deployment, and cloud hosting.

This project is designed to reflect **real-world backend development practices**, not tutorial-level code.

---

## 🔥 Project Status

✅ Backend features complete  
✅ PostgreSQL integration  
✅ Alembic migrations created and applied  
✅ Dockerized and deployed  
✅ Tested via Swagger & live API calls  

**Project is complete and deployment-ready.**

---

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
🔑 Authentication Flow
User logs in using /auth/login

Server issues a JWT access token

Client sends token in Authorization: Bearer <token>

Token is validated and user is loaded via dependency injection

Protected routes automatically receive authenticated user

▶️ Running Locally (Without Docker)
1️⃣ Clone repository
git clone https://github.com/Anishbh06/fastapi-social-backend.git
cd fastapi-social-backend
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Configure environment variables
Create .env:

DATABASE_URL=postgresql://user:password@host:port/dbname
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
5️⃣ Run migrations
alembic upgrade head
6️⃣ Start server
uvicorn app.main:app --reload
Open Swagger UI:
http://127.0.0.1:8000/docs

🐳 Docker Usage
Build image
docker build -t fastapi-social-backend .
Run container
docker run -d -p 8000:8000 --env-file .env fastapi-social-backend
Apply migrations inside container
docker exec -it <container_name> alembic upgrade head
📌 API Endpoints
Method	Endpoint	Description	Auth
POST	/users	Register user	❌
POST	/auth/login	Login	❌
GET	/auth/me	Current user profile	✅
POST	/posts	Create post	✅
GET	/posts	Get all posts	❌
GET	/posts/me	Get my posts	✅
PUT	/posts/{id}	Update own post	✅
DELETE	/posts/{id}	Delete own post	✅
🧠 Why This Project Matters
This backend demonstrates:

Clean architecture

Secure authentication

Ownership-based authorization

Database migrations

Dockerized deployment

Cloud hosting readiness

Built as a portfolio-grade backend project.

👤 Author
Anish
Software Engineer
