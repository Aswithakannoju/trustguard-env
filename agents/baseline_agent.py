from core.tasks import SimpleTask
from core.env import Environment

class BaselineAgent:
    def __init__(self):
        self.env = Environment()
        self.task = SimpleTask()

    def run(self):
        state = self.env.reset()
        done = False

        while not done:
            actions = self.task.get_possible_actions(state)

            # pick first action (simple logic)
            action = actions[0]

            observation = self.env.step(action)

            print(f"Action: {action.name}")
            print(f"Result: {observation.result}")
            print(f"Reward: {observation.reward}")
            print("-----")

            done = observation.done
