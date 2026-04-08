import random

class TrustGuardEnv:
    def __init__(self, task="easy"):
        self.task = task
        self.step_count = 0
        self.done = False

    def reset(self):
        self.step_count = 0
        self.done = False
        
        self.state = {
            "brand_verified": random.choice([True, False]),
            "seller_verified": random.choice([True, False]),
            "review_score": random.randint(1, 5)
        }
        return self.state

    def step(self, action):
        self.step_count += 1
        
        score = 0.0
        
        # Reward logic
        if self.state["brand_verified"]:
            score += 0.3
        if self.task != "easy" and self.state["seller_verified"]:
            score += 0.3
        if self.task == "hard" and self.state["review_score"] > 3:
            score += 0.4

        self.done = True
        
        return self.state, score, self.done, {}
