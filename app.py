import uvicorn
from fastapi import FastAPI
from jaysmlmodel import IrisModel, IrisSpecies

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello Igor'}

@app.get('/{name}')
def get_name(name: str):
    return {'message': f'Hello, {name}'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)