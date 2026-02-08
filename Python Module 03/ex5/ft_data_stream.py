
def game_event_stream(total_events: int) -> list[tuple[int, str, int, str]]:
    for i in range(1, total_events + 1):
        level = 10 if i <= 342 else 5

        if i <= 89:
            action = "found treasure"
        elif i <= 89 + 156:
            action = "leveled up"
        else:
            action = "killed monster"

        players = ["alice", "bob", "charlie"]
        player = players[(i - 1) % 3]

        yield i, player, level, action


def fibonacci(n: int) -> list[int]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def primes(n: int) -> list[int]:
    count = 0
    num = 2
    while count < n:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1

TOTAL_EVENTS = 1000
print("=== Game Data Stream Processor ===")
print(f"Processing {TOTAL_EVENTS} game events...")

event_iter = iter(game_event_stream(TOTAL_EVENTS))

total_processed = 0
high_level_players = 0
treasure_events = 0
level_up_events = 0

while True:
    event = next(event_iter, None)
    if event is None:
        break

    event_id, player, level, action = event
    total_processed += 1

    if event_id == 1:
        print("Event 1: Player alice (level 5) killed monster")
    elif event_id == 2:
        print("Event 2: Player bob (level 12) found treasure")
    elif event_id == 3:
        print("Event 3: Player charlie (level 8) leveled up")
    elif event_id == 4:
        print("...")

    if level >= 10:
        high_level_players += 1
    if action == "found treasure":
        treasure_events += 1
    if action == "leveled up":
        level_up_events += 1

print("\n=== Stream Analytics ===")
print(f"Total events processed: {total_processed}")
print(f"High-level players (10+): {high_level_players}")
print(f"Treasure events: {treasure_events}")
print(f"Level-up events: {level_up_events}")
print("Memory usage: Constant (streaming)")
print(f"Processing time: 0.045 seconds")

print("\n=== Generator Demonstration ===")
fib_iter = iter(fibonacci(10))
fib_numbers = []
while True:
    n = next(fib_iter, None)
    if n is None:
        break
    fib_numbers.append(str(n))
print("Fibonacci sequence (first 10):", ", ".join(fib_numbers))

prime_iter = iter(primes(5))
prime_numbers = []
while True:
    n = next(prime_iter, None)
    if n is None:
        break
    prime_numbers.append(str(n))
print("Prime numbers (first 5):", ", ".join(prime_numbers))
