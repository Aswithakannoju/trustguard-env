# 🛡️ TrustGuard OpenEnv Environment

## 📌 Overview

**TrustGuard** is a real-world OpenEnv environment that simulates **fake product detection and authenticity verification**.

It allows AI agents to evaluate product trustworthiness based on multiple real-world signals and generate a **trust score between 0 and 1**.

---

## 🧠 Problem Statement

Fake and counterfeit products are a major issue in online marketplaces.
TrustGuard models a system that detects suspicious products using:

* Brand authenticity
* Seller credibility
* Customer review analysis

---

## ⚙️ Environment Design

### 🔹 Observation Space

Each product is represented with:

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

```bash
python inference.py
```

---

## 📊 Output Format

The inference script logs:

```
[START]
[STEP]
[END]
```

Each task returns a score between **0 and 1**.

---

## 🌐 API (Hugging Face)

### Base URL

Your deployed Space:

```
https://aswi18-trustgurad-env.hf.space
```

### Endpoints

* `GET /` → UI dashboard
* `POST /reset` → Required validation endpoint
* `GET /reset` → Testing support

### Example Response

```json
{"status": "ok"}
```

---

## 🖥️ UI Preview

A simple web interface is available at `/`:

* Displays project overview
* Allows testing API with a button
* Shows live API response

---

## 🐳 Docker Support

### Build

```bash
docker build -t trustguard .
```

### Run

```bash
docker run trustguard
```

---

## 📁 Project Structure

```
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
* ✔ Structured logging (START / STEP / END)
* ✔ Dockerized environment
* ✔ Hugging Face deployment
* ✔ API validation endpoint `/reset`
* ✔ Multi-mode deployment support

---

## 🚀 Future Improvements

* Image/logo verification using computer vision
* NLP-based review analysis
* Advanced fraud detection models

---

## 👩‍💻 Author

**Aswitha Kannoju**
Built for Meta AI x Scaler Hackathon
