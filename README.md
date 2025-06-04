# 🔬 Plasma Spectrum CLI Tool

**Version:** 1.0  
**Author:** Shay Sapozhnikov 
**Last Updated:** June 2025

---

## 📌 Overview

The **Plasma Spectrum CLI Tool** is a Python-based command-line interface designed to analyze, classify, and visualize elemental spectral data from plasma emission samples.

It integrates multiple machine learning models to predict which element is most likely present in a sample, compares predictions against known reference spectra, and outputs visual and textual analyses to assist scientific interpretation.

---

## 🧠 Core Features

- 🌈 **Element Classification:** Predicts elemental composition from spectral data using machine learning models (e.g., Random Forest).
- 📈 **Reference Matching:** Compares sample spectra to known reference spectra.
- 🎨 **Graphical Visualization:** Plots both raw and smoothed spectra for easy interpretation.
- ⚡ **Fast and Interactive CLI:** Simple menu interface for analysis, model evaluation, and troubleshooting.
- 🧬 **Supports Over 80 Elements:** From Hydrogen to Molybdenum, using labels like `Fe_1`, `Cu_2`, etc.

## 📁 Project Structure

```plaintext
plasmaspec/
├── Doc/                                # Documentation files
├── Models/                             # Trained machine learning models
│   ├── Heavy_metals_model/
│   │   ├── heavy_metals_rf_classifier.pkl
│   │   └── label_encoder_heavy_metals.pkl
│   ├── Light_elements_model/
│   │   ├── light_elements_rf_classifier.pkl
│   │   └── light_elements_label_encoder.pkl
│   ├── Nonmetals_&_Metalloids_model/
│   │   ├── Nonmetals_&_Metalloids_model.pkl
│   │   └── Nonmetals_&_Metalloids_label_encoder.pkl
│   ├── Rare_Earth_Elements_model/
│   │   ├── Rare_Earth_Elements_model.pkl
│   │   └── Rare_Earth_Elements_label_encoder.pkl
│   └── Transition_Metals_Model/
│       ├── Transition_Metals_model.pkl
│       └── Transition_Metals_label_encoder.pkl
├── Reference Data/
│   └── Data/                           # Elemental reference spectra (.csv)
│       └── [Element].csv               # e.g., Hydrogen.csv, Iron.csv, etc.
├── Src/                                # Source code files
│   ├── PlasmaSpec.py                   # Main CLI controller
│   ├── analyze.py                      # Spectrum analysis logic
│   ├── help.py                         # Help menu and usage instructions
│   ├── setup.py                        # Setup and environment config
│   ├── utill.py                        # Utility functions (label mapping, etc.)
│   ├── view.py                         # Visualization utilities
│   └── __pycache__/                    # Cached Python bytecode
├── Uknown Sample Data example/
│   └── TEST.csv                        # Example spectral sample
├── requirements.txt                    # Dependency list
├── temp_processed_input.csv            # Temporary processed input file
├── main.py                             # Main CLI entry point
└── README.md                           # Project documentation (this file)


## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/plasma-spectrum-cli.git
cd plasma-spectrum-cli
```

---

### 2. Dependencies

```
colorama
scikit-learn
joblib
numpy
pandas
matplotlib
scipy
```

Install via:

```bash
pip install -r requirements.txt
```

---

### 3. Prepare Your Models

Place your trained `.pkl` models inside the `models/` directory. These models should conform to the Scikit-learn API (`predict` method).

---

## 🚀 Running the Tool

Run the script from the terminal:

```bash
python3 PlasmaSpec.py
```

You will see a menu with numbered options like:

```
1. Analyze Spectral Sample
2. Compare with Reference
3. Evaluate Model Accuracy
4. Install Requirements
5. Exit
```

Follow the prompts to perform desired tasks.

---

## 📂 Input Format

### Spectral Data

- Format: CSV
- Required columns: `wavelength` and `intensity`
- Example:
```csv
wavelength,intensity
200,0.02
201,0.03
...
```

### Reference Data

Stored in `Reference Data/Data/` as individual CSVs for each element.

---

## 🧪 Machine Learning Models

The script supports multiple models trained for elemental classification.

Each model:
- Accepts preprocessed spectral vectors.
- Outputs a label like `Fe_1`, `H_3`, etc.
- Maps predictions back to the full element name using `label_to_filename`.

> 🔎 Tip: Train your models using consistent label encoding (`LabelEncoder`) for seamless integration.

---

## 📊 Output

- Terminal output with prediction results and confidence levels.
- Spectrum comparison plot saved as an image.
- Similarity score against reference spectra (if selected).

Example output:

```
Prediction: Iron (Fe)
Model Confidence: 89.23%
Best Match in Reference Data: Fe_2 (Similarity: 0.97)
```



## 🧼 Troubleshooting

- **Model Not Found?**
  Ensure your model file is named correctly and inside `models/`.

- **Path Errors?**
  Run from the root directory. The script uses relative paths.

- **Wrong Output?**
  Make sure your input CSV follows the expected format and contains relevant wavelengths.

---

## 📚 Acknowledgments

This project is built upon:
- **NIST Atomic Spectra Database**
- **Scikit-learn** for ML modeling
- **Colorama** for colorful CLI interactions
- **Matplotlib** for spectral plotting

---

## 📝 Future Enhancements

- ✅ Add support for additional rare earth elements
- 🔄 Export predictions to Excel
- 🌐 Build web-based GUI version
- 🧠 Implement model ensemble voting

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss your proposal.

---

## 📜 License

This project is licensed under the MIT License.

---
