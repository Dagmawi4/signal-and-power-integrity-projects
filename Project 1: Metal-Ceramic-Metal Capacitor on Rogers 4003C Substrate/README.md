# HFSS Project: Metal-Ceramic-Metal Capacitor on Rogers 4003C

This project models and simulates a **metal-ceramic-metal capacitor** on a **Rogers 4003C substrate** using **ANSYS HFSS**, focusing on impedance (Z-parameters) and reflection coefficient (S-parameters) analysis across a broad frequency range.

---

## 📌 Objective

To simulate and analyze the frequency response of a high-frequency capacitor and identify its **resonant frequency**, using accurate electromagnetic modeling and parameter sweeps in HFSS.

---

## 🧩 Project Overview

- **Substrate Material**: Rogers 4003C — known for low dielectric loss and stable electrical properties at high frequencies.
- **Dielectric Layer**: Alumina (Al₂O₃) ceramic for its high dielectric constant.
- **Conductors**: Copper layers above and below the ceramic.
- **Simulation Type**: Frequency sweep from 2 GHz to 15 GHz.
- **Key Results**: Resonant frequency identified at **11 GHz** with minimal S11 reflection and low impedance.

---

## 🧱 Model Components

| Component        | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| Rogers 4003C     | High-frequency PCB material forming the base substrate                      |
| Al₂O₃ Ceramic    | Dielectric material between metal plates (high εᵣ)                           |
| Copper           | Used as top and bottom plates (metal layers)                                |
| Lumped Port      | Simulates signal input/output to extract S-parameters                       |
| Radiation Boundary | Simulates free-space propagation environment                              |

---

## 🔢 Key Design Variables

| Parameter      | Value       | Meaning                                          |
|----------------|-------------|--------------------------------------------------|
| sub_L, sub_W   | 20 mm       | Substrate dimensions (length, width)             |
| sub_H          | 1.524 mm    | Substrate height                                 |
| cap_L, cap_W   | 3 mm        | Capacitor dimensions                             |
| cap_H          | 1 mm        | Ceramic layer height                             |
| copper_t       | 18 µm       | Copper thickness                                 |
| via_R          | 0.5 mm      | Via radius for electrical connections            |
| strip_L, strip_W | 5 mm, 2 mm | Conductor strip dimensions                       |

---

## 📊 Simulation Results

### S-Parameter (S11)
- Reflection coefficient minimum observed at **11 GHz**
- Indicates optimal resonance and minimal signal reflection

### Z-Parameter (Z11)
- Impedance drops sharply around **5 GHz** and **11 GHz**
- Confirms resonant frequency and effective capacitor behavior

---

## 🧠 Conclusion

This HFSS simulation successfully demonstrates the frequency-dependent behavior of a high-frequency metal-ceramic-metal capacitor. The model captures realistic conditions with proper boundary definitions and material selection. The capacitor shows effective resonance near **11 GHz**, validating its design for high-frequency signal applications.

📄 See `HFSS_Project_Report.docx` for full documentation and technical analysis.

