#  Steps involved to achieve ---- COMMAND LINE OPERATION WITH FASTAPI.

# Understand about API??.. (session taken by JP).
An API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other. It defines how requests and responses should be made and exchanged, enabling integration between systems.

# Why with FASTAPI?... 
FastAPI is a modern, fast (high-performance) Python web framework for building APIs, designed to help developers create robust, efficient, and scalable APIs easily.

Key Benefits of FastAPI:
1.Speed: FastAPI is one of the fastest Python frameworks, thanks to its ASGI (Asynchronous Server Gateway Interface) support.
2.Ease of Use: Writing APIs is straightforward with minimal code and auto-generated documentation.
3.Automatic Documentation: Provides interactive Swagger UI and ReDoc for testing and understanding APIs.
4.Asynchronous Support: Built-in support for async/await for handling multiple requests efficiently.
5.Validation and Type Safety: Uses Python type hints for request validation and auto-completion, reducing errors.
6.Scalability: Suitable for large-scale applications with complex API requirements.
7.Community Support: Growing ecosystem with active contributors and libraries.


# FASTAPI ALEMBIC OPEARTION ?
Alembic is a lightweight database migration tool for SQLAlchemy. It helps manage schema changes (like adding/removing tables or columns) without manually modifying the database.

# Why Use Alembic with FastAPI?
1.Version Control: Tracks schema changes in a structured way.
2.Team Collaboration: Ensures everyone in the team works on the same database schema.
3.Ease of Use: Automates database updates through migration scripts.
4.Rollback: Allows undoing migrations when needed.


# FASTAPI CRUD-router?
FastAPI CRUDRouter is a package that simplifies the process of building CRUD (Create, Read, Update, Delete) operations in FastAPI. It automatically generates standard CRUD endpoints for your models, reducing boilerplate code and speeding up development.

# Why Use CRUDRouter?
1.Automatic CRUD Endpoints: Generates routes for common operations (GET, POST, PUT, DELETE).
2.Reduced Code: Eliminates repetitive CRUD code for each model.
3.Consistency: Ensures uniformity across all endpoints.
4.Customizable: Allows extending or modifying generated routes.


# COMMAND LINE Opearation?
--> To automate operations like table creation using a command such as alembic revision -m "create table", you can extend Alembic's functionality by adding custom logic.

1.Dynamic Migrations:
Instead of hardcoding schemas, you can dynamically generate migrations based on predefined rules or input parameters.

2.Custom Hooks:
Alembic allows you to hook custom Python functions into its command-line operations. This is typically done by modifying the env.py file.

3.Migration Autogeneration:
You can use Alembic's autogenerate feature to detect and create migration scripts for new tables or schema changes automatically.

4.Command Extensions:
Extend Alembic's CLI commands to trigger specific actions like creating tables, altering schemas, or applying business rules dynamically.


****************************************************************************************************************

# ---->  Journey Steps  <-----
1.create database in MySQL Workbench..
2.Connect MySQL with FASTAPI...   with Mysql credientials (username,password,localhost,db_name).
3.Create,Insert,Update,Delete Records with Alembic Opeartions.
4.Insert records with default columns. in (Alembic opeartions)
5.Test CRUD Operation  with Swagger UI.
6.Implement CRUD operation with FASTAPI-CRUD router -- to create automatic CRUD operations.
7.create custom template script in alembic. to create,Insert,update records with Json file (without any Hardcode). 





