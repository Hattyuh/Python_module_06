from ex3.base import Creature
from ex3.factories import (
    CreatureFactory,
    FlameFactory,
    TransformCreatureFactory
)
from ex4.strategies import (
    InvalidStrategyError,
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy
)


def battle(
        opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    opp_count = len(opponents)
    print(
        "*** tournament ***\n"
        f"{opp_count} opponents involved"
    )
    for j in range(opp_count - 1):
        print("\n  round:", j + 1)
        for i in range(j + 1, opp_count):
            creature1: Creature = opponents[j][0].create_base()
            creature2: Creature = opponents[i][0].create_base()
            print("\n* battle *")
            print(
                f"{creature1.describe()}\n"
                "  vs\n"
                f"{creature2.describe()}\n"
                "  now fight!\n"
            )
            try:
                opponents[j][1].act(creature1)
                opponents[i][1].act(creature2)
            except InvalidStrategyError as error:
                print("Battle error, aborting tournament:", error)
                return


if __name__ == "__main__":
    opponents: list[tuple[CreatureFactory, BattleStrategy]] = [
        (FlameFactory(), NormalStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]
    print(
        "Tournament 0 (basic)\n"
        "[ (Flameling+Normal), (Shiftling+Aggressive) ]"
    )
    battle(opponents)
    opponents = [
        (TransformCreatureFactory(), AggressiveStrategy()),
        (FlameFactory(), AggressiveStrategy()),
    ]
    print(
        "Tournament 1 (error)\n"
        "[ (Shiftling+Aggressive), (Flameling+Aggressive) ]"
    )
    battle(opponents)
