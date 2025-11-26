from fastapi import FastAPI,Depends

app = FastAPI()

@app.get('/')
def get_data():
    return
