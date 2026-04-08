from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body style="font-family: Arial; text-align:center; padding:40px;">
            <h1>🛡️ TrustGuard</h1>
            <p>Fake Product Detection System</p>
            <button onclick="testReset()">Test API</button>
            <p id="result"></p>
            <script>
                function testReset(){
                    fetch('/reset',{method:'POST'})
                    .then(r=>r.json())
                    .then(d=>document.getElementById('result').innerText=JSON.stringify(d))
                }
            </script>
        </body>
    </html>
    """

@app.get("/reset")
@app.post("/reset")
def reset():
    return {"status": "ok"}

def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
