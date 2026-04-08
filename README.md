# 🚀 TrustGuard OpenEnv Environment

## 📌 Overview

**TrustGuard** is a real-world OpenEnv environment designed to simulate **fake product detection and authenticity verification**.

It evaluates products based on:

* Brand authenticity
* Seller verification
* Customer review quality

The environment enables AI agents to interact and learn how to assess product trustworthiness using structured signals.

---

## 🧠 Problem Statement

Fake and counterfeit products are a major issue in e-commerce.
TrustGuard simulates a system that helps identify suspicious products and assign a **trust score (0–1)**.

---

## ⚙️ Environment Design

### 🔹 State (Observation Space)

Each product contains:

* `brand_verified` → True/False
* `seller_verified` → True/False
* `review_score` → Integer (1–5)

---

### 🔹 Action Space

* `analyze_product` → Agent evaluates product authenticity

---

### 🔹 Reward Function

Partial rewards are assigned:

* +0.3 → Brand verified
* +0.3 → Seller verified (medium & hard tasks)
* +0.4 → Good reviews (hard task)

Final score is normalized between **0 and 1**.

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

The script logs:

```
[START]
[STEP]
[END]
```

Each task produces a score between **0.0 and 1.0**.

---

## 🐳 Docker Support

Build:

```bash
docker build -t trustguard .
```

Run:

```bash
docker run trustguard
```

---

## 🌐 Hugging Face Deployment

API Endpoint:

```
POST /reset
```

Example Response:

```json
{"status": "ok"}
```

---

## 📁 Project Structure

```
env.py
inference.py
tasks.py
openenv.yaml
Dockerfile
app.py
```

---

## ✅ OpenEnv Compliance

* ✔ step() / reset() implemented
* ✔ 3 tasks (easy → hard)
* ✔ Reward system (0–1)
* ✔ Dockerized
* ✔ HF Space deployed
* ✔ Inference reproducible

---

## 🚀 Future Improvements

* Image/logo verification using CV models
* NLP-based review analysis
* Fraud pattern detection

---

## 👩‍💻 Author
**Aswitha Kannoju**  
Built for Meta AI x Scaler Hackathon


