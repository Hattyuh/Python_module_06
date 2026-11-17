from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[str] = []
        self.processed_data: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Data is invalid")
        if isinstance(data, list):
            for d in data:
                self.data.append(str(d))
                self.processed_data += 1
        else:
            self.data.append(str(data))
            self.processed_data += 1

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise IndexError("No data available")
        return (self.processed_data - len(self.data), self.data.pop(0))


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for d in data:
                if isinstance(d, bool):
                    return False
                if not isinstance(d, float | int):
                    return False
            return True
        if isinstance(data, bool):
            return False
        return isinstance(data, float | int)

    def ingest(self, data: float | int | list[int] | list[float]) -> None:
        super().ingest(data)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for d in data:
                if not isinstance(d, str):
                    return False
            return True
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        super(). ingest(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for d in data:
                if not isinstance(d, dict):
                    return False
                for key, value in d.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True
        if not isinstance(data, dict):
            return False
        for key, value in data.items():
            if not isinstance(key, str) or not isinstance(value, str):
                return False
        return True

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        super(). ingest(data)


def processor_test(
    processor_name: type[DataProcessor],
    test_values: list[Any]
) -> None:
    proc = processor_name()
    print(f"\n== Testing {processor_name.__name__} ==")
    for value in test_values:
        try:
            print(f"Trying to validate '{value}': {proc.validate(value)}")
            print(f"Trying to ingest without direct validation '{value}'")
            proc.ingest(value)
        except (ValueError, IndexError) as error:
            print(f"        {error}")
        print(f"Stored data in processor: {proc.data}\n")
    while proc.data:
        try:
            data: Any = proc.output()
            print(f"{processor_name.__name__} value {data[0]}: {data[1]}")
        except IndexError as error:
            print(error)


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    test_values: Any = [
        1, 2, 3,
        [2, "two"],
        "one",
        {"dog": "kutya"}, {"cat": 1},
    ]
    procs: list[type[DataProcessor]] = [
        NumericProcessor,
        TextProcessor,
        LogProcessor
    ]
    for element in procs:
        processor_test(element, test_values)
