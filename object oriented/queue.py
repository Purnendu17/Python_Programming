class CheckoutCounter:
    """Represents a checkout counter with a queue of customers."""
    def __init__(self, counter_id: int, queue_length: int):
        self.counter_id = counter_id
        self.queue_length = queue_length

class StoreManager:
    """Manages the process of finding the fastest checkout counter."""
    def __init__(self, counters: list):
        self.counters = counters

    def find_fastest_counter(self) -> int:
        """Finds the counter with the shortest queue."""
        if not self.counters:
            raise ValueError("No counters available.")

        # Use `min` to simplify finding the counter with the shortest queue
        fastest_counter = min(self.counters, key=lambda c: c.queue_length)
        return fastest_counter.counter_id

# Example Usage
if __name__ == "__main__":
    # Create a list of checkout counters with their queue lengths
    counters = [
        CheckoutCounter(1, 5),
        CheckoutCounter(2, 3),
        CheckoutCounter(3, 8)
    ]

    # Initialize the store manager
    manager = StoreManager(counters)

    # Find the fastest counter
    fastest_counter_id = manager.find_fastest_counter()
    print(f"The fastest counter is Counter {fastest_counter_id}.")
