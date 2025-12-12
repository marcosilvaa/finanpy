# QWEN.md - Finanpy Project Context

## Project Overview

**Finanpy** is a full-stack web system built with **Django** and frontend using **Django Template Language (DTL)** styled with **Tailwind CSS**. It's designed for **personal finance management**, offering a modern, responsive interface with a dark theme. The project prioritizes simplicity, usability, and adherence to Django best practices while avoiding over-engineering.

The application allows authenticated users to register, view, and categorize their financial transactions (income and expenses) organized by customizable categories. It provides a dashboard with financial summary, transaction history, and essential metrics. Authentication occurs via email (not username), with the entire interface in Brazilian Portuguese, while the code is in English.

## Project Structure

```
finanpy/
├── .git/
├── .venv/
├── accounts/           # Authentication and user management app
├── categories/         # Transaction categories management
├── core/              # Core Django project (settings, urls, etc.)
├── profiles/          # User profiles information
├── transactions/      # Financial transactions CRUD
├── users/             # User model extensions
├── .gitignore
├── .python-version
├── db.sqlite3
├── main.py
├── manage.py
├── pyproject.toml
├── README.md
├── requirements.txt
├── uv.lock
└── docs/              # Project documentation
```

## Technologies and Stack

- **Backend**: Python 3.13+, Django 5+
- **Frontend**: Django Template Language + Tailwind CSS (via CDN)
- **Database**: SQLite (default Django)
- **Authentication**: Django Built-in (customized for email-based login)
- **Package Manager**: uv (with pip fallback)

## Key Features (Planned/Implemented)

Based on the Product Requirements Document (PRD.md):

- ✅ Email-based user registration and login
- ✅ Dashboard with financial summary
- ✅ Transaction registration (amount, type, category, date)
- ✅ Customizable categories for transactions
- ✅ Transaction history with filtering
- ✅ Dark-themed, responsive interface
- ✅ Modular app architecture

## Project Configuration

### Settings
- Language: English (en-us) - *Note: Will need to be changed to pt-br according to PRD*
- Timezone: UTC - *Note: Will need to be changed to America/Sao_Paulo according to PRD*
- Database: SQLite (`db.sqlite3`)
- Static files: Standard Django static files handling

### Apps
- `django.contrib.admin` - Django admin interface
- `django.contrib.auth` - Authentication system
- `django.contrib.contenttypes` - Content types framework
- `django.contrib.sessions` - Session framework
- `django.contrib.messages` - Message framework
- `django.contrib.staticfiles` - Static files management
- `accounts` - Custom user authentication
- `categories` - Transaction categorization
- `transactions` - Transaction management
- `profiles` - User profile features
- `users` - User-related features

## Building and Running

### Prerequisites
- Python 3.13 or higher
- pip package manager
- Git

### Setup Instructions

1. **Clone the repository** (if applicable)
2. **Create virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Linux/Mac
   # or
   .venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`.

## Development Conventions

### Code Style
- Python code follows PEP8
- Code is written in English (variables, functions, comments)
- UI/UX elements are in Brazilian Portuguese

### Architecture
- Modular Django apps following domain-driven design
- Class-Based Views (CBVs) preferred for Django views
- Clean separation between models, views, templates, and forms
- Authentication using Django's built-in system customized for email login

### Database Schema
Based on the ERD in the PRD, the system will include:
- User model (customized for email login)
- Profile model
- Account model
- Category model
- Transaction model

## Development Status

The project is currently in the early stages of development based on the PRD document. Key components like:
- Custom user model with email authentication
- Authentication forms/views
- Template structure with Tailwind CSS
- Core models for transactions and categories

Most are planned according to the sprint plan in the PRD but may not be fully implemented yet.

## Documentation

Comprehensive documentation is available in the `docs/` directory with:
- Product overview
- Technical architecture
- Development guidelines
- Design system
- Folder structure
- Setup guide
- User stories