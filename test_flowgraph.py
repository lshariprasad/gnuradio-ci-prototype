import time

# -----------------------------
# MOCK GNU RADIO CLASSES
# -----------------------------

class FakeTopBlock:
    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass


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
        self.start()
        time.sleep(0.1)
        self.stop()
        self.wait()
        return self.sink.data()


# -----------------------------
# PYTEST TEST CASES
# -----------------------------

def test_basic_flow():
    fg = TestFlowgraph()
    data = fg.run_test()
    assert len(data) > 0


def test_empty_output():
    fg = TestFlowgraph()
    fg.sink.data = lambda: []
    data = fg.run_test()
    assert len(data) == 0


def test_noise_simulation():
    fg = TestFlowgraph()
    fg.sink.data = lambda: [0.1, -0.2, 0.3]
    data = fg.run_test()
    assert len(data) == 3