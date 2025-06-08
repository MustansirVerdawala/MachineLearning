# 🫀 Heart Failure Mortality Prediction with XGBoost

This project builds a binary classification model using XGBoost to predict the likelihood of patient mortality from heart failure. The dataset is sourced from HuggingFace (`mstz/heart_failure`) and includes a mix of clinical measurements and patient attributes.

---

## 📁 Dataset

- **Source**: [mstz/heart_failure](https://huggingface.co/datasets/mstz/heart_failure) (via HuggingFace Datasets)
- **Target Variable**: `is_dead`
- **Features**:
  - `age`, `creatinine_phosphokinase_concentration_in_blood`, `heart_ejection_fraction`
  - `platelets_concentration_in_blood`, `serum_creatinine_concentration_in_blood`, `serum_sodium_concentration_in_blood`
  - Boolean flags: `has_anaemia`, `has_diabetes`, `has_high_blood_pressure`, `is_male`, `is_smoker`

---

## 🧼 Preprocessing

- Checked for missing values and whitespace issues
- Dropped `days_in_study` (leakage)
- Converted boolean flags to integers
- Applied `RobustScaler` to numerical columns to reduce the impact of outliers
- Performed a stratified 67/16.5/16.5 train/validation/test split

---

## 📊 Model

- **Algorithm**: XGBoost Classifier (`binary:logistic`)
- **Hyperparameters**:
  - `scale_pos_weight=4` to handle class imbalance
  - `max_depth=2`, `gamma=0.25`, `learning_rate=0.05`
  - `n_estimators=10000`, with `early_stopping_rounds=100`
  - `eval_metric='aucpr'`
  - Focus: The primary optimization goal in this project was high recall for the positive class (is_dead = 1), to minimize false negatives and avoid missing high-risk patients.

---

## 📈 Performance

| Dataset    | AUC   | Accuracy | F1-Score (Dead) | Precision (Dead) | Recall (Dead) |
|------------|-------|----------|------------------|-------------------|----------------|
| Train      | 0.872 | 0.73     | 0.69             | 0.55              | 0.91           |
| Validation | 0.833 | 0.61     | 0.60             | 0.45              | 0.88           |
| Test       | 0.829 | 0.70     | 0.63             | 0.52              | 0.81           |

---

## 📌 Visualizations

- Boxplots to analyze outliers
- Confusion matrices for each split
- XGBoost’s AUC-PR learning curve
- Feature importance (gain, cover, weight, etc.)
- Visualized tree from the first boosting round

---

## 🚀 Run on Google Colab
Click the badge below to open and run the notebook in Colab:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1s3WyCJgwFFe2Ge4Cq_aiPLmGUBwZeOLB?usp=drive_open#scrollTo=cuI9DfK_79k2)

---

## 🛠️ Libraries Used
- `pandas`, `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `XGBoost`
- `Datasets`

---

## 📎 Author
**Mustansir Verdawala**  
