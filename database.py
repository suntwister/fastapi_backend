from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pymysql.constants import CLIENT
import os

# Load .env variables
load_dotenv()

# Build database URL
db_url = (
    f"mysql+pymysql://{os.getenv('dbuser')}:{os.getenv('dbpassword')}"
    f"@{os.getenv('dbhost')}:{os.getenv('dbport')}/{os.getenv('dbname')}"
)

# Create the database engine
engine = create_engine(db_url, connect_args={"client_flag": CLIENT.MULTI_STATEMENTS})

# Create a session factory
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

# Create tables if they don't exist
queries = [
    text("""
        CREATE TABLE IF NOT EXISTS users (
            userid INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        );
    """),
    text("""
        CREATE TABLE IF NOT EXISTS courses (
            courseid INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            level VARCHAR(100) NOT NULL
        );
    """),
    text("""
        CREATE TABLE IF NOT EXISTS enrollments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            userid INT,
            courseid INT,
            FOREIGN KEY (userid) REFERENCES users(userid),
            FOREIGN KEY (courseid) REFERENCES courses(courseid)
        );
    """)
]

for q in queries:
    db.execute(q)

db.commit()
print("✅ Tables created successfully.")
