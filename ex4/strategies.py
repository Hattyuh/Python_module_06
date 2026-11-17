from abc import ABC, abstractmethod
from typing import cast
from ex3.base import Creature, TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise InvalidStrategyError(
                f"Invalid Creature '{creature}' for this {type(self).__name__}"
            )

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.c_name}'"
                f"for this {type(self).__name__}"
            )
        c = cast(TransformCapability, creature)
        c.transform()
        print(creature.attack())
        c.revert()

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)
