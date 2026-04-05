from core.tasks import SimpleTask
from core.env import Environment
import random

class BaselineAgent:
    def __init__(self):
        self.env = Environment()
        self.task = SimpleTask()

    def run(self):
        state = self.env.reset()
        done = False

        while not done:
            actions = self.task.get_possible_actions(state)

            action = random.choice(actions)

            observation = self.env.step(action)

            # 🔥 update state
            state = self.env.state

            print(f"Action: {action.name}")
            print(f"Result: {observation.result}")
            print(f"Reward: {observation.reward}")
            print("-----")

            done = observation.done
