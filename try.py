from fastapi import FastAPI
app= FastAPI()
@app.get("/")
def write():
    return{
        "Name" : "Diya",
        "Age" : 20
    }
