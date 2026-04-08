from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "TrustGuard API Running"}

@app.get("/reset")
@app.post("/reset")
def reset():
    return {"status": "ok"}
