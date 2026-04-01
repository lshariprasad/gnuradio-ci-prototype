# 🚀 GNU Radio Hardware-in-the-Loop (HIL) CI Prototype

A prototype CI system for automated validation of GNU Radio flowgraphs using a simulated Hardware-in-the-Loop (HIL) approach.

---

## ❗ Problem

GNU Radio currently lacks automated validation of signal processing pipelines in CI environments.

This means:
- Flowgraphs are not tested automatically
- Signal quality issues go undetected
- Hardware-dependent validation is difficult

---

## 💡 Solution

This project introduces a **CI-integrated HIL testing approach** that:

- Simulates SDR signal input
- Processes data through flowgraphs
- Computes signal metrics (noise floor)
- Produces automated PASS/FAIL results
- Runs fully inside GitHub Actions

---

## 🏗️ Architecture
Signal Simulator → Flowgraph Processing → Metric Calculation → Result Validation → JSON Output → CI Pipeline



---

## 🔧 Features

- ✅ Automated flowgraph testing
- ✅ Pytest-based validation
- ✅ GitHub Actions CI integration
- ✅ Simulated HIL testing
- ✅ JSON result logging
- ✅ CI artifact generation

---

## 📊 Example Output

```json
{
  "samples": 100,
  "noise_floor": 0.42,
  "status": "PASS"
}
```

## 📌 What this means:
noise_floor: Signal noise level detected

status: PASS if within acceptable threshold

## ⚙️ CI Pipeline
On every commit:

Runs automated tests using pytest

Executes HIL simulation

Generates JSON result logs

Uploads artifacts in GitHub Actions

## 🎥 Demo
👉 This video demonstrates:

Running the test suite (pytest)

HIL simulation execution

PASS/FAIL validation

CI workflow integration


https://github.com/user-attachments/assets/fc362802-de59-42df-a01f-13810092addf


## Picture 

<img width="1918" height="1020" alt="image" src="https://github.com/user-attachments/assets/0fac7aeb-7eee-4b0a-9c0d-2dbe6e241c11" />


## 🔮 Future Work
GNU Radio native integration

Real SDR hardware testing (USRP / PlutoSDR)

CorteXlab remote execution

<<<<<<< HEAD
Advanced signal validation (BER, SNR)

## 📌 GSoC 2026 Proposal
This repository is part of my proposal:

"Hardware-in-the-Loop CI for GNU Radio"
=======
Advanced validation (BER, SNR)

## 📌 GSoC 2026 Proposal
This repository is part of my proposal:

"Hardware-in-the-Loop CI for GNU Radio"

## 🤝 Feedback
I would really appreciate feedback from the GNU Radio community on:

Improving realism of HIL simulation

Aligning with GNU Radio testing practices

Extending toward real hardware integration

👨‍💻 Author: Hari Prasad L S
>>>>>>> 02126ad (Files are Updated with New version !)
