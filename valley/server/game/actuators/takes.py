from .base import Actuator as BaseActuator

from ....common.definitions import Action


class Actuator(BaseActuator):
    name = "takes"
    interactable = False
    activatable = False

    def tick(self) -> None:
        if self._entity.held is not None:
            return

        if (entity := self._entity.obstacle) is None:
            return

        if entity.usable is False:
            return

        self._entity.perform(Action.TAKE)
