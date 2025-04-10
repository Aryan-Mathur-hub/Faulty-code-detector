# 🧠 Faulty Code Detector

This project uses **machine learning and deep learning models** to detect whether a C program is **faulty or non-faulty** based on its code structure. It leverages static analysis and preprocessed datasets to train predictive models for fault classification.

---

## 📁 Project Structure

```
FAULTY CODE DETECTOR/
├── Datasets/                         # Preprocessed datasets (from PROMISE)
│   ├── processed_jm1.csv
│   └── processed_kc1.csv
│
├── Examples/                         # Example C files
│   ├── faulty_example.c
│   └── non_faulty_example.c
│
├── Model_training/                   # Notebooks for training models
│   ├── DL_Models.ipynb
│   └── ML_Models.ipynb
│
├── models/                           # Trained model files
│   ├── ann_model.pth                 # ANN (PyTorch)
│   ├── lr_model.pkl                  # Logistic Regression
│   ├── meta_model.pth                # Meta model (ensemble)
│   ├── nn_model.h5                   # Keras-based neural network
│   ├── rf_model.pkl                  # Random Forest
│   ├── nn_model.pth                  # Another PyTorch NN variant
│   ├── scaler.pkl                    # Scaler used for feature normalization
│   └── xgb_model.pkl                 # XGBoost model
│
├── data_processing_promise_dataset.py  # Script to process PROMISE datasets
├── Faulty_code_predictor.ipynb         # Final prediction notebook
├── Static_code_analyzer.py             # Extracts code features for prediction
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation
```

---

## 🔍 What It Does

- Extracts **static features** from C code using `Static_code_analyzer.py`
- Loads pre-trained ML/DL models to **predict if code is faulty**
- Uses curated datasets (`jm1`, `kc1`) from the **PROMISE repository**
- Supports **ensemble/meta-learning** using multiple models

---

## 🛠 How To Use

### 1. 🔧 Setup Environment

```bash
pip install -r requirements.txt
```

### 2. 🧪 Analyze Example

You can test the system using the sample C files:

```bash
python Static_code_analyzer.py Examples/faulty_example.c
```

Then, use the notebook:

```bash
jupyter notebook Faulty_code_predictor.ipynb
```

This will load the models and predict if the analyzed code is **Faulty** or **Non-Faulty**.

---

## 📊 Models Used

- Logistic Regression  
- Random Forest  
- XGBoost  
- Neural Networks (Keras + PyTorch)  
- Meta Model (ensemble)

---

## 📚 Datasets

- Based on the **PROMISE repository**
- Processed: `jm1`, `kc1`

---

## 📄 License

MIT License

---

Let me know if you’d like to add usage screenshots, evaluation metrics, or contribution guidelines!
