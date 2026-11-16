from ex3 import TransformCreatureFactory
from ex3.creatures import Shiftling, Morphagon


def test(factory: TransformCreatureFactory) -> None:
    creatures: list[tuple[str, Shiftling | Morphagon]] = [
        ("base:", factory.create_base()),
        ("evolved:", factory.create_evolved())
    ]
    for text, creature in creatures:
        print(f"  {text}")
        print(
            f"{creature.describe()}\n"
            f"{creature.attack()}"
        )
        creature.transform()
        print(creature.attack())
        creature.revert()


if __name__ == "__main__":
    print("Testing Creature with transform capability")
    tcFactory = TransformCreatureFactory()
    test(tcFactory)
