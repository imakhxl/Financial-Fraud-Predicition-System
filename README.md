# 💳 Financial Fraud Detection

This project is a **Financial Fraud Detection System** built using Python, Streamlit, and XGBoost. The system predicts whether a financial transaction is fraudulent based on historical transaction data and engineered features.

---

## 📊 Dataset

- The dataset contains **6,362,620 transaction records**.
- Each record contains features like transaction type, amount, sender and receiver balances, and more.
- The dataset is highly imbalanced with only ~0.13% fraudulent transactions.

**Dataset Download:** [Kaggle Fraud Detection Dataset](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download)

---

## 🛠 Features

- **Transaction type** (e.g., PAYMENT, TRANSFER, CASH_OUT, CASH_IN, DEBIT)
- **Amount and balance features**: `amount`, `oldbalanceOrg`, `newbalanceOrig`, `oldbalanceDest`, `newbalanceDest`
- **Engineered features**:
  - `balanceDiffOrig` & `balanceDiffDest`
  - `amount_to_oldbalance_ratio`
  - `balance_change_ratio`
  - `high_risk_type` (TRANSFER & CASH_OUT)
  - Frequency encoding for senders and receivers (`sender_freq`, `receiver_freq`)

---

## 🧰 Model

- **Algorithm:** XGBoost Classifier
- **Handling Imbalance:** `scale_pos_weight` to balance the rare fraud class
- **Evaluation Metrics:**
  - Accuracy: **99.93%**
  - Precision-Recall AUC: **0.9609**
  - F1-Score for fraud class: **0.78**

---

## ⚡ How to Run

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-folder>

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
Download the dataset from Kaggle and place it in the project folder.

Train the model (optional if you want to retrain):

bash
Copy code
jupyter notebook FraudDetection.ipynb
Run the Streamlit app:

bash
Copy code
streamlit run fraud_detection.py
Open the provided URL in your browser to access the web app.

📈 App Features
Select transaction type and input transaction details.

See fraud prediction and fraud probability instantly.

Highlights high-risk features when the transaction is likely fraudulent.

📝 Notes
The model uses a combination of numerical and categorical features with preprocessing via StandardScaler and OneHotEncoder.

Pipeline saved as: fraud_detection_pipeline_updated.pkl

🔗 References
Kaggle Dataset

Streamlit Documentation

XGBoost Documentation

