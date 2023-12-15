# SQLAlchemy-Code-Challenge
# Restaurant Reviews Code Challenge

This code challenge focuses on building a domain model for restaurant reviews using SQLAlchemy. It involves defining relationships between three primary models: `Restaurant`, `Review`, and `Customer`.

## Domain Model Relationships

- A `Restaurant` has many `Review`s.
- A `Customer` has many `Review`s.
- A `Review` belongs to both a `Restaurant` and a `Customer`.

## Directory Structure

- `/alembic`: Contains migration scripts and configurations for database management using Alembic.
- `/models`: Includes model definitions for `Restaurant`, `Review`, and `Customer`.
- `seeds.py`: Populates sample data into the database to facilitate testing and development.

## Getting Started

1. **Setting Up Database Schema**:
   - Use SQLAlchemy Migrations to create tables for `Restaurant`, `Customer`, and `Review`.
   - Establish relationships between tables according to the provided instructions.
   - Seed the database with sample instances of `Restaurant` and `Customer`.

2. **Object Relationship Methods**:
   - Implement methods within each class to handle object relationships:
     - `Review.customer()`, `Review.restaurant()`
     - `Restaurant.reviews()`, `Restaurant.customers()`
     - `Customer.reviews()`, `Customer.restaurants()`

3. **Aggregate and Relationship Methods**:
   - Develop aggregate methods for:
     - `Customer`: `full_name()`, `favorite_restaurant()`, `add_review()`, `delete_reviews()`
     - `Review`: `full_review()`
     - `Restaurant`: `fanciest()`, `all_reviews()`

## Evaluation Rubric

- **Folder Structure**: Ensure all necessary files and directories are correctly structured.
- **Initializers and Methods**: Implement all required methods within the classes.
- **Object Relationship Methods**: Verify the accuracy of object relationship methods.
- **Method Usage and Correctness**: Ensure methods are appropriately used and yield correct results.

## Notes

- Test your methods in the console with sample instances before submission.
- Prioritize error-free implementations over incomplete functionalities.
- Refactor code for best practices if time permits.