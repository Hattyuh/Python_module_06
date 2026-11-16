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
    def __init__(self, is_transformed: bool = False) -> None:
        self.is_transformed = is_transformed

    @abstractmethod
    def transform(self) -> None:
        self.is_transformed = True

    @abstractmethod
    def revert(self) -> None:
        self.is_transformed = False


if __name__ == "__main__":
    print("Module test in progress")
