#  FastAPI Backend Project

A simple backend API built with **FastAPI** and **MySQL**.  
This project demonstrates how to connect a FastAPI app to a MySQL database, create and authenticate users securely with **bcrypt**, and manage configuration with environment variables.

---

##  Project Structure

fastapi_backend/
│
├── app.py # Main FastAPI entry file
├── database.py # MySQL database connection and table creation
├── user.py # User signup & login routes
├── requirements.txt # Project dependencies
├── .env # Environment variables (NOT pushed to GitHub)
└── .gitignore # Ignored files and folders


---

## Installation & Setup

### 1️ Clone the repository
git clone https://github.com/suntwister/fastapi_backend.git
cd fastapi_backend

### 2️ Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # On Windows

### 3️ Install dependencies
pip install -r requirements.txt

### 4️ Create a .env file

Create a .env file in the project root and add your configuration:

port=5000
host=127.0.0.1

dbuser=root
dbpassword=YourPassword
dbhost=localhost
dbport=3306
dbname=backend_db

###  Running the App

To start the FastAPI server:

python app.py

Open in your browser or Postman:

http://127.0.0.1:5000

