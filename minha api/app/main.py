from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Query

app = FastAPI(title="Minha API Simples")

class EchoIn(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello(name: str = "world"):
    return {"message": f"hello, {name}"}

# @app.get("/")
# def root():
#     return {"message": "API rodando! Acesse /docs para ver a documentação"}

@app.post("/echo")
def echo(payload: EchoIn):
    return {"text": payload.text, "length": len(payload.text)}

@app.get("/sum")
def sum_numbers(a: int = Query(...), b: int = Query(...)):
    return {"result": a + b}