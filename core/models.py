from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class State:
    data: Dict[str, Any]

@dataclass
class Action:
    name: str
    params: Dict[str, Any]

@dataclass
class Observation:
    result: Any
    reward: float
    done: bool
