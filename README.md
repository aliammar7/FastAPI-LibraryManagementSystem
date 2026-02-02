# Library Management API

This is a **Library Management API** built with [FastAPI](https://fastapi.tiangolo.com/). It provides endpoints for managing users, books, and authentication.

## Features

- **User Management**: Create, update, delete, and retrieve user details.
- **Book Management**: Add, update, delete, and list books.
- **Authentication**: Secure login with JWT-based authentication.
- **Database Integration**: Uses PostgreSQL with SQLAlchemy ORM.

---

## Project Structure

```
app/
├── api/                # API routes
├── core/               # Core configurations and database setup
├── models/             # SQLAlchemy models
├── repositories/       # Database interaction logic
├── schemas/            # Pydantic schemas
├── services/           # Business logic
├── utils/              # Utility functions
├── main.py             # Application entry point
```

---

## Requirements

- Python 3.11+
- PostgreSQL database

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/library-management-api.git
   cd library-management-api
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the `.env` file:

   Create a `.env` file in the root directory with the following variables:

   ```env
   DATABASE_URL=postgresql+psycopg2://<username>:<password>@<host>:<port>/<database>
   SECRET_KEY=<your-secret-key>
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   PROJECT_NAME=Library Management API
   VERSION=1.0.0
   ```

---

## Running the Application

1. Start the FastAPI server:

   ```bash
   uvicorn app.main:app --reload
   ```

2. Access the API documentation:

   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Database Setup

Ensure your PostgreSQL database is running and the `DATABASE_URL` in the `.env` file is correctly configured. The database tables will be created automatically on application startup.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.