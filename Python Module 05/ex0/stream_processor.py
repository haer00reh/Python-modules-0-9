from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, list) or not all(
             isinstance(x, (int)) for x in data):
            raise ValueError("NumericProcessor expects a list of numbers")
        print("Validation: Numeric data verified")
        return True

    def process(self, data: List[float]) -> str:
        total = sum(data)
        avg = total / len(data)
        return f"Processed {len(data)} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            raise ValueError("TextProcessor expects a string")
        print("Validation: Text data verified")
        return True

    def process(self, data: str) -> str:
        char_count = len(data)
        word_count = len(data.split())
        return f"Processed text: {char_count} characters, {word_count} words"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str) or ":" not in data:
            raise ValueError("LogProcessor expects"
                             "a log string like 'LEVEL: message'")
        print("Validation: Log entry verified")
        return True

    def process(self, data: str) -> str:
        level, message = data.split(":", 1)
        level = level.upper()
        message = message.strip()

        if level == "ERROR":
            return f"[ALERT] ERROR level detected: {message}"
        elif level == "WARNING":
            return f"[WARN] Warning detected: {message}"
        else:
            return f"[INFO] {message}"

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


def run_processor(processor: DataProcessor, data: Any) -> None:
    if not isinstance(processor, DataProcessor):
        raise TypeError("ERROR: must inherite from DataProcessor")
    try:
        print(f"Processing data: {data}")
        processor.validate(data)
        result = processor.process(data)
        print(processor.format_output(result))
    except ValueError as e:
        print(f"Validation Error: {e}")


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("Initializing Numeric Processor...")
    run_processor(NumericProcessor(), [1, 2, 3, 4, 5])

    print("\nInitializing Text Processor...")
    run_processor(TextProcessor(), "Hello Nexus World")

    print("\nInitializing Log Processor...")
    run_processor(LogProcessor(), "ERROR: Connection timeout")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...\n")
    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    test_data = [
        [10, 20, 30],
        "Polymorphism is powerful",
        "WARNING: Disk space low",
    ]

    for proc, data in zip(processors, test_data):
        run_processor(proc, data)
        print()
print("Foundation systems online. Nexus ready for advanced streams.")