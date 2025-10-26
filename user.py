import bcrypt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
from dotenv import load_dotenv
from database import db
import uvicorn
import os

# load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="Use Authentication API", version="1.0.0")

# -------------------------
# Pydantic Models
# -------------------------

class SignupRequest(BaseModel):
    name: str = Field(..., example="Samuel John")
    email: str = Field(..., example="samuel@example.com")
    password: str = Field(..., example="John12345")

class LoginRequest(BaseModel):
    email: str = Field(..., example="samuel@example.com")
    password: str = Field(..., example="John12345")

# ------- SIGNUP ------------
@app.post("/signup")
def signup(user: SignupRequest):
    try:
        # check if email exist
        duplicate_query = text("SELECT * FROM users WHERE email = :email")
        result = db.execute(duplicate_query, {"email": user.email}).fetchone()

        if result:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Hash password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), salt)

        # Insert user into DB
        query = text("""
            INSERT INTO users (name, email, password)
            VALUES(:name, :email, :password)
        """)
        db.execute(query, {
            "name": user.name,
            "email": user.email,
            "password": hashed_password.decode("utf-8")
        })
        db.commit()

        return {"message": "User registered successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# --------- LOGIN -----------   
@app.post("/login")
def login(user: LoginRequest):
    try:
        # check if email exist
        query = text("SELECT * FROM users WHERE email = :email")
        result = db.execute(query, {"email": user.email}).fetchone()

        if not result:
            raise HTTPException(status_code=404, detail="User not found")

        # Extract the hashed password from DB row
        stored_password = result[3].encode("utf-8")

        # Verify password
        if not bcrypt.checkpw(user.password.encode("utf-8"), stored_password):
            raise HTTPException(status_code=401, detail="Invalid email or password")

        return {"message": "Login successful"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Run server 
if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))
    