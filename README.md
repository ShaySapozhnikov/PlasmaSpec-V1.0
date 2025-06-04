
# 🔬 Plasma Spectrum CLI Tool

**Version:** 1.0  
**Author:** Shay Sapozhnikov  
**Last Updated:** June 2025

---

## 📌 Overview

The **Plasma Spectrum CLI Tool** is a command-line application designed for analyzing and classifying optical emission spectra of plasma samples. By leveraging **machine learning** and **domain-specific reference data**, the tool can predict the elemental composition of unknown plasma spectra and visualize their spectral signatures.

It is particularly useful for scientific research, spectroscopy labs, and chemical identification in physical or chemical sciences.

---

## 🧠 How It Works

This tool employs a combination of:

### 🔍 1. **Spectral Preprocessing**
- The input CSV data must contain `wavelength` and `intensity` columns.
- Data is:
  - **Cleaned**: Invalid or null values are removed.
  - **Sorted**: Wavelengths are ordered for consistency.
  - **Interpolated**: Spectra are resampled over a standard grid to ensure uniform input across samples.
    - *Implementation:* Linear interpolation via `scipy.interpolate.interp1d`.
  - **Smoothed**: Uses a **Savitzky-Golay filter** to reduce noise while preserving peaks.
    - *Implementation:* `scipy.signal.savgol_filter` with configurable `window_length` and `polyorder`.
  - **Normalized**: The intensity vector is scaled (e.g., Min-Max normalization) to mitigate differences due to varying brightness.

### 🧠 2. **Machine Learning-Based Classification**
- Each model is a **Random Forest classifier** trained on specific categories of elements:
  - Heavy Metals
  - Light Elements
  - Nonmetals & Metalloids
  - Transition Metals
  - Rare Earth Elements
- These models are trained with `scikit-learn` and saved as `.pkl` files.
- Features are extracted from smoothed and normalized intensity values over interpolated wavelengths.
- Output is a label like `Fe_1`, which is decoded back to an element name using a `LabelEncoder`.

### 📊 3. **Reference Spectrum Matching**
- After a model predicts an element, the predicted spectrum is compared against a reference CSV.
- A **peak-matching similarity score** is calculated:
  - Peaks in the sample and reference are matched based on closeness in both **wavelength** and **intensity** (within tolerances).
  - Similarity is the ratio of matched peaks to total reference peaks.

---

## 🎯 Core Features

- 🌈 **Element Identification** via machine learning classifiers
- 📈 **Reference Similarity Scoring**
- 🧠 **Supports 80+ Elements** (e.g., Hydrogen to Molybdenum)
- 🎨 **Visual Plotting** of raw and smoothed spectra
- 🖥️ **Menu-Driven CLI Interface**
- 🔍 **Model Confidence & Similarity Reporting**

---

## 📁 Project Structure

```plaintext
plasmaspec/                   
├── Models/                   # Trained ML models (Random Forest)
│   └── [Grouped by element class]/
├── Reference Data/Data/      # Reference elemental spectra (.csv)
├── Src/                      # Source code
│   ├── PlasmaSpec.py         # CLI controller
│   ├── analyze.py            # Spectrum analysis & ML inference
│   ├── view.py               # Visualization logic
│   ├── utill.py              # Label mapping, model dictionaries
│   └── ...
├── Unknown Sample Data/      # Example sample input
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## 🛠️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/ShaySapozhnikov/PlasmaSpec-V1.0
cd PlasmaSpec-V1.0
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies include:
- `scikit-learn`
- `pandas`, `numpy`, `scipy`
- `matplotlib`
- `joblib`
- `colorama`

---

## 🚀 Usage Guide

From the root directory:

```bash
cd Src
python3 PlasmaSpec.py
```

Menu options:
```
1. Analyze Spectral Sample 
2. View an Element's Spectra
3. Help (?)
4. Setup
5. Exit
```

---

## 📥 Input Format

### Sample Spectrum

```csv
wavelength,intensity
200,0.02
201,0.03
...
```

### Reference Files

Stored in `Reference Data/Data/` as individual `.csv` files named after each element:
```
Iron.csv
Hydrogen.csv
Calcium.csv
...
```

---

## 🧪 Machine Learning Models

### 📦 Model Types

Each model is scoped to a subset of elements:
- `Heavy_metals_rf_classifier.pkl`
- `Light_elements_rf_classifier.pkl`
- `Rare_Earth_Elements_model.pkl`
- `Nonmetals_&_Metalloids_model.pkl`
- `Transition_Metals_model.pkl`

Each follows Scikit-learn's API:
```python
model.predict(X)
```

### 🔁 Label Encoding

Each classifier comes with a `.pkl` `LabelEncoder` file, ensuring consistent mapping between model labels and element names:
```python
label_encoder.inverse_transform(prediction)
```

### 🧮 Prediction Pipeline

1. Input spectrum is interpolated, smoothed, and normalized.
2. Vectorized form is passed to the model.
3. Model predicts a label.
4. Label is decoded into a human-readable element.
5. Predicted spectrum is optionally compared to a reference spectrum.

---

## 📊 Output Example

```text
Prediction: Iron (Fe)
Model Confidence: 89.23%
Best Match in Reference Data: Fe_2 (Similarity: 0.97)
```

A visual plot (smoothed vs reference) is saved to disk for analysis.

---

## 🔎 How Similarity Scoring Works

The `compare_spectrum_to_reference` function:
- Locates all local maxima in the smoothed intensity curve.
- Compares each sample peak against reference peaks.
- If a reference peak is within ±5 nm in wavelength and ±20% in intensity, it's considered a match.
- Score = matched peaks / total reference peaks.

This approach helps **validate classification predictions** with spectral physics in mind.

---

## 🧼 Troubleshooting

| Issue                     | Solution                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| Model not found          | Ensure the `.pkl` file exists in `Models/` and matches required filename |
| Wrong prediction         | Verify input spectrum quality and wavelength alignment                   |
| Reference mismatch       | Check if reference data exists and is clean                              |
| Path errors              | Always run from the root folder or use relative paths                    |

---

## 🧠 Future Roadmap

- ✅ Expand support for rare earths
- 🧠 Model ensemble voting (average across multiple models)
- 📤 Export results to Excel
- 🌐 Web GUI using Flask or Streamlit
- 🧪 Spectrum noise augmentation for training

---

## 🤝 Contributing

Contributions are welcome! Please:
- Fork the repo
- Submit a pull request with clear descriptions
- Open issues for bugs or feature requests

---

## 📚 Acknowledgments

- **NIST Atomic Spectra Database** — Reference spectra source
- **Scikit-learn** — ML modeling engine
- **Colorama** — CLI styling
- **Matplotlib** — Visualization engine
- **SciPy** — Signal smoothing and interpolation

---

## 📜 License

This project is licensed under the **MIT License**.
