import random
import time
import json
import os
from datetime import datetime

class HILSimulator:
    def __init__(self):
        self.connected = False

    def connect(self):
        logging.info("Connecting to simulated hardware...")
        time.sleep(0.5)
        self.connected = True
        print("Connected")

    def disconnect(self):
        self.connected = False
        print("Disconnected")

    def run_test(self, noise_override=None):
        if not self.connected:
            raise RuntimeError("Hardware not connected")

        print("Running HIL test...")

        if noise_override is not None:
            noise_floor = noise_override
        else:
            samples = [random.uniform(-1, 1) for _ in range(100)]
            noise_floor = sum(abs(x) for x in samples) / len(samples)

        result = {
            "timestamp": datetime.now().isoformat(),
            "samples": 100,
            "noise_floor": noise_floor,
            "status": "PASS" if noise_floor < 0.8 else "FAIL"
        }

        os.makedirs("results", exist_ok=True)

        filename = f"results/hil_result_{int(time.time())}.json"
        with open(filename, "w") as f:
            json.dump(result, f, indent=4)

        print(f"Saved result → {filename}")
        return result


# CORRECT PLACE (outside class)
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="HIL CI Simulator")
    parser.add_argument("--threshold", type=float, default=0.8,
                        help="Noise threshold for PASS/FAIL")

    args = parser.parse_args()

    hil = HILSimulator()
    hil.connect()

    result = hil.run_test()

    # Apply threshold logic
    if result["noise_floor"] < args.threshold:
        result["status"] = "PASS"
    else:
        result["status"] = "FAIL"

    print("\nFinal Result:")
    print(result)

    hil.disconnect()