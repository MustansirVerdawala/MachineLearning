# 🛒 Customer Segmentation using RFM Analysis & K-Means Clustering

This project performs customer segmentation on an **online retail dataset** using **RFM analysis** (Recency, Frequency, Monetary) and **K-Means clustering**. The goal is to identify different types of customers based on purchasing behavior, such as loyal customers, high spenders, and one-time buyers.

## 📂 Dataset
- **File Used:** `Online Retail.xlsx`
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/online+retail)
- Focused only on **customers in the United Kingdom**

## 📊 Features Engineered
- `TotalPrice`: `Quantity * UnitPrice`
- RFM:
  - **Recency**: Days since last purchase
  - **Frequency**: Number of unique invoices
  - **Monetary**: Total money spent

## 🧼 Data Cleaning
- Dropped null `CustomerID`
- Removed rows with non-positive `Quantity` or `UnitPrice`
- Filtered for transactions from **United Kingdom**

## 📈 Clustering
- Used **StandardScaler** to normalize RFM features
- Determined optimal clusters using:
  - **Elbow Method**
  - **Silhouette Scores**
- Final clustering done with **K=5**

## 📉 Visualization
- 3D scatter plot of RFM features colored by cluster
- 2D PCA projection for visual clarity
- Radar charts to visualize average behavior per cluster

## 🔍 Cluster Profiles (Interpretation)
- **Cluster 0**: High frequency, moderate spenders – likely regular, loyal customers.
- **Cluster 1**: Low frequency, low monetary – casual or first-time buyers.
- **Cluster 2**: Frequent and high spenders – VIPs. Your moneybags. Treat them like royalty.
- **Clusters 3 & 4**: Probably noise or outliers – niche or edge-case consumers.

## 🚀 Run on Google Colab
Click the badge below to open and run the notebook in Colab:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1F50fJu4N1SynH5cgAmy5Lb2yXKbWNVRO?usp=drive_open#scrollTo=L-UHrxRyR7Z7)

---

## 🛠️ Libraries Used
- `pandas`, `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `mpl_toolkits.mplot3d`
- `PCA`, `KMeans`, `silhouette_score`

---

## 📎 Author
**Mustansir Verdawala**  

