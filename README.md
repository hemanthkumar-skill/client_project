# Project Django

Welcome to the **Project Django** repository! This project serves as a comprehensive example of a web application built using the Django framework. It includes essential features like client management, project assignment, and user authentication, all implemented using Django REST Framework.

## Features

- **Client Management**: Add, update, delete, and fetch client information with ease.
- **Project Assignment**: Assign projects to clients and manage user assignments to these projects.
- **User Authentication**: Built-in user authentication to secure access to the application.
- **Django Admin Integration**: Utilize Django's default admin interface for managing users.
- **API Endpoints**: A set of RESTful API endpoints for interacting with the application.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sampath7996/Project_Django.git

2.  Navigate to the project directory:
       cd Project_Django
    
3.  Create a virtual environment:
        python -m venv venv
    
4.  Activate the virtual environment:

        On Windows:
          venv\Scripts\activate
        On macOS/Linux:
           source venv/bin/activate


5. Install the dependencies
    pip install -r requirements.txt

6.  Run database migrations:
      python manage.py makemigrations
      python manage.py migrate
    
7.    Create a superuser:
      python manage.py createsuperuser

8.  Start the development server:
      python manage.py runserver

**API Endpoints**

1.Create a New Client
URL: /api/clients/
Method: POST
Body (JSON):
json

{
  "client_name": "Client A"
}

2.Fetch Client Information
URL: /api/clients/{id}/
Method: GET

3.Update Client Information
URL: /api/clients/{id}/
Method: PUT/PATCH
Body (JSON):
json

{
  "client_name": "Updated Client Name"
}

4.Delete a Client
URL: /api/clients/{id}/
Method: DELETE

5.Create a New Project
URL: /api/projects/
Method: POST
Body (JSON):
json

{
  "project_name": "Project A",
  "client_id": 1,
  "users": [1, 2]
}

6.List Projects Assigned to Logged-in User
URL: /api/user/projects/
Method: GET
