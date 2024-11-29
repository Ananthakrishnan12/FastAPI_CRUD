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

2. Install Required Python Packages:
--> Install fastapi, uvicorn, sqlalchemy, and mysql-connector-python for API development and database integration using requirnments.txt file 

In the cmd type.
-->  pip install -r requirnments.txt

3. Create table in the Database.. (Using Alembic operation)..
In the command prompt.
type --> alembic init alembic
It create alembic directory.
Go to alembic.ini file and change the deatils in sqlalchemy.url="mysql+mysqlconnector://username:password@localhost/sample_db"  
Replace with ypur username,password,db_name with your MySQL credientials..
Next , In the command prompt..
type --> alembic revision -m "create table" 
It creates script in the version folder with revision id like this (7b1ba8e1d3a2_create_items_table).
Give the column field & Description of your custom tables.
Next, (For execution) In the command prompt,
type --> alembic upgrade head  

For validation, Go to MySQL workbench 
type --> select * from table_name;

Like that we can implement create table,Insert record,update records & Delete records in the Table.


4. Create a Modular Directory Structure
--> Separate files for database configuration, models, and main application logic:
--> database.py for database connection setup.
--> models.py for defining the database schema.
--> main.py for API endpoints and routing logic.


5. Implement CRUD Operations
--> Define API routes for:
--> Create: Add a new employee to the database.
--> Read: Retrieve employee details using their ID.
--> Update: Modify an existing employee's details.
--> Delete: Remove an employee record.

6. Run the Application...
In the cmd prompt 
type --> uvicorn main:app --reload

8.Test the API:
In the web browser... http://127.0.0.1:8000/docs

Note: Port number: 5000 for Flask
      Port number: 8000 for FastAPI

