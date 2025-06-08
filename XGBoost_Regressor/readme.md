# 🧬 Life Expectancy Regression with XGBoost

This project builds a regression model using XGBoost to predict a country’s **life expectancy** from various socioeconomic and health-related features. The dataset was sourced from a WHO-backed open dataset available [here](https://raw.githubusercontent.com/EvidenceN/Life-Expectancy-Prediction/master/Life%20Expectancy/Data/Life%20Expectancy%20Data.csv).

---

## 📁 Dataset

- **Target**: `Life_expectancy_`
- **Features**:
  - Numeric: `Adult_Mortality`, `Alcohol`, `percentage_expenditure`, `_BMI_`, `_HIV/AIDS`, `Schooling`, etc.
  - Categorical: `Status` → converted to dummy variables
- **Preprocessing**:
  - Dropped rows with missing values
  - Removed leakage features (e.g., `Income composition of resources`)
  - Scaled numerical columns using `RobustScaler`
  - Stratified 50/25/25 Train/Valid/Test split

---

## 🧼 Data Cleaning

- Dropped country/year info and redundant features (GDP, Measles, Polio, etc.)
- One-hot encoded `Status` and removed weak predictors
- Replaced whitespaces in column names
- Standardized numerical columns to reduce outlier impact

---

## 📊 Model

- **Model**: `XGBoostRegressor`
- **Objective**: `reg:squarederror`
- **Hyperparameters**:
  - `learning_rate=0.01`, `n_estimators=1000`, `max_depth=5`
  - `gamma=0.20`, `reg_lambda=25`
  - `early_stopping_rounds=100`, `eval_metric='rmse'`
- **Baseline**:
  - Mean Life Expectancy: **69.30**
  - Baseline RMSE: **0.812**

---

## 📈 Performance

| Dataset    | RMSE   | MAE    | R²     |
|------------|--------|--------|--------|
| Train      | 0.1726 | 0.1203 | 0.9545 |
| Validation | 0.2380 | 0.1649 | 0.9163 |
| Test       | 0.2243 | 0.1537 | 0.9237 |

---

## 📌 Visualizations

- **Boxplots** comparing distributions across splits
- **SHAP Summary Plot** for model interpretability
- **XGBoost Learning Curve** (RMSE vs boosting rounds)

---

## 📈 Achievements

 - 🎯 Beat the baseline RMSE of 0.812 by 72% on training data
→ Achieved RMSE of 0.1726, a massive reduction in prediction error.
 - 🧠 Model generalizes well, maintaining high accuracy on unseen data:
   - Validation RMSE: 0.2380 (71% lower than baseline)
   - Test RMSE: 0.2243 (72% lower than baseline)
   - 📏 R² Score of 0.9237 on test set, indicating the model explains over 92% of the variance in life expectancy.
 - 💪 Low MAE (0.1537) means your predictions are not only accurate but consistently close to real values — less than a quarter of a year off, on average.
 - 🔍 SHAP analysis confirms meaningful, interpretable predictions — this isn’t a black box, it’s a well-lit stage.
 - 🧪 Minimal overfitting — tight RMSE values across train/valid/test mean this model isn’t just memorizing data like a desperate med student before finals.

---

## 🛠️ Libraries Used

- `pandas`, `numpy`
- `scikit-learn`
- `xgboost`
- `matplotlib`, `seaborn`
- `shap`
- `ydata-profiling`

---

## 🚀 Run on Google Colab

Click the badge below to open and run the notebook in Colab:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1gih4vzTiKlrz8vr4d056G-v_IxRsTNPh?usp=drive_open#scrollTo=bpPySjzoUSwP)

---

## 📎 Author

**Mustansir Verdawala**
