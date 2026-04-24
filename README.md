# 🛡️ TrustGuard OpenEnv Environment

## 📌 Overview

**TrustGuard** is a real-world OpenEnv environment designed to simulate **fake product detection and authenticity verification**.

It enables AI agents to evaluate products based on multiple real-world signals and generate a **trust score between 0.0 and 1.0**.

---

## 🧠 Problem Statement

Counterfeit and fake products are a major challenge in modern e-commerce platforms.

TrustGuard simulates a system that detects suspicious products using:

* Brand authenticity
* Seller verification
* Customer review analysis

---

## ⚙️ Environment Design

### 🔹 Observation Space

Each product contains:

* `brand_verified` → Boolean
* `seller_verified` → Boolean
* `review_score` → Integer (1–5)

---

### 🔹 Action Space

* `analyze_product` → Agent evaluates product authenticity

---

### 🔹 Reward Function

The environment provides **partial rewards**:

* +0.3 → Brand verified
* +0.3 → Seller verified (medium & hard tasks)
* +0.4 → High review score (hard task)

Final score is normalized between **0.0 and 1.0**

---

## 🧪 Tasks

| Task   | Difficulty | Description                              |
| ------ | ---------- | ---------------------------------------- |
| Easy   | ⭐          | Check brand authenticity                 |
| Medium | ⭐⭐         | Check brand + seller                     |
| Hard   | ⭐⭐⭐        | Full trust evaluation (reviews included) |

---

## ▶️ Running Inference

```bash id="w5zhqy"
python inference.py
```

---

## 📊 Output Format

The inference script strictly follows:

```id="sy0xlg"
[START]
[STEP]
[END]
```

Each task produces a score between **0.0 and 1.0**

---

## 🌐 API (Hugging Face Deployment)

### Base URL

```id="y0y2hy"
https://aswi18-trustgurad-env.hf.space
```

### Endpoints

* `GET /` → UI dashboard
* `POST /reset` → Required validation endpoint
* `GET /reset` → Testing support

### Example Response

```json id="2wrsqr"
{"status": "ok"}
```

---

## 🖥️ UI Interface

A simple web UI is available at `/`:

* Displays system overview
* Allows API testing via button
* Shows live API response

---

## 🐳 Docker Support

### Build

```bash id="g9n76g"
docker build -t trustguard .
```

### Run

```bash id="gi9y2j"
docker run trustguard
```

---

## 📁 Project Structure

```id="jrv0h4"
env.py
inference.py
tasks.py
openenv.yaml
Dockerfile
pyproject.toml
uv.lock
server/
   app.py
README.md
```

---

## ✅ OpenEnv Compliance

* ✔ step() / reset() implemented
* ✔ 3 tasks (easy → hard)
* ✔ Reward system (0–1 range)
* ✔ OpenAI client usage
* ✔ Structured logs (START / STEP / END)
* ✔ Dockerized environment
* ✔ Hugging Face deployment
* ✔ API endpoint `/reset`
* ✔ Multi-mode deployment ready
* ✔ server/app.py with main() entrypoint

---

## 🚀 Future Improvements

* Image/logo verification using computer vision
* NLP-based review sentiment analysis
* Advanced fraud detection models

---

## 👩‍💻 Author

**Aswitha Kannoju**

