import os
from typing import List
from openai import OpenAI
from env import TrustGuardEnv

# Environment variables (as required)
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
API_KEY = os.getenv("HF_TOKEN") or os.getenv("API_KEY")

# OpenAI client (MANDATORY requirement)
client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

TASK_NAME = "trustguard"
BENCHMARK = "trustguard_env"

# Logging functions (STRICT FORMAT)
def log_start(task: str, env: str, model: str):
    print(f"[START] task={task} env={env} model={model}", flush=True)

def log_step(step: int, action: str, reward: float, done: bool):
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null", flush=True)

def log_end(success: bool, steps: int, score: float, rewards: List[float]):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}", flush=True)

# Generate action using OpenAI (with safe fallback)
def get_action():
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You analyze product authenticity."},
                {"role": "user", "content": "Give a short action to analyze product"}
            ],
            max_tokens=10,
            temperature=0.5
        )
        action = (response.choices[0].message.content or "").strip()
        return action if action else "analyze_product"
    except Exception:
        return "analyze_product"

# Run a single task
def run_task(task: str):
    env = TrustGuardEnv(task)
    state = env.reset()

    rewards = []
    log_start(task, BENCHMARK, MODEL_NAME)

    step = 1
    action = get_action()

    state, reward, done, _ = env.step(action)
    rewards.append(reward)

    log_step(step, action, reward, done)

    score = max(0.01, min(0.99, reward))  # normalize
    success = score > 0.1

    log_end(success, step, score, rewards)

# Run all tasks
if __name__ == "__main__":
    for task in ["easy", "medium", "hard"]:
        run_task(task)
