import time

# -----------------------------
# MOCK GNU RADIO CLASSES
# -----------------------------

class FakeTopBlock:
    def start(self):
        print("Flowgraph started")

    def stop(self):
        print("Flowgraph stopped")

    def wait(self):
        print("Flowgraph finished")


class FakeSink:
    def data(self):
        # Simulated output samples
        return [1, 2, 3, 4, 5]


# -----------------------------
# TEST FLOWGRAPH CLASS
# -----------------------------

class TestFlowgraph(FakeTopBlock):
    def __init__(self):
        self.sink = FakeSink()

    def run_test(self):
        print("Starting flowgraph...")

        # Start flowgraph
        self.start()
        time.sleep(1)
        self.stop()
        self.wait()

        # Collect data
        data = self.sink.data()
        print(f"Collected {len(data)} samples")

        # PASS / FAIL LOGIC
        if len(data) > 0:
            print("TEST PASSED ✅")
        else:
            print("TEST FAILED ❌")

        return data


# -----------------------------
# MAIN EXECUTION
# -----------------------------

if __name__ == "__main__":
    fg = TestFlowgraph()
    result = fg.run_test()

    print("Test completed successfully.")

import json

result_data = {
    "samples": len(result),
    "status": "PASS" if len(result) > 0 else "FAIL"
}

with open("results.json", "w") as f:
    json.dump(result_data, f)

print("Results saved to results.json")