import random
import time

class HILSimulator:
    def __init__(self):
        self.connected = False

    def connect(self):
        print("Connecting to simulated hardware...")
        time.sleep(1)
        self.connected = True
        print("Connected ✅")

    def disconnect(self):
        print("Disconnecting hardware...")
        self.connected = False

    def run_test(self):
        if not self.connected:
            raise Exception("Hardware not connected")

        print("Running HIL test...")

        # Simulated SDR data
        samples = [random.uniform(-1, 1) for _ in range(100)]

        noise_floor = sum(abs(x) for x in samples) / len(samples)

        result = {
            "samples": len(samples),
            "noise_floor": noise_floor,
            "status": "PASS" if noise_floor < 0.8 else "FAIL"
        }

        print(f"Test Result: {result}")
        return result