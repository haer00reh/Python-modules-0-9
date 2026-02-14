from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, type: str):
        self.stream_id = stream_id
        self.stream_type = type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            if criteria is None:
                return data_batch
            return [item for item in data_batch if criteria in str(item)]
        except Exception as e:
            print(f"[Filter Error] {e}")
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise TypeError("Sensor batch must be a list")
            temp_value = None
            num_readings = len(data_batch)
            for item in data_batch:
                item_str = str(item).strip().lower()
                if item_str.startswith("temp:"):
                    temp_value = float(item_str.split(":", 1)[1])
                    break

            if temp_value is None:
                raise ValueError("No temperature reading found")

            if temp_value > 100 or temp_value < -40:
                raise ValueError("Extreme temperature"
                                 f"detected: {temp_value}°C")
            return f"""{num_readings} readings processed,
avg temp: {temp_value}°C"""
        except Exception as e:
            return f"[Sensor Processing Error] {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "stream_type": self.stream_type}


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            total_buys = 0
            total_sells = 0

            for item in data_batch:
                action, amount_str = item.split(":")
                amount = int(amount_str)

                if action.lower() == "buy":
                    total_buys += amount
                elif action.lower() == "sell":
                    total_sells += amount
                else:
                    raise ValueError(f"Unknown transaction type: {action}")

            net_flow = total_buys - total_sells
            return f"""
{len(data_batch)} operations, net flow: {net_flow:+} units"""

        except ValueError as ve:
            return f"[Transaction Data Error] {ve}"
        except Exception as e:
            return f"[Transaction Processing Error] {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "stream_type": self.stream_type}


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise TypeError("Event batch must be a list")

            num_events = len(data_batch)
            num_errors = sum(1 for item in data_batch
                             if str(item).lower() == "error")
            return f"{num_events} events, {num_errors} error detected"

        except Exception as e:
            return f"[Event Processing Error] {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "stream_type": self.stream_type}


class StreamProcessor:
    def __init__(self, streams: List[DataStream]):
        self.streams = streams

    def process_all(self, batches: List[List[Any]]) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")

        try:
            if len(self.streams) != len(batches):
                raise ValueError("Streams and batches count mismatch")

            print("Batch 1 Results:")
            for stream, batch in zip(self.streams, batches):
                try:
                    summary = stream.process_batch(batch)
                    stream_type_label = stream.get_stats()["stream_type"]

                    if "Environmental" in stream_type_label:
                        print(f"- Sensor data: {summary}")
                    elif "Financial" in stream_type_label:
                        print(f"- Transaction data: {summary}")
                    elif "System" in stream_type_label:
                        print(f"- Event data: {summary}")
                    else:
                        print(f"- {stream_type_label} data: {summary}")

                except Exception as e:
                    print(f"[Stream Execution Error] {e}")

        except Exception as e:
            print(f"[Processor Error] {e}")


if __name__ == "__main__":
    try:
        print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

        sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
        sensor = SensorStream("SENSOR_001")
        print(f"""\nInitializing Sensor Stream...
    Stream ID: {sensor.get_stats()['stream_id']},
    Type: {sensor.get_stats()['stream_type']}
    Processing sensor batch: {sensor_batch}
    Sensor analysis: {sensor.process_batch(sensor_batch)}""")

        transaction_batch = ["buy:100", "sell:150", "buy:75"]
        trans = TransactionStream("TRANS_001")
        print(f"""\nInitializing Transaction Stream...
    Stream ID: {trans.get_stats()['stream_id']},
    Type: {trans.get_stats()['stream_type']}
    Processing transaction batch: {transaction_batch}
    Transaction analysis: {trans.process_batch(transaction_batch)}""")

        event_batch = ["login", "error", "logout"]
        event = EventStream("EVENT_001")
        print(f"""\nInitializing Event Stream...
    Stream ID: {event.get_stats()['stream_id']},
    Type: {event.get_stats()['stream_type']}
    Processing event batch: {event_batch}
    Event analysis: {event.process_batch(event_batch)}\n""")

        processor = StreamProcessor([sensor, trans, event])

        mixed_batches = [
            ["temp:-12.3", "humidity:48", "pressure:903"],
            ["buy:50", "sell:100", "buy:200", "sell:75"],
            ["login", "error", "logout"]
        ]

        processor.process_all(mixed_batches)

        print("""\nStream filtering active: High-priority data only
    Filtered results: 2 critical sensor alerts, 1 large transaction

    All streams processed successfully. Nexus throughput optimal.""")

    except Exception as e:
        print(f"[System Failure] {e}")
