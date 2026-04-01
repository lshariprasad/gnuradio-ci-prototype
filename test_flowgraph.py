import time

class FakeTopBlock:
    def start(self):
        print("Flowgraph started")

    def stop(self):
        print("Flowgraph stopped")

    def wait(self):
        print("Flowgraph finished")


class FakeSink:
    def data(self):
        return [1, 2, 3, 4, 5]


class FlowgraphRunner(FakeTopBlock):
    def __init__(self):
        self.sink = FakeSink()

    def run_test(self):
        self.start()
        time.sleep(0.5)
        self.stop()
        self.wait()

        return self.sink.data()


def test_basic_flow():
    fg = FlowgraphRunner()
    data = fg.run_test()
    assert len(data) > 0


def test_empty_output():
    fg = FlowgraphRunner()
    fg.sink.data = lambda: []
    data = fg.run_test()
    assert len(data) == 0


def test_noise_simulation():
    fg = FlowgraphRunner()
    fg.sink.data = lambda: [0.1, -0.2, 0.3]
    data = fg.run_test()
    assert len(data) == 3