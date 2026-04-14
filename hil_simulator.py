import random
import time
import json
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class HILSimulator:
    def __init__(self):
        self.connected = False

    def connect(self):
        logging.info("Connecting to simulated hardware...")
        time.sleep(0.5)
        self.connected = True
        logging.info("Connected")

    def disconnect(self):
        self.connected = False
        logging.info("Disconnected")

    def run_test(self, noise_override=None):
        if not self.connected:
            raise RuntimeError("Hardware not connected")

        logging.info("Running HIL test...")

        # Generate noise
        if noise_override is not None:
            noise_floor = noise_override
        else:
            samples = [random.uniform(-1, 1) for _ in range(100)]
            noise_floor = sum(abs(x) for x in samples) / len(samples)

        # Prepare result
        result = {
            "timestamp": datetime.now().isoformat(),
            "samples": 100,
            "noise_floor": noise_floor,
            "status": "PASS" if noise_floor < 0.8 else "FAIL"
        }

        # Save results
        os.makedirs("results", exist_ok=True)
        filename = "results/hil_result.json"

        with open(filename, "w") as f:
            json.dump(result, f, indent=4)

        logging.info(f"Noise floor: {noise_floor}")
        logging.info(f"Saved result → {filename}")

        return result


# CLI execution
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="HIL CI Simulator")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.8,
        help="Noise threshold for PASS/FAIL"
    )

    
    args = parser.parse_args()

    hil = HILSimulator()
    hil.connect()

    result = hil.run_test()

    # Apply threshold logic
    result["status"] = "PASS" if result["noise_floor"] < args.threshold else "FAIL"

    logging.info(f"Final Result: {result}")

    hil.disconnect()
