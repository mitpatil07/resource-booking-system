# 📦 Resource Booking System

A simple Django-based web application that allows users to view, book, and manage limited-quantity resources.

---

## 🚀 Features

- JWT authentication (SimpleJWT)
- RESTful APIs for:
  - Listing resources
  - Booking a resource
  - Viewing user's bookings
- Bootstrap-powered frontend
- Admin panel for resource/user management
- PostgreSQL database
- Dockerized for deployment
- Unit tests with coverage

---

## 🛠️ Tech Stack

- **Backend**: Django, DRF
- **Frontend**: Bootstrap (Django templates)
- **Database**: PostgreSQL
- **Auth**: JWT (SimpleJWT)
- **DevOps**: Docker, Docker Compose

---

## 📁 Folder Structure

```
resource_booking/
├── bookings/                
│   ├── migrations/
│   ├── templates/bookings/
│   │   └── index.html
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── booking_system/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Local Setup

1. Clone the repository:
```bash
git clone https://github.com/mitpatil07/resource_booking.git
cd resource_booking
```

2. Create a virtual environment:
```bash
python -m venv env
env\Scripts\activate      # Windows
# or
source env/bin/activate     # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Setup PostgreSQL and `.env` or environment variables.

5. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the server:
```bash
python manage.py runserver
```

---

## 🐳 Docker Setup

1. Run with Docker Compose:
```bash
docker-compose up --build
```

2. Access:
- Admin: http://localhost:8000/admin/
- Frontend: http://localhost:8000/

---

## 🔑 API Endpoints

| Method | Endpoint             | Description                        |
|--------|----------------------|------------------------------------|
| POST   | `/api/token/`        | Get JWT access and refresh tokens  |
| POST   | `/api/token/refresh/`| Refresh JWT token                  |
| GET    | `/api/resources/`    | List all resources                 |
| POST   | `/api/resources/`    | Add new resource (auth required)   |
| POST   | `/api/book/`         | Book a resource (auth required)    |
| GET    | `/api/mybookings/`   | Get user's bookings (auth required)|

---

## 🧪 Run Tests

```bash
python manage.py test bookings
```
