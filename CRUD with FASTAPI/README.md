# FastAPI CRUD Application with MySQL....

# steps involved....

create a separate python Environment...
In the cmd prompt..
type --> python -m venv fastapi
     --> cd fastapi
     --> cd Scripts
     --> activate

1. Set Up MySQL Database:
 --> Create a MySQL database (e.g., sample_db).
 --> Define a table for storing employee data with fields such as id, name, email, department, and created_at.

2. Install Required Python Packages:
--> Install fastapi, uvicorn, sqlalchemy, and mysql-connector-python for API development and database integration using requirnments.txt file 

In the cmd type.
-->  pip install -r requirnments.txt

3. Create a Modular Directory Structure
--> Separate files for database configuration, models, and main application logic:
--> database.py for database connection setup.
--> models.py for defining the database schema.
--> main.py for API endpoints and routing logic.

4. Configure the Database
--> Use SQLAlchemy to establish a connection to the MySQL database.
--> Define a session factory to handle database transactions.
--> DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/sample_db" in the database.py
--> Replace username,password,localhost & db_name with your MySQL credientials.

5. Design the Database Model
--> Create a SQLAlchemy model representing the employees table.
--> Include attributes like id (Primary Key), name, email, department, and created_at.

6. Implement CRUD Operations
--> Define API routes for:
--> Create: Add a new employee to the database.
--> Read: Retrieve employee details using their ID.
--> Update: Modify an existing employee's details.
--> Delete: Remove an employee record.

7. Run the Application...
In the cmd prompt 
type --> uvicorn main:app --reload

8.Test the API:
In the web browser... http://127.0.0.1:8000/docs

Note: Port number: 5000 for Flask
      Port number: 8000 for FastAPI
