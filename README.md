# Backend Python

This repository contains a collection of projects and exercises focusing on advanced Python programming, Django backend development, API testing, and DevOps integration. The curriculum progresses from core Python concepts to building and deploying robust RESTful APIs.

## 📂 Repository Structure

### 🚀 Core Application

**`messaging_app/`**
A full-featured Django REST Framework application handling real-time messaging.

- **CI/CD:** Includes `Jenkinsfile` for automated pipelines.
- **API Docs:** Postman collections included for endpoint testing.
- **Database:** SQLite configuration with optimized models.

### 🧪 Testing & QA

**`0x03-Unittests_and_integration_tests/`**
Focuses on testing methodologies using `unittest` and `unittest.mock`.

- `test_client.py` & `test_integration.py`: Implementation of mock objects and integration suites.
- `fixtures.py`: Data seeding for consistent test environments.

### ⚙️ Django Internals

**`Django-Middleware-0x03/`**
Custom middleware implementation for request processing.

- Request logging (`requests.log`) and performance monitoring.
- Custom handling of request/response cycles.

**`Django-signals_orm-0x04/`**
Advanced database operations and event-driven architecture.

- **Signals:** pre_save/post_save triggers for automated actions.
- **ORM:** Optimized queries and database interactions within the `messaging` module.

### 🐍 Advanced Python

- **`python-decorators-0x01/`**: Deep dive into functional programming patterns, closures, and decorators.
- **`python-context-async-perations-0x02/`**: Asynchronous programming, coroutines, and context managers.

## 🛠 Tech Stack

- **Language:** Python 3.12+
- **Frameworks:** Django 5.x, Django REST Framework
- **Tools:** Jenkins, Postman, SQLite, Gunicorn
- **Testing:** Unittest, Mock

## ⚡ Getting Started

Each directory functions as an independent module. To run the main application:

1.  **Navigate to the app directory:**

    ```bash
    cd messaging_app
    ```

2.  **Activate the environment:**

    ```bash
    source vevn/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the server:**
    ```bash
    python manage.py runserver
    ```

## 🧪 Running Tests

To execute the test suites for the testing module:

```bash
cd 0x03-Unittests_and_integration_tests
python -m unittest discover -v
```
