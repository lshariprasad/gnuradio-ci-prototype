# 🚀 GNU Radio Hardware-in-the-Loop (HIL) CI Prototype

A prototype CI system for automated validation of GNU Radio flowgraphs using a simulated Hardware-in-the-Loop (HIL) approach.

---

## ❗ Problem

GNU Radio currently lacks automated validation of signal processing pipelines in CI environments.

This results in:

* Flowgraphs not being tested automatically
* Signal quality issues going undetected
* Difficulty in validating hardware-dependent behavior

---

## 💡 Solution

This project introduces a **CI-integrated HIL testing system** that:

* Simulates SDR signal input
* Processes signal data through flowgraph-like logic
* Computes signal metrics (noise floor)
* Produces automated PASS/FAIL validation
* Runs fully inside CI pipelines (GitHub Actions)

---

## 🏗️ Architecture

```
Signal Simulator → Flowgraph Processing → Metric Calculation → Validation → JSON Output → CI Pipeline
```

---

## 🚀 Why This Matters for GNU Radio

GNU Radio currently lacks automated CI validation for signal pipelines.

This project demonstrates:

* Automated testing of flowgraphs
* Signal quality validation (noise floor)
* Hardware-in-the-loop simulation
* CI-ready validation pipeline

👉 This helps prevent broken signal pipelines and improves reliability.

---

## 🔧 Features

* ✅ Simulated HIL testing environment
* ✅ Deterministic testing with configurable inputs
* ✅ Pytest-based validation system
* ✅ GitHub Actions CI integration
* ✅ JSON result logging
* ✅ CI artifact generation
* ✅ CLI-based configurable validation

---

## 📊 Example Output

```json
{
  "samples": 100,
  "noise_floor": 0.42,
  "status": "PASS"
}
```

### 📌 What this means:

* `noise_floor`: computed signal noise level
* `status`: PASS if below threshold, FAIL otherwise

---

## 🖥️ CLI Usage

```bash
python hil_simulator.py --threshold 0.5
```

### 🔍 Example Behavior

| Noise Floor | Threshold | Result |
| ----------- | --------- | ------ |
| 0.42        | 0.5       | PASS   |
| 0.55        | 0.5       | FAIL   |

---

## ⚙️ CI Pipeline

On every commit:

* Runs tests using `pytest`
* Executes HIL simulation
* Generates JSON result logs
* Uploads artifacts via GitHub Actions

---

## 🔍 How Validation Works

The system simulates SDR-like signal samples and computes noise floor:

* Average absolute signal value
* Compared against threshold
* Produces PASS/FAIL

Results are stored as:

```
results/hil_result.json
```

📌 Note: Generated files are excluded via `.gitignore`

---

## 🎥 Demo

👉 This video demonstrates:

* Running pytest
* HIL simulation
* PASS/FAIL validation
* CI workflow

🔗 https://github.com/user-attachments/assets/fc362802-de59-42df-a01f-13810092addf

---

## 🔮 Future Work

* GNU Radio native integration
* Real SDR hardware testing (USRP / PlutoSDR)
* Remote execution (CorteXlab)
* Advanced metrics (BER, SNR)

---

## 📜 Logging

Structured logging tracks:

* Connection lifecycle
* Test execution
* Noise computation
* Result generation

---

## 📌 GSoC 2026 Proposal

**"Hardware-in-the-Loop CI for GNU Radio"**

---

## 🤝 Feedback

I would really appreciate feedback from the GNU Radio community on:

* Improving HIL realism
* Aligning with GNU Radio workflows
* Extending to real hardware

---

👨‍💻 Author: Hari Prasad L S
