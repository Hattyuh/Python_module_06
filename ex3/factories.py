from abc import ABC, abstractmethod
from creatures import Flameling, Pyrodon, Shiftling, Morphagon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:

    def create_evolved(self) -> Creature:


class TransformCreatureFactory(CreatureFactory):
    def create_base(self, creature_type: type[Creature]) -> Creature:
        return creature_type("Shiftling", "Normal")

    def create_evolved(self, creature_type: type[Creature]) -> Creature:
        new_creature: Creature = creature_type("Morphagon", "Normal")
        new_creature.transform()
        return new_creature


if __name__ == "__main__":
    print("Module test is in progress")
