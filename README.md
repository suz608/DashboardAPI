# DashboardAPI
This is a Django backend for [personal-dashboard](https://github.com/suz608/personal-dashboard) app.

### Prerequisites
To get started, make sure you have the following installed on your machine:

- Python (version 3.x)
- Pip (Python Package Installer)
- Pipenv
- Django

### To set up this backend
1. Clone the repository:
    ```bash
    git clone https://github.com/suz608/DashboardAPI.git
    cd DashboardAPI
    ```
2. Activate pipenv:
    ```bash
    pip shell
    ```
3. Create environment file:
    ```bash
    cd api
    touch .env
    ```
    Add 'FRONTEND_URL' to the '.env' file ( The default URL is "http://localhost:4200")
4. Start the server:
    ```bash
    python manage.py runserver
    ```
