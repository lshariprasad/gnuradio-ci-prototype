from gnuradio import gr, blocks, analog
import time

class TestFlowgraph(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "Test Flowgraph")

        self.signal = analog.sig_source_f(
            sampling_freq=1000,
            waveform=analog.GR_SIN_WAVE,
            frequency=100,
            amplitude=1
        )

        self.sink = blocks.vector_sink_f()

        self.connect(self.signal, self.sink)

    def run_test(self):
        print("Starting flowgraph...")
        self.start()
        time.sleep(2)
        self.stop()
        self.wait()

        data = self.sink.data()
        print(f"Collected {len(data)} samples")

        return data


if __name__ == "__main__":
    fg = TestFlowgraph()
    data = fg.run_test()

    print("Test completed successfully.")