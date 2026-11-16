from ex3 import FlameFactory, TransformCreatureFactory
from ex3.factories import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()
    print(
        f"{base_creature.describe()}\n"
        f"{base_creature.attack()}\n"
        f"{evolved_creature.describe()}\n"
        f"{evolved_creature.attack()}\n"
    )


def fight(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    print(
        f"{creature1.describe()}\n"
        "  vs\n"
        f"{creature2.describe()}\n"
        "  fight!\n"
        f"{creature1.attack()}\n"
        f"{creature2.attack()}"
    )


if __name__ == "__main__":
    print("Testing factory")
    fFactory = FlameFactory()
    test_factory(fFactory)
    tcFactory = TransformCreatureFactory()
    test_factory(tcFactory)
    fight(fFactory, tcFactory)
