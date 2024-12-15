# Vehicle Marketplace API

A **FastAPI-based backend application** for managing vehicle ads. This application allows users to create, update, and view vehicle listings. Below are the instructions to set up and run the project locally.

---

## Features

- User registration and authentication.
- Vehicle ad creation, update, and deletion.
- Search and filter vehicles by various criteria.
- Secure password hashing and JWT-based authentication.

---

## Requirements

Ensure you have the following installed on your system:

- Python 3.10+
- PostgreSQL
- Git
- Virtual Environment (optional but recommended)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/vehicle-marketplace.git
cd vehicle-marketplace
```
### 2.  Create a Virtual Environment
Create and activate a virtual environment:

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3.  Install Dependencies
Install required Python packages:
```bash
pip install -r requirements.txt
```

### 4.   Configure Environment Variables
Create a .env file in the root directory of the project and add the following:
```bash
DATABASE_URL=postgresql://<username>:<password>@localhost/vehicle-market
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
Replace <username> and <password> with your PostgreSQL credentials.

### 5.   Initialize the Database
1. Create a PostgreSQL database named vehicle-market (or the name you used in the .env file).
2. Run Alembic migrations to set up the database schema:
```bash
alembic upgrade head
```

### 6.   Start the Application
Run the FastAPI application:
```bash
uvicorn app.main:app --reload
```
The application will be available at http://127.0.0.1:8000.

### 7.   Access the API Documentation
Visit the interactive API documentation at:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc






