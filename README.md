# Bethany Website

A modern business website built with Django.

## Setup Instructions

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Linux/Mac: `source .venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```
8. Visit http://127.0.0.1:8000 in your browser

## Features

- Modern responsive design
- User authentication (login/register)
- Portfolio showcase
- Service details
- Contact form
- Admin interface

## Project Structure

- `config/` - Django project settings
- `core/` - Main application
- `templates/` - HTML templates
- `assets/` - Static files (CSS, JS, images)
- `media/` - User-uploaded files
