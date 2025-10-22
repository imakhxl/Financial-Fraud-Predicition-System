# 💳 Financial Fraud Detection System

This project is a **Financial Fraud Detection System** built using **Python**, **Streamlit**, and **XGBoost**. It's designed to predict whether a financial transaction is fraudulent in real-time based on historical transaction data and a set of engineered features.

---

## 🚀 How to Run

Follow these steps to set up and run the application locally:

1.  **Clone the Repository**
    ```bash
    git clone <repo-url>
    cd <repo-folder>
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download the Dataset**
    * Download the dataset from the [Kaggle Fraud Detection Dataset](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download).
    * Place the downloaded file in the project's root directory.

4.  **Train the Model (Optional)**
    * If you wish to retrain the model, execute the training notebook:
        ```bash
        jupyter notebook FraudDetection.ipynb
        ```
    * *Note: A pre-trained model pipeline is included (`fraud_detection_pipeline_updated.pkl`).*

5.  **Run the Streamlit App**
    * Launch the interactive web application:
        ```bash
        streamlit run fraud_detection.py
        ```
    * Open the provided URL in your web browser to access the application.

---

## 📊 Dataset Overview

| Feature | Detail |
| :--- | :--- |
| **Size** | **6,362,620** transaction records |
| **Features** | Transaction type, amount, sender/receiver balances, etc. |
| **Imbalance** | **Highly Imbalanced** ($\approx 0.13\%$ fraudulent transactions) |
| **Source** | [Kaggle Fraud Detection Dataset](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download) |

---

## 🛠 Features Used

The system utilizes both raw and expertly **engineered features** for enhanced predictive power:

### ⚙️ Raw & Core Features

* **Transaction type** (`PAYMENT`, `TRANSFER`, `CASH_OUT`, `CASH_IN`, `DEBIT`)
* **Amount and balance features**: `amount`, `oldbalanceOrg`, `newbalanceOrig`, `oldbalanceDest`, `newbalanceDest`

### ✨ Engineered Features

* **Balance Differences**: `balanceDiffOrig` and `balanceDiffDest` (change in balance *before* and *after* the transaction).
* **Ratios**: `amount_to_oldbalance_ratio` and `balance_change_ratio`.
* **High-Risk Flag**: `high_risk_type` (Boolean flag for `TRANSFER` & `CASH_OUT` transaction types, which are statistically more prone to fraud).
* **Frequency Encoding**: `sender_freq` and `receiver_freq` (to capture the transactional activity level of accounts, which can be an indicator of suspicious behavior).

---

## 🧰 Model and Performance

### 🧠 Model Architecture

* **Algorithm**: **XGBoost Classifier** (eXtreme Gradient Boosting)
* **Preprocessing**: Features are processed via a pipeline including `StandardScaler` for numerical data and `OneHotEncoder` for categorical data (transaction type).
* **Imbalance Handling**: The severe class imbalance is addressed using the **`scale_pos_weight`** parameter in XGBoost to assign a higher weight to the rare fraud class, preventing the model from ignoring it.

### 📈 Evaluation Metrics

The model demonstrates strong performance in identifying the rare fraud class:

| Metric | Result | Interpretation |
| :--- | :--- | :--- |
| **Accuracy** | **99.93%** | High overall correctness, but misleading due to imbalance. |
| **Precision-Recall AUC** | **0.9609** | Excellent measure of performance for imbalanced data. |
| **F1-Score (Fraud Class)** | **0.78** | Good harmonic mean of precision and recall for the positive (fraud) class. |

---

## ⚡ App Features

The Streamlit web application provides an intuitive interface for real-time prediction:

* **Interactive Input**: Select the transaction type and input all required transaction details.
* **Instant Prediction**: See the **fraud prediction** (Fraudulent/Non-Fraudulent) and the **fraud probability** instantly.
* **Risk Highlighting**: Highlights high-risk features and details when the transaction is deemed likely fraudulent.

---

## 📝 Notes

* The complete feature engineering, model training, and saving process is detailed in `FraudDetection.ipynb`.
* The trained model and preprocessing steps are bundled and saved as: `fraud_detection_pipeline_updated.pkl`.

---

## 🔗 References

* [Kaggle Dataset](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download)
* [Streamlit Documentation](https://docs.streamlit.io/)
* [XGBoost Documentation](https://xgboost.readthedocs.io/en/latest/index.html)

