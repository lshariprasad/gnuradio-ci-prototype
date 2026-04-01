import random
import time
import json
import os
from datetime import datetime


class HILSimulator:
    def __init__(self):
        self.connected = False

    def connect(self):
        print("Connecting to simulated hardware...")
        time.sleep(0.5)
        self.connected = True
        print("Connected ")

    def disconnect(self):
        print("Disconnected")

    def run_test(self):
        if not self.connected:
            raise Exception("Hardware not connected")

        print("Running HIL test...")

        samples = [random.uniform(-1, 1) for _ in range(100)]
        noise_floor = sum(abs(x) for x in samples) / len(samples)

        result = {
            "timestamp": datetime.now().isoformat(),
            "samples": len(samples),
            "noise_floor": noise_floor,
            "status": "PASS" if noise_floor < 0.8 else "FAIL"
        }

        os.makedirs("results", exist_ok=True)

        filename = f"results/hil_result_{int(time.time())}.json"
        with open(filename, "w") as f:
            json.dump(result, f, indent=4)

        print(f"Saved result → {filename}")
        return result