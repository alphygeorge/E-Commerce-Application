## Project Overview
This project is an advanced e-commerce analytics platform built with Django. It includes product inventory management, restock alerts, and an API for handling sales data. The project uses **MySQL** as the database and features include:
- ‭Accessing customer information (with proper authentication)‬
- ‭Retrieving aggregated sales data‬
- Sales analytics by product category.
- API for inventory updates. 
- Excel export functionality using the `openpyxl` library for generating sales reports.

## Technologies Used
- **Django** - Backend framework
- **Django REST Framework (DRF)** - For building RESTful APIs
- **MySQL** - Database, integrated via `pymysql`
- **drf-yasg** - Swagger/OpenAPI documentation
- **openpyxl** - Excel export functionality
- **pymysql** - MySQL integration with Django

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/alphygeorge/E-Commerce-Application.git
cd your-django-project

### 2. Install Dependencies
You can install all necessary Python packages using pip:
pip install -r requirements.txt

### 3. Configure Environment Variables
Create a .env file in the root directory of your project with the following details:

SECRET_KEY=your-secret-key
DB_NAME=your-database-name
DB_USER=your-database-username
DB_PASSWORD=your-database-password
DB_HOST=localhost

Ensure that your .env file is included in your .gitignore to avoid committing sensitive information.

### 4. Set Up MySQL Database
Create the MySQL database that your project will use:

CREATE DATABASE your_database_name;

Next, grant access to the MySQL user specified in the .env file.

GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_db_user'@'localhost' IDENTIFIED BY 'your_db_password';
FLUSH PRIVILEGES;

### 5. Migrate Database and Load Fixtures
Run the following command to apply database migrations:

python manage.py migrate

If you have SQL dumps or fixtures for sample data, load them using:

For fixtures (JSON or XML)
python manage.py loaddata path_to_fixture.json

For SQL dump (use your MySQL command line or Workbench)
mysql -u your_db_user -p your_database_name < path_to_sql_dump.sql

### 6. Run the Server
After everything is set up, start the Django development server:

python manage.py runserver

You can now access the project at http://127.0.0.1:8000/.

## Key Design Decisions
### 1. Database
The choice of MySQL was driven by its robustness and scalability for handling large datasets, essential for an e-commerce platform. We integrated MySQL using the pymysql driver, which is lightweight and well-suited for Python-Django applications.

### 2. Inventory Management
We implemented a custom Inventory model that triggers restock alerts whenever the stock falls below a set threshold. This ensures timely restocking, preventing products from being unavailable. The inventory system is tied to the Product model via a one-to-one relationship.

### 3. Environment Variables
Sensitive information like the database credentials and the secret key is managed through environment variables stored in a .env file. This enhances security and keeps configuration flexible across different environments (development, production).

### 4. API Documentation
We used the drf-yasg library to automatically generate OpenAPI/Swagger documentation for all the RESTful APIs. This provides a user-friendly interface for developers to explore the available endpoints and their requirements.


