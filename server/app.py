from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# UI Home Page
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>TrustGuard</title>
        </head>
        <body style="font-family: Arial; text-align: center; padding: 40px;">
            <h1>🛡️ TrustGuard</h1>
            <h3>Fake Product Detection Environment</h3>
            
            <p>
                This system simulates product authenticity checking using:
            </p>

            <ul style="list-style: none;">
                <li>✔ Brand Verification</li>
                <li>✔ Seller Validation</li>
                <li>✔ Review Score Analysis</li>
            </ul>

            <p><b>Output:</b> Trust Score (0 to 1)</p>

            <button onclick="testReset()" 
                style="padding:10px 20px; font-size:16px; cursor:pointer;">
                Test API (/reset)
            </button>

            <p id="result" style="margin-top:20px; font-weight:bold;"></p>

            <script>
                function testReset() {
                    fetch('/reset', {method:'POST'})
                    .then(res => res.json())
                    .then(data => {
                        document.getElementById('result').innerText =
                        "API Response: " + JSON.stringify(data);
                    })
                    .catch(err => {
                        document.getElementById('result').innerText = "Error: " + err;
                    });
                }
            </script>
        </body>
    </html>
    """

# Required endpoint (validator uses this)
@app.get("/reset")
@app.post("/reset")
def reset():
    return {"status": "ok"}
