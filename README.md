# DashboardAPI
This is a Django backend for [personal-dashboard](https://github.com/suz608/personal-dashboard) app.

## Prerequisites
To get started, make sure you have the following installed on your machine:

- Python (version 3.x)
- Pip (Python Package Installer)
- Pipenv
- Django

## 🚀 Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/suz608/DashboardAPI.git
    cd DashboardAPI
    ```
2. Install the environment:
    ```bash
    pipenv install
    ```
2. Activate pipenv:
    ```bash
    pipenv shell
    ```
3. Create environment file:
    ```bash
    cd api
    touch .env
    ```
4. Add the following line to .env:
    ```bash
    FRONTEND_URL = < Your frontend URL >
    ```
5. Apply migrations(if needed):
    ```bash
    python manage.py migrate
    ```
6. Start the server:
    ```bash
    python manage.py runserver
    ```
