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

Run the simulator with custom threshold:

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

## 🎥 Demo

👉 This video demonstrates:

* Running the test suite (`pytest`)
* HIL simulation execution
* PASS/FAIL validation
* CI workflow integration

🔗 https://github.com/user-attachments/assets/fc362802-de59-42df-a01f-13810092addf

---

## 📁 Output

<<<<<<< HEAD

https://github.com/user-attachments/assets/fc362802-de59-42df-a01f-13810092addf


## Picture 

<img width="1918" height="1020" alt="image" src="https://github.com/user-attachments/assets/0fac7aeb-7eee-4b0a-9c0d-2dbe6e241c11" />

=======
## 🔍 How Validation Works

The system simulates SDR-like signal samples and computes noise floor as:

- Average absolute signal value
- Compared against threshold
- Produces PASS/FAIL

This mimics real-world signal validation in CI pipelines.

=======
Results are stored as:

```
results/hil_result_<timestamp>.json
```

📌 Note: Generated files are excluded from version control via `.gitignore`

---
>>>>>>> d69879b (Enhance HIL CI prototype: add CLI threshold support, improve validation logic, clean repo, and update README)

## 🔮 Future Work

* GNU Radio native flowgraph integration
* Real SDR hardware testing (USRP / PlutoSDR)
* Remote execution (CorteXlab)
* Advanced metrics (BER, SNR)

---

## 📌 GSoC 2026 Proposal

This repository is part of my proposal:

**"Hardware-in-the-Loop CI for GNU Radio"**

---

## 🤝 Feedback

I would really appreciate feedback from the GNU Radio community on:

* Improving realism of HIL simulation
* Aligning with GNU Radio testing workflows
* Extending toward real hardware integration

---

👨‍💻 Author: Hari Prasad L S
