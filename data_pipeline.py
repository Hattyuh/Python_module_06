from typing import Protocol, Any


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CsvExporter(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("\nCSV Outout:")
        print(','.join(d[1] for d in data))


class JsonExporter(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if data:
            print("\nJSON Output:")
            json: list[str] = []
            for i, d in enumerate(data):
                json.append(f'"item_{i}": "{d[1]}"')
            print("{", ','.join(json), "}")


if __name__ == "__main__":
    from data_stream import DataStream
    from data_processor import (
        DataProcessor,
        NumericProcessor,
        TextProcessor,
        LogProcessor
    )
    print(
        "=== Code Nexus - Data Pipeline ===\n"
        "\nRegistering data processors..."
    )
    procs: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    ds = DataStream()
    for proc in procs:
        ds.register_processor(proc)
    print(
        "Registered data processors: ",
        ", ".join(type(proc).__name__ for proc in ds.procs)
    )
    test_values: list[Any] = [
        False, True,
        1, 2, 3, 4, 5,
        "one", "two", "three", "four",
        {"sword": "sharp"}, {"six": "seven"},
        {"hello": "there"}, {"black": "white"}
    ]
    print(
        "\nCreating data stream...\n"
        f"Data stream: {test_values}\n"
        "\nProcessing stream..."
    )
    ds.process_stream(test_values)
    ds.print_processors_stats()
    print("\nConsuming elements...")
    ds.output_pipeline(1, CsvExporter())
    ds.output_pipeline(7, JsonExporter())
    ds.print_processors_stats()
