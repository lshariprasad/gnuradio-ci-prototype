# 🚀 GNU Radio Hardware-in-the-Loop (HIL) CI Prototype

This project demonstrates an automated CI system for GNU Radio flowgraph validation, including simulated Hardware-in-the-Loop (HIL) testing.

## 🔧 Features

- ✅ Automated flowgraph testing
- ✅ Pytest-based validation
- ✅ GitHub Actions CI integration
- ✅ Simulated HIL testing environment
- ✅ JSON result logging system
- ✅ CI artifact generation

## 📊 Example Output

```json
{
  "samples": 100,
  "noise_floor": 0.42,
  "status": "PASS"
}
```
## ⚙️ CI Pipeline
Every commit:

Runs automated tests

Executes HIL simulation

Generates result logs

Uploads artifacts

## 🎯 Future Work
Real GNU Radio integration

USRP hardware testing

CorteXlab remote execution

Advanced signal validation (BER, SNR)

## 📌 GSoC 2026 Proposal
This project is part of a proposal for:

"Hardware-in-the-Loop CI for GNU Radio"