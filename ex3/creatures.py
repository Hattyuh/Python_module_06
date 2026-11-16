from .base import Creature, TransformCapability


class Flameling(Creature):
    def __init__(self) -> None:
        super.__init__("Flameling", "Fire")

    def attack(self) -> str:
        return (f"{self.c_name} uses Ember")


class Pyrodon(Creature):
    def __init__(self) -> None:
        super.__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return (f"{self.c_name} uses Flamethrower")



class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.c_name} performs a boosted strike!"
        return f"{self.c_name} attacks normally."

    def transform(self) -> None:
        print(self.c_name, " shifts into a sharper form!")
        super().transform()

    def revert(self) -> None:
        print(self.c_name, " returns to normal.")
        super().revert()


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.c_name} unleashes a devastating morph strike!"
        return f"{self.c_name} attacks normally."

    def transform(self) -> None:
        print(self.c_name, " morphs into a dragonic battle form!")
        super().transform()

    def revert(self) -> None:
        print(self.c_name, " stabilizes its form.")
        super().revert()
