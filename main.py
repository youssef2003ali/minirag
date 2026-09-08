from fastapi import FastAPI

app = FastAPI()
@app.get("/welcome")
def welcome():
    return {
        "message" :"Welcome to n3n3 FAST API TEST"
    }