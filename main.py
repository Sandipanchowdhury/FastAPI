from fastapi import FastAPI

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message" : "Welcome to FastAPI."}


# About Route
@app.get("/about")
def about():
    return {"message":"This is my about section"}

# Description
@app.get("/users")
def users():
    return {
        "users": ["Mohit","Rohit","Amit"]
    }
