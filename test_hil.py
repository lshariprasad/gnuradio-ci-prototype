from hil_simulator import HILSimulator
import pytest

def test_hil_connection():
    hil = HILSimulator()
    hil.connect()
    assert hil.connected is True
    hil.disconnect()


def test_hil_run_structure():
    hil = HILSimulator()
    hil.connect()
    result = hil.run_test()

    assert result["samples"] == 100
    assert "noise_floor" in result
    assert result["status"] in ["PASS", "FAIL"]


def test_hil_pass_condition():
    hil = HILSimulator()
    hil.connect()

    result = hil.run_test(noise_override=0.2)

    assert result["status"] == "PASS"


def test_hil_fail_condition():
    hil = HILSimulator()
    hil.connect()

    result = hil.run_test(noise_override=0.9)

    assert result["status"] == "FAIL"


def test_not_connected_error():
    hil = HILSimulator()

    with pytest.raises(Exception):
        hil.run_test()