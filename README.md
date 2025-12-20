# NexoLetter 📧

NexoLetter is a professional-grade, asynchronous newsletter management system built with **FastAPI**, **SQLAlchemy 2.0**, and **Pydantic v2**.  
It is designed with scalability, clean architecture, and modern Python best practices in mind.

## 🏗️ Project Structure

```text
NexoLetter/
|-- app/
│   |-- api/
│   │   |-- v1/             # API versioning logic
│   │       |-- endpoints/  # Route logic (users, newsletters, etc.)
│   │       |-- api.py      # V1 router aggregator
│   |-- core/               # Configuration, database, security
│   |-- models/             # SQLAlchemy ORM models
│   |-- schemas/            # Pydantic v2 schemas
|   |-- services/           # Application logic
|   |-- utils/              # Common utilities
│   |-- main.py             # FastAPI application entry point
|-- tests/                  # Pytest test suite
|-- requirements.txt        # List of Python Packages
|-- .env.template           # Environment variables (template)
|-- .gitignore              # Git ignore rules
|-- README.md
```

## 🚀 Quick Start

### 1. Prerequisites

- Python **3.10+**
- pip or pipx
- (Optional) virtualenv or venv

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/TharunNo1/NexoLetter.git
cd NexoLetter

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
# .venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the project root:

```env
# Database settings
DB__DATABASE_URL="sqlite:///./nexoletter.db"
DB__ECHO=True

# API settings
PROJECT_NAME="NexoLetter"
API_V1_STR="/api/v1"
```

### 4. Run the Application

```bash
uvicorn app.main:app --reload
```

Once running, the API will be available at:

- http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 🧪 Testing

```bash
pytest
```

## 🧠 Design Principles

- Async-first API design
- Explicit versioning for long-term stability
- Strict data validation with Pydantic v2
- Separation of concerns (API, core, models, schemas)
- Production-ready structure from day one

## 📌 Notes

- The `.env` file is intentionally excluded from version control.
- SQLite is used by default for local development; switching to PostgreSQL or MySQL only requires a connection string change.
- The architecture supports background jobs, email providers, and queue systems.
