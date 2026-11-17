import typing
from data_pipeline import ExportPlugin
from data_processor import (
        DataProcessor,
        NumericProcessor,
        TextProcessor,
        LogProcessor
)


class DataStream:
    def __init__(self) -> None:
        self.procs: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            self.procs.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for data in stream:
            for proc in self.procs:
                if proc.validate(data):
                    proc.ingest(data)
                    break
            else:
                print(f"{data} can not be processed")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        for proc in self.procs:
            if proc.processed_data > 0:
                print(
                    f"{proc.__class__.__name__}: "
                    f"total {proc.processed_data} items processed, "
                    f"remaining {len(proc.data)} on processor"
                )
            else:
                print(f"{proc.__class__.__name__}: unused - no stats")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.procs:
            data: list[tuple[int, str]] = []
            for i in range(nb):
                if proc.data:
                    data.append(proc.output())
            plugin.process_output(data)


if __name__ == "__main__":
    print(
        "=== Code Nexus - Data Stream ===\n"
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
    test_values: list[typing.Any] = [
        False, True,
        1, 2, 3, 4, 5,
        "Hello", "There",
        {"sword": "sharp"}, {"yoyo": 2}
    ]
    print(
        "\nCreating data stream...\n"
        f"Data stream: {test_values}\n"
        "\nProcessing stream..."
    )
    ds.process_stream(test_values)
    ds.print_processors_stats()
    print("\nConsuming elements...")
    for proc in ds.procs:
        try:
            print(
                f"Element consumed from {type(proc).__name__}:",
                proc.output()
            )
        except IndexError as error:
            print(f"Element can not be consumed: {error}")
    ds.print_processors_stats()
