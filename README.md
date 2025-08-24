Personal Blogging Platform API

A complete, token-authenticated RESTful API for a personal blogging platform built with Django and Django REST Framework. This project provides all the backend services required to power a modern blog application.
Features

    Full CRUD Operations: Create, Read, Update, and Delete articles.

    Token-Based Authentication: Secure user registration and login system using dj-rest-auth for stateless authentication.

    Object-Level Permissions: Users can only edit or delete their own articles, but anyone can read any article.

    Auto-Generated API Documentation: Interactive API documentation powered by drf-spectacular, providing a live Swagger/OpenAPI interface.

    Structured & Organized: Built with a clear separation between the Django project (core) and the main application (articles).

Tech Stack

    Backend: Python, Django, Django REST Framework

    Database: SQLite3 (default, configurable)

    Authentication: dj-rest-auth, django-allauth

    API Documentation: drf-spectacular (OpenAPI 3)

Setup and Installation

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
Prerequisites

    Python 3.10+

    pip and venv

Installation Steps

    Clone the repository:

    git clone [https://github.com/](https://github.com/)<YOUR_USERNAME>/<YOUR_REPOSITORY_NAME>.git
    cd <YOUR_REPOSITORY_NAME>

    Create and activate a virtual environment:

    python -m venv venv
    source venv/bin/activate

    Install the required dependencies:

    pip install -r requirements.txt

    (Note: You will need to create a requirements.txt file. You can do this by running pip freeze > requirements.txt in your current project.)

    Apply the database migrations:

    python manage.py migrate

    Create a superuser to access the admin panel:

    python manage.py createsuperuser

    Run the development server:

    python manage.py runserver

    The API will now be running at http://127.0.0.1:8000.

API Usage & Endpoints

You can interact with the API using any API client like Postman or a command-line tool like curl.
Authentication

1. Register a new user:

curl -X POST \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "email": "test@example.com", "password": "a-strong-password123", "password2": "a-strong-password123"}' \
[http://127.0.0.1:8000/api/auth/registration/](http://127.0.0.1:8000/api/auth/registration/)

2. Log in to get an auth token:

curl -X POST \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "a-strong-password123"}' \
[http://127.0.0.1:8000/api/auth/login/](http://127.0.0.1:8000/api/auth/login/)

    The response will contain your token key. Copy it for the next steps.

Articles (CRUD)

Replace <YOUR_TOKEN_HERE> with the key you received from the login step.

1. Create a new article:

curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Token <YOUR_TOKEN_HERE>" \
-d '{"title": "My First Post", "content": "This is the content of my first post."}' \
[http://127.0.0.1:8000/api/articles/](http://127.0.0.1:8000/api/articles/)

2. List all articles (no auth required):

curl -X GET [http://127.0.0.1:8000/api/articles/](http://127.0.0.1:8000/api/articles/)

3. Retrieve a single article (no auth required):

curl -X GET [http://127.0.0.1:8000/api/articles/1/](http://127.0.0.1:8000/api/articles/1/)

4. Update an article (must be the author):

curl -X PUT \
-H "Content-Type: application/json" \
-H "Authorization: Token <YOUR_TOKEN_HERE>" \
-d '{"title": "My Updated Title", "content": "This is the updated content."}' \
[http://127.0.0.1:8000/api/articles/1/](http://127.0.0.1:8000/api/articles/1/)

5. Delete an article (must be the author):

curl -X DELETE \
-H "Authorization: Token <YOUR_TOKEN_HERE>" \
[http://127.0.0.1:8000/api/articles/1/](http://127.0.0.1:8000/api/articles/1/)

API Documentation

This project includes auto-generated, interactive API documentation. Once the server is running, you can access it at the following URLs:

    Swagger UI: http://127.0.0.1:8000/api/schema/swagger-ui/

    ReDoc: http://127.0.0.1:8000/api/schema/redoc/

You can use these interfaces to explore and test all the API endpoints directly from your browser.
