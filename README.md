# Ecommerce API

A RESTful API for managing members, shops, and products, built with Python, FastAPI, and PostgreSQL.

## Features

### Authentication
- Member registration
- Member login
- Password hashing using Argon2

### Shops
- Create a shop using the member's phone number
- Retrieve all shops
- Retrieve a shop by ID
- Update shop information

### Products
- Create products for a shop
- Retrieve all products of a shop
- Retrieve a product by ID
- Update product information
- Delete products

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- Psycopg
- Pydantic
- Pydantic Settings
- pwdlib (Argon2)

## Project Structure

```text
ecommerce-api/
├── migrations/
├── tests/
├── scr/
│   ├── api/
│   │   ├── dependencies.py
│   │   └── endpoints/
│   │       └── v1/
│   │           └── router.py
│   ├── connections/
│   │   └── postgresql.py
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   ├── app.py
│   └── config.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd ecommerce-api
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate it on Windows:

```bash
.venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ecommerce_db
DB_USER=your_username
DB_PASSWORD=your_password
```

Replace the values with your PostgreSQL configuration.

Never commit your `.env` file or expose database credentials.

## Database

Create a PostgreSQL database named `ecommerce_db` and execute the database schema provided in the project's migrations.

The database contains three main tables:

- `members`
- `shops`
- `products`

## Run the Application

From the project root, run:

```bash
uvicorn scr.app:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

## API Documentation

Interactive API documentation is available through FastAPI:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

All endpoints use the `/api/v1` prefix.

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register a member |
| POST | `/auth/login` | Login a member |
| POST | `/shops` | Create a shop using a phone number |
| GET | `/shops` | Retrieve all shops |
| GET | `/shops/{shop_id}` | Retrieve a shop |
| PUT | `/shops/{shop_id}` | Update a shop |
| POST | `/shops/{shop_id}/products` | Create a product |
| GET | `/shops/{shop_id}/products` | Retrieve shop products |
| GET | `/products/{product_id}` | Retrieve a product |
| PUT | `/products/{product_id}` | Update a product |
| DELETE | `/products/{product_id}` | Delete a product |

## Notes

- Member passwords are stored as Argon2 hashes.
- Each member can have multiple shops.
- Each shop can contain multiple products.
- Shop creation uses the member's phone number to find their ID.
- Login currently validates credentials but does not issue access tokens.
- Token-based authentication and ownership authorization are not implemented in this version.