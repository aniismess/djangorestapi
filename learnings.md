## 1. The Foundation: Setting Up the Workspace

The first step was to create a clean, isolated, and structured environment for our project.

    What we did:

        Virtual Environment (venv): We created and activated a virtual environment. This was the most critical first step. It acted like a clean, empty workshop, ensuring that the tools and libraries for this project (like a specific version of Django) wouldn't conflict with any other Python projects on your system.

        Installed Dependencies (pip): Inside this environment, we installed our core tools: django, djangorestframework, and their dependencies like dj-rest-auth and django-allauth.

        Project & App Scaffolding: We used django-admin startproject to create the main project skeleton (core) and python manage.py startapp to create the self-contained articles application.

    Why we did it: This separation is fundamental to professional software development. It ensures your project is reproducible and isolated. The project (core) handles the global configuration, while the app (articles) handles one specific feature, making the code organized and reusable.

## 2. The Blueprint: Models and the Database

With the structure in place, we needed to define what our data would look like.

    What we did:

        Defined the Model (models.py): We created the Article model as a Python class. This class acted as the single source of truth for our article data structure, defining fields like title (a CharField), content (a TextField), and most importantly, author (a ForeignKey to Django's built-in User model).

        Created Migrations (makemigrations): We ran the makemigrations command. This told Django to inspect our models.py file and generate a "blueprint" file—a Python script that described the SQL commands needed to build a database table matching our model.

        Applied Migrations (migrate): We ran the migrate command, which executed that blueprint, creating the actual articles_article table in our database.

    Why we did it: This two-step migration process allows you to treat your database schema like code. It's version-controlled, repeatable, and separates the definition of your data (the model) from the creation of the database structure (the migration).

## 3. The API Engine: Serializers, ViewSets, and URLs

This was the core of the API development, where we exposed our database to the outside world.

    What we did:

        Serializer (serializers.py): We created the ArticleSerializer. This class acted as our "universal translator." Its job was to convert the complex Python Article objects from our database into a simple, universal JSON format for responses, and to validate incoming JSON data on POST requests.

        ViewSet (views.py): We created the ArticleViewSet. This was the "brain" of the operation, containing the application logic. By inheriting from ModelViewSet, we instantly got all the standard CRUD (Create, Read, Update, Delete) logic without writing it ourselves.

        Router (urls.py): We used DRF's DefaultRouter to automatically connect our ArticleViewSet to the correct URLs (/api/articles/, /api/articles/{id}/, etc.).

    Why we did it: This separation of concerns is the power of DRF. The Model handles data structure, the Serializer handles data representation, and the ViewSet handles application logic. This makes the code incredibly clean and easy to maintain.

## 4. The Security Guard: Authentication & Permissions

With the API working, we locked it down to ensure it was secure.

    What we did:

        Token Authentication (dj-rest-auth): We integrated the dj-rest-auth and django-allauth libraries. This gave us pre-built, secure endpoints for user registration and login. Instead of relying on browser sessions, it allowed our API to be stateless, where users prove their identity on every request using a unique token.

        Custom Permissions (permissions.py): We wrote the IsAuthorOrReadOnly permission class. This was a crucial security refinement. It went beyond simply checking if a user was logged in and added a check to ensure that a user could only UPDATE or DELETE articles that they themselves had written (obj.author == request.user).

    Why we did it: Security is not an afterthought. By implementing token authentication, we made our API accessible to any kind of client (not just browsers). By adding object-level permissions, we enforced business logic and protected user data from unauthorized access, which is a requirement for any real-world application.

## 5. The Instruction Manual: API Documentation

The final step was to make our API usable for other developers (or our future selves).

    What we did:

        Installed drf-spectacular: We added this package to our project.

        Configured Settings & URLs: We updated settings.py to tell DRF to use drf-spectacular for schema generation and added the documentation URLs to our urls.py.

    Why we did it: drf-spectacular automatically inspected our code—the URLs, the ViewSet, and the Serializer—and generated a complete, interactive OpenAPI (Swagger) documentation page. This provides a professional, user-friendly guide to our API that stays up-to-date as our code changes, saving countless hours of manual documentation work.

## The Debugging Journey

Throughout this process, we encountered and solved several common errors:

    Syntax Errors: Simple typos like Class instead of class or missing commas in lists. These were solved by carefully reading the Python traceback.

    Configuration Errors: Forgetting to add apps to INSTALLED_APPS or middleware to MIDDLEWARE. The Django error pages were very explicit about how to fix these.

    Client-Side Errors: Incorrect curl commands (like http:/ instead of http://) or browser caching issues. This taught us to verify both the client's request and the server's response independently.
