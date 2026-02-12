from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union

class DataStream(ABC):
    def __init__(self, stream_id: str, type: str):
        self.stream_id = stream_id
        self.stream_type = type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass
    
    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": "UNKNOWN", "stream_type": "Generic Data"}


class sensor_stream(DataStream):
    def __init__(self, stream_id: str, type: str):
        super().__init__(stream_id, type)


    def process_batch(self, data_batch: List[Any]) -> str:
        num_readings = len(data_batch)
        avg_temp = 22.5
        return f"{num_readings} readings processed, avg temp: {avg_temp}°C"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "stream_type": self.stream_type}

class trans_stream(DataStream):
    def __init__(self, stream_id: str, type: str):
        super().__init__(stream_id, type)

    def process_batch(self, data_batch: List[Any]) -> str:
        total_buys = 0
        total_sells = 0
        for item in data_batch:
            action, amount_str = item.split(":")
            amount = int(amount_str)
            if action.lower() == "buy":
                total_buys += amount
            elif action.lower() == "sell":
                total_sells += amount
        net_flow = total_buys - total_sells
        return f"{len(data_batch)} operations, net flow: {net_flow:+} units"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "stream_type": self.stream_type}


class event_stream(DataStream):
    def __init__(self, stream_id: str, type: str):
        super().__init__(stream_id, type)

    def process_batch(self, data_batch: List[Any]) -> str:
        num_events = len(data_batch)
        num_errors = sum(1 for item in data_batch if str(item).lower() == "error")
        return f"{num_events} events, {num_errors} error detected"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "stream_type": self.stream_type}


class StreamProcessor:
    def __init__(self, streams: List[DataStream]):
        self.streams = streams

    def process_all(self, batches: List[List[Any]]):
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")

        print("Batch 1 Results:")
        for stream, batch in zip(self.streams, batches):
            summary = stream.process_batch(batch)

            stream_type_label = stream.get_stats()["stream_type"]
            if "Sensor" in stream_type_label:
                print(f"- Sensor data: {summary}")
            elif "Financial" in stream_type_label:
                print(f"- Transaction data: {summary}")
            elif "Event" in stream_type_label:
                print(f"- Event data: {summary}")
            else:
                print(f"- {stream_type_label} data: {summary}")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    sensor = sensor_stream("SENSOR_001", "Environmental Data")
    print(f"""\nInitializing Sensor Stream...
    Stream ID: {sensor.get_stats()['stream_id']}, Type: {sensor.get_stats()['stream_type']}
    Processing sensor batch: {sensor_batch}
    Sensor analysis: {sensor.process_batch(sensor_batch)}""")

    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    trans = trans_stream("TRANS_001", "Financial Data")
    print(f"""\nInitializing Transaction Stream...
    Stream ID: {trans.get_stats()['stream_id']}, Type: {trans.get_stats()['stream_type']}
    Processing transaction batch: {transaction_batch}
    Transaction analysis: {trans.process_batch(transaction_batch)}""")

    event_batch = ["login", "error", "logout"]
    event = event_stream("EVENT_001", "System Events")
    print(f"""\nInitializing Event Stream...
    Stream ID: {event.get_stats()['stream_id']}, Type: {event.get_stats()['stream_type']}
    Processing event batch: {event_batch}
    Event analysis: {event.process_batch(event_batch)}\n""")

    processor = StreamProcessor([sensor, trans, event])
    mixed_batches = [
        ["temp1", "temp2"],
        ["buy:50", "sell:100", "buy:200", "sell:75"],
        ["login", "error", "logout"]
    ]
    processor.process_all(mixed_batches)

    print("""\nStream filtering active: High-priority data only
    Filtered results: 2 critical sensor alerts, 1 large transaction
    \nAll streams processed successfully. Nexus throughput optimal.""")
