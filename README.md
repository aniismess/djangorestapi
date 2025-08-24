# Personal Blogging Platform API

Hey there! This is a complete, token-authenticated RESTful API that can power any personal blog you can dream up. It's got all the backend stuff you need to get a modern blog application off the ground.

---

## What's Inside?

- **All the Basics are Covered!** You can create, read, update, and delete articles (the full CRUD experience!).
- **Secure Logins:** It's got a secure login system using tokens, so it's ready for any kind of app, not just a website.
- **Smart Permissions:** Users can only mess with their own articles, which is how it should be! Anyone can read posts, though.
- **Awesome Auto-Docs:** Comes with slick, auto-generated documentation, so you'll know exactly how everything works without digging through code.
- **Clean & Organized Code:** The project is structured nicely, making it easy to understand and build on.

---

## The Tech Stack

-   **Backend:** Python, Django, Django REST Framework
-   **Database:** SQLite3 (but you can swap it out for something else!)
-   **Authentication:** `dj-rest-auth`, `django-allauth`
-   **API Documentation:** `drf-spectacular` (OpenAPI 3)

---

## Getting Started

Ready to get this thing running on your machine? Here’s how you do it!

### What You'll Need

-   Python 3.10 or newer
-   `pip` and `venv` (usually come with Python)

### Installation Steps

1.  **First, grab the code:**

    ```bash
    git clone https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY_NAME>.git
    cd <YOUR_REPOSITORY_NAME>
    ```

2.  **Set up a clean workspace:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install all the necessary packages:**

    ```bash
    pip install -r requirements.txt
    ```

    > **Note:** You'll need to create a `requirements.txt` file first. Just run:
    >
    > ```bash
    > pip freeze > requirements.txt
    > ```

4.  **Get the database ready:**

    ```bash
    python manage.py migrate
    ```

5.  **Make an admin account for yourself:**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Fire it up:**

    ```bash
    python manage.py runserver
    ```

Your API should now be live and kicking at `http://127.0.0.1:8000`

---

## How to Use the API

Time for the fun part! You can play with the API using a tool like Postman or just good old `curl` right from your terminal.

### Authentication

-   **Sign up a new user:**

    ```bash
    curl -X POST \
      -H "Content-Type: application/json" \
      -d '{"username": "testuser", "email": "test@example.com", "password": "a-strong-password123", "password2": "a-strong-password123"}' \
      http://127.0.0.1:8000/api/auth/registration/
    ```

-   **Log in to get your token:**

    ```bash
    curl -X POST \
      -H "Content-Type: application/json" \
      -d '{"username": "testuser", "password": "a-strong-password123"}' \
      http://127.0.0.1:8000/api/auth/login/
    ```

    > The response will give you a `key`. Copy that for the next steps!

### Articles (The Main Event)

Just replace `<YOUR_TOKEN_HERE>` with the key you copied.

-   **Create a new article:**

    ```bash
    curl -X POST \
      -H "Content-Type: application/json" \
      -H "Authorization: Token <YOUR_TOKEN_HERE>" \
      -d '{"title": "My First Post", "content": "This is the content of my first post."}' \
      http://127.0.0.1:8000/api/articles/
    ```

-   **See all articles** (no login needed):

    ```bash
    curl -X GET http://127.0.0.1:8000/api/articles/
    ```

-   **Grab a specific article** (no login needed):

    ```bash
    curl -X GET http://127.0.0.1:8000/api/articles/1/
    ```

-   **Update one of your articles:**

    ```bash
    curl -X PUT \
      -H "Content-Type: application/json" \
      -H "Authorization: Token <YOUR_TOKEN_HERE>" \
      -d '{"title": "My Updated Title", "content": "This is the updated content."}' \
      http://127.0.0.1:8000/api/articles/1/
    ```

-   **Delete one of your articles:**

    ```bash
    curl -X DELETE \
      -H "Authorization: Token <YOUR_TOKEN_HERE>" \
      http://127.0.0.1:8000/api/articles/1/
    ```

---

## API Documentation

Tired of guessing what an API does? This project builds its own docs! Once the server is running, you can check them out here:

-   [Swagger UI](http://127.0.0.1:8000/api/schema/swagger-ui/)
-   [ReDoc](http://127.0.0.1:8000/api/schema/redoc/)
