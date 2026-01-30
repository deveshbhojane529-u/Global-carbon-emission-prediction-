# Global-carbon-emission-prediction-
Machine learning project predicting global carbon emissions using real data
# 🌍 Global Carbon Emission Prediction (1960–2020)

This project analyzes and predicts **global carbon emissions** using machine learning techniques.  
It combines historical data (1960–2020) from multiple countries and regions, providing insights into emission trends, country‑level comparisons, and predictive modeling.

---

## 📊 Dataset
- **Source References:**
  - [World Bank CO₂ Emissions Data](https://data.worldbank.org/indicator/EN.ATM.CO2E.KT)
  - [Global Carbon Project](https://www.globalcarbonproject.org/)
  - [IPCC Climate Reports](https://www.ipcc.ch/reports/)
- **Features:**
  - `Country` – Nation/region name
  - `Year` – 1960–2020
  - `CO2_Emissions` – Million tons of CO₂
  - `Population` – Population size
  - `GDP` – Gross Domestic Product (Billion USD)
- **Derived Features:**
  - `Emissions_per_capita`
  - `GDP_per_capita`

---

## ⚙️ Methodology
1. **Data Cleaning** – Handle missing values, normalize features.  
2. **Exploratory Analysis** – Line charts of emissions by country.  
3. **Feature Engineering** – Per capita emissions, GDP per capita.  
4. **Model Building**:
   - Linear Regression
   - Ridge Regression
   - Random Forest Regressor
   - Decision Tree Classifier
   - K-Means Clustering  
5. **Evaluation Metrics**:
   - R² Score
   - Mean Squared Error (MSE)
   - Accuracy (for classification)

---

## 📈 Results
- **Global Trend Graph** → Emissions growth across countries (1960–2020).  
- **Regression Plot** → Actual vs predicted emissions (Linear Regression).  
- **Model Comparison** → Linear, Ridge, Random Forest (Random Forest performed best, R² ≈ 0.90).  
- **Clustering Output** → K-Means grouped countries into 3 realistic clusters (high, medium, low emitters).  
- **Top Emitters in 2020**:
  1. China – 10,000 Mt  
  2. USA – 6,000 Mt  
  3. EU – 4,200 Mt  
  4. India – 2,400 Mt  
  5. Africa – 2,000 Mt  

---
