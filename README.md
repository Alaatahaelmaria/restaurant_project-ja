# Restaurant Project

This project is a simple web application for restaurant search and user authentication, built with Flask, SQLite, and MongoDB.

## Features
- User registration and login (SQLite)
- Restaurant search (MongoDB)
- Web interface with HTML/CSS

## Project Structure
- `app.py`: Main Flask application (routes, logic)
- `create_sql_table.py`: Initializes SQLite database and user table
- `setup_mongodb.py`: Sets up MongoDB and inserts sample restaurant data
- `database/requirements.txt`: (empty, add dependencies if needed)
- `static/`: Static files (CSS, images)
- `templates/`: HTML templates (login, register, search)

## Setup Instructions
1. **Python Environment**: Activate the virtual environment in `restaurant_project_env/`.
   - On Windows PowerShell:
     ```powershell
     .\restaurant_project_env\Scripts\Activate.ps1
     ```
2. **Install Dependencies**:
   - If not already installed, add required packages to `requirements.txt` and run:
     ```powershell
     pip install -r database/requirements.txt
     ```
   - Main dependencies: `Flask`, `pymongo`, `sqlite3` (standard library)
3. **Initialize Databases**:
   - Run the scripts to set up databases:
     ```powershell
     python create_sql_table.py
     python setup_mongodb.py
     ```
4. **Run the Application**:
   - Start the Flask app:
     ```powershell
     python app.py
     ```
   - Access the app at [http://localhost:5000](http://localhost:5000)

## Notes
- Default users are created in SQLite (`users.db`).
- Sample restaurants are inserted into MongoDB (`restaurant_db`).
- Customize HTML/CSS in `templates/` and `static/` folders.

## License
MIT
