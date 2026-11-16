from abilities import Creature, TransformCapability


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
            return f"{self.c_name} uses special attack"
        return f"{self.c_name} attacks normally"

    def transform(self) -> None:
        super().transform()

    def revert(self) -> None:
        super().revert()


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.c_name} uses special attack"
        return f"{self.c_name} attacks normally"

    def transform(self) -> None:
        super().transform()

    def revert(self) -> None:
        super().revert()


if __name__ == "__main__":
    print("Module test in progress")
