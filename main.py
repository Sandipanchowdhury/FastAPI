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

# User_Details
@app.get("/users/{user_id}")
def get_users(user_id:int):
    return {
        "user_id" : user_id
    }

