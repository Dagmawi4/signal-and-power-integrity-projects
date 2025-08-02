import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"C:\Users\dagit\OneDrive\Desktop\Fall 2024\EE 486,486 Signal and Power Integrity\HFSS Project\Project 2\S Parameter Plot 1.csv"
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File not found at '{file_path}'. Check the path and try again.")
    exit()

# Clean column names by removing spaces, brackets, and special characters
data.columns = data.columns.str.strip().str.replace(r"[^\w]", "", regex=True)

# Debugging: Print cleaned column names
print("Cleaned Column Names:", data.columns)

# Extract relevant columns
try:
    frequency = data['FreqGHz'] * 1e9  # Convert GHz to Hz
    S21_dB = data['dBS21']  # NEXT data in dB
    S12_dB = data['dBS12']  # FEXT data in dB
except KeyError as e:
    print(f"Error: {e}. Check your file for column names.")
    exit()

# Convert S-parameters from dB to linear scale
S21_linear = 10 ** (S21_dB / 20)  # NEXT coefficient
S12_linear = 10 ** (S12_dB / 20)  # FEXT coefficient

# Time settings for simulation
time = np.linspace(0, 2e-9, 1000)  # Time range (0 to 2 ns)
unit_step = np.heaviside(time, 1)  # Unit step input signal

# Interpolate S-parameter coefficients for the time domain
NEXT_coeff = np.interp(time, np.linspace(0, max(time), len(S21_linear)), S21_linear)
FEXT_coeff = np.interp(time, np.linspace(0, max(time), len(S12_linear)), S12_linear)

# Crosstalk transfer functions
def NEXT_signal(input_signal, coeff):
    """Simulate Near-End Crosstalk (NEXT)."""
    next_signal = coeff * np.diff(input_signal, prepend=0)
    return next_signal

def FEXT_signal(input_signal, coeff, delay=50):
    """Simulate Far-End Crosstalk (FEXT)."""
    delayed_signal = np.roll(input_signal, delay)
    delayed_signal[:delay] = 0  # Zero out initial delay
    fext_signal = coeff * delayed_signal
    return fext_signal

# Simulate the signals
next_output = NEXT_signal(unit_step, NEXT_coeff)
fext_output = FEXT_signal(unit_step, FEXT_coeff, delay=50)

# Plot results
plt.figure(figsize=(10, 8))

# Input Signal
plt.subplot(3, 1, 1)
plt.plot(time, unit_step, color='blue')
plt.title("Input Signal (Unit Step)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

# Near-End Crosstalk (NEXT)
plt.subplot(3, 1, 2)
plt.plot(time, next_output, color='red')
plt.title("Near-End Crosstalk (NEXT)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

# Far-End Crosstalk (FEXT)
plt.subplot(3, 1, 3)
plt.plot(time, fext_output, color='green')
plt.title("Far-End Crosstalk (FEXT)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
