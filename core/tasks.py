from core.models import State, Action

class SimpleTask:
    def get_initial_state(self) -> State:
        return State(data={"step": 0})

    def get_possible_actions(self, state: State):
        return [
            Action(name="move_forward", params={}),
            Action(name="wait", params={})
        ]
