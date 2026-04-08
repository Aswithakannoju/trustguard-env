import os
from env import TrustGuardEnv

TASK_NAME = "trustguard"
BENCHMARK = "trustguard_env"

def log_start(task, env, model):
    print(f"[START] task={task} env={env} model={model}", flush=True)

def log_step(step, action, reward, done):
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null", flush=True)

def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}", flush=True)

def run_task(task):
    env = TrustGuardEnv(task)
    state = env.reset()

    rewards = []
    log_start(task, BENCHMARK, "baseline")

    step = 1
    action = "analyze_product"

    state, reward, done, _ = env.step(action)
    rewards.append(reward)

    log_step(step, action, reward, done)

    score = reward
    success = score > 0.2

    log_end(success, step, score, rewards)

for task in ["easy", "medium", "hard"]:
    run_task(task)
