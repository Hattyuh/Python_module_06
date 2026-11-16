from abc import ABC, abstractmethod

class Creature(ABC):
    def __init__(self, c_name: str, c_type: str) -> None:
        self.c_name = c_name
        self.c_type = c_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.c_name} is a {self.c_type} creature"


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> None:
        pass

    @abstractmethod
    def revert(self) -> None:
        pass


class Shiftling(Creature, TransformCapability):
    def __init__(self, c_name: str, c_type: str) -> None:
        super.__init__(c_name, c_type)
        self.is_transformed: bool = False

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.c_name} uses special attack"
        return f"{self.c_name} attacks normally"

    def transform(self) -> None:
        self.is_transformed = True

    def revert(self) -> None:
        self.is_transformed = False


class Morphagon(Creature, TransformCapability):
    def __init__(self, c_name: str, c_type: str) -> None:
        super.__init__(c_name, c_type)
        self.is_transformed: bool = False

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.c_name} uses special attack"
        return f"{self.c_name} attacks normally"

    def transform(self) -> None:
        self.is_transformed = True

    def revert(self) -> None:
        self.is_transformed = False


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> None:
        pass

    @abstractmethod
    def create_evolved(self) -> None:
        pass

if __name__ == "__main__":
    shiftling = 
