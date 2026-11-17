from typing import Protocol, Any


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CsvExporter:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("\nCSV Outout:")
        values: list[str] = [d[1] for d in data]
        for i, value in enumerate(values):
            escaped: bool = False
            if '"' in value:
                values[i] = values[i].replace('"', '""')
                values[i] = '"' + values[i] + '"'
                escaped = True
            if ("," in value or "\n" in value) and not escaped:
                values[i] = f'"{value}"'
        print(','.join(values))


class JsonExporter:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if data:
            print("\nJSON Output:")
            json: list[str] = []
            for rank, value in data:
                json.append(f'"item_{rank}": "{value}"')
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
        1, 2, 3, 4, 5, 6, 7, 8,
        "one", "two", "three", "four", "five", "six", "seven",
        {"sword": "sharp"}, {"six": "seven"},
        {"hello": "there"}, {"black": "white"},
        {"yo": "lo"}, {"va", "lid"}
    ]
    print(
        "\nCreating data stream...\n"
        f"Data stream: {test_values}\n"
        "\nProcessing stream..."
    )
    ds.process_stream(test_values)
    ds.print_processors_stats()
    print("\nConsuming elements...")
    ds.output_pipeline(2, CsvExporter())
    ds.output_pipeline(2, JsonExporter())
    ds.print_processors_stats()
