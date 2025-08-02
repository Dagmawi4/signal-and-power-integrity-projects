# Signal and Power Integrity – Project 2

This project investigates **crosstalk** between two closely spaced microstrip lines using both **HFSS (High-Frequency Structure Simulator)** and **Python-based time-domain simulations**. The focus is on analyzing and visualizing **Near-End Crosstalk (NEXT)** and **Far-End Crosstalk (FEXT)** using S-parameters obtained from HFSS.

## 🔍 Project Objective

To model, simulate, and analyze signal interference (crosstalk) that occurs when two microstrip lines are placed close to each other. The project uses:
- **HFSS** for electromagnetic simulation of the microstrip geometry
- **Python** for post-processing and visualizing crosstalk effects in the time domain

## 🧠 HFSS Simulation Summary

The HFSS model consists of two parallel microstrip lines on an FR4 substrate:

- **Ports**: Ports 1 and 3 are input ports; Ports 2 and 4 are output ports.
- **Signal Traces**: The close proximity between the orange and blue traces induces crosstalk.
- **S-Parameters**:
  - `S11` and `S22`: Input reflection coefficients
  - `S21` and `S12`: Transmission coefficients used for NEXT and FEXT analysis

HFSS provides S-parameter results that are exported as a CSV file and used for time-domain analysis.

## 🧪 Python Crosstalk Simulation

The Python script processes the S-parameters and simulates signal behavior:

1. **Load and clean CSV data**
2. **Convert `S21` and `S12` from dB to linear scale**
3. **Apply a unit step signal**
4. **Simulate**:
   - **NEXT**: Derived from the derivative of the input, scaled by `S21`
   - **FEXT**: A delayed version of the input, scaled by `S12`
5. **Visualize**:
   - Input Signal
   - Near-End Crosstalk (NEXT)
   - Far-End Crosstalk (FEXT)

### 📦 Libraries Used
- `numpy`
- `pandas`
- `matplotlib`

Install with:
```bash
pip install numpy pandas matplotlib

