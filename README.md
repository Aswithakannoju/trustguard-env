# 🛡️ TrustGuard OpenEnv Environment

## 📌 Overview

**TrustGuard** is a real-world OpenEnv environment designed to simulate **fake product detection and authenticity verification**.

It evaluates products using:

* Brand authenticity
* Seller verification
* Customer reviews

The goal is to help AI agents learn how to assign a **trust score (0–1)** to products.

---

## 🧠 Problem Statement

Counterfeit and fake products are a major challenge in online marketplaces.
TrustGuard simulates a system that identifies suspicious products and estimates their authenticity.

---

## ⚙️ Environment Design

### 🔹 Observation Space

Each product contains:

* `brand_verified` → True/False
* `seller_verified` → True/False
* `review_score` → Integer (1–5)

---

### 🔹 Action Space

* `analyze_product` → Agent evaluates product authenticity

---

### 🔹 Reward Function

Partial rewards are given:

* +0.3 → Brand verified
* +0.3 → Seller verified (medium & hard tasks)
* +0.4 → Good reviews (hard task)

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

Logs follow strict format:

```
[START]
[STEP]
[END]
```

Each task outputs a score between **0 and 1**

---

## 🌐 API (Hugging Face)

Endpoint:

```
POST /reset
```

Response:

```
{"status": "ok"}
```

---

## 🐳 Docker

Build:

```
docker build -t trustguard .
```

Run:

```
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
app.py
pyproject.toml
README.md
```

---

## ✅ OpenEnv Compliance

* ✔ step() / reset() implemented
* ✔ 3 tasks (easy → hard)
* ✔ Reward system (0–1)
* ✔ OpenAI client usage
* ✔ Dockerized
* ✔ Hugging Face deployed
* ✔ Inference reproducible

---

## 🚀 Future Improvements

* Image/logo verification using computer vision
* NLP-based review analysis
* Fraud detection models

---

## 👩‍💻 Author

**Aswitha Kannoju**
Built for Meta AI x Scaler Hackathon
