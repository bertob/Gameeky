from typing import Tuple

from .action import Action
from .serializeable import Serializeable


class Message(Serializeable):
    def __init__(
        self,
        session_id: int,
        action: Action = Action.NOTHING,
        value: float = 0,
        sequence: int = 0,
    ) -> None:
        self.session_id = session_id
        self.action = action
        self.value = value
        self.sequence = sequence

    def to_values(self) -> Tuple[int, int, float, int]:
        return (self.session_id, self.action, self.value, self.sequence)

    @classmethod
    def from_values(cls, values: Tuple[int, int, float, int]) -> "Message":
        session_id, action, value, sequence = values
        return cls(session_id, Action(action), value, sequence)
