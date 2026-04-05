from core.models import State, Action, Observation

class Environment:
    def __init__(self):
        self.state = State(data={"step": 0})

    def reset(self):
        self.state = State(data={"step": 0})
        return self.state

    def step(self, action: Action) -> Observation:
        # simple logic for now
        self.state.data["step"] += 1

        reward = 1.0  # dummy reward
        done = self.state.data["step"] >= 5  # stop after 5 steps

        return Observation(
            result=f"Action {action.name} executed",
            reward=reward,
            done=done
        )
