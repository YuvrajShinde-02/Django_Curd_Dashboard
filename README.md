# Django CRUD API with Visualization (Assignment)

This project is a Django-based web application that provides:
- **CRUD APIs** for managing `Lead` records
- **Integration with a third-party API** (JSONPlaceholder)
- **Data visualization dashboard** using Chart.js
- **PostgreSQL database backend**

---

## 🚀 Features
- **CRUD Endpoints**
  - Create, Read, Update, Delete leads at `/api/leads/`
- **Third-party API Integration**
  - Import sample users from JSONPlaceholder into database
  - Endpoint: `/api/leads/import_from_jsonplaceholder/`
- **Visualization Dashboard**
  - View daily lead creation trends at `/`
- **Admin Panel**
  - Manage leads at `/admin/`

---

## 🛠️ Tech Stack
- Python 3.12+
- Django 5.x
- Django REST Framework (DRF)
- PostgreSQL
- Chart.js

---

## ⚙️ Setup Instructions

### 1. Clone the repository
    git clone https://github.com/<your-username>/django-crud-api-dashboard.git
    cd django-crud-api-dashboard


### 2. Create a virtual environment
    python -m venv venv
    source venv/bin/activate   # On Linux/Mac
    venv\Scripts\activate      # On Windows

### 3. Install dependencies
    pip install -r requirements.txt

### 4. Configure PostgreSQL

    Ensure PostgreSQL is installed and running.

    Create a database and user:

    CREATE DATABASE leads_db;
    CREATE USER lead_user WITH PASSWORD 'lead_pass';
    ALTER ROLE lead_user SET client_encoding TO 'utf8';
    ALTER ROLE lead_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE lead_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE leads_db TO lead_user;


    Update settings.py (already configured for PostgreSQL in this project)

### 5. Apply migrations
    python manage.py makemigrations
    python manage.py migrate

### 6. Create superuser (optional, for admin panel)
    python manage.py createsuperuser

### 7. Run the server
    python manage.py runserver

### 8. API Endpoints
    CRUD Operations

    GET /api/leads/ → List all leads

    POST /api/leads/ → Create new lead

    GET /api/leads/{id}/ → Get a single lead

    PUT /api/leads/{id}/ → Update a lead

    PATCH /api/leads/{id}/ → Partially update a lead

    DELETE /api/leads/{id}/ → Delete a lead

### Third-party API Import
    POST /api/leads/import_from_jsonplaceholder/

Fetches sample users from JSONPlaceholder and adds them as leads.
### Visualization
    GET /api/leads/metrics_by_day/ → Returns lead counts grouped by day.