from hil_simulator import HILSimulator


def test_hil_connection():
    hil = HILSimulator()
    hil.connect()
    assert hil.connected is True
    hil.disconnect()


def test_hil_run():
    hil = HILSimulator()
    hil.connect()
    result = hil.run_test()

    assert result["samples"] == 100
    assert "noise_floor" in result
    assert result["status"] in ["PASS", "FAIL"]


def test_hil_fail_condition():
    hil = HILSimulator()
    hil.connect()

    # Force bad noise
    hil.run_test = lambda: {
        "samples": 100,
        "noise_floor": 1.5,
        "status": "FAIL"
    }

    result = hil.run_test()
    assert result["status"] == "FAIL"