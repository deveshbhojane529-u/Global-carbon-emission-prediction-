# 🌍 Global Carbon Emission Prediction (1960–2026)

This project applies **machine learning** to analyze and predict global carbon emissions.  
It combines **historical data (1960–2020)** with **projected values (2021–2026)**, providing insights into emission trends, country‑level comparisons, and sustainability planning.

---

##📌 References
• 	World Bank CO₂ Emissions Data →  (data.worldbank.org in Bing)
• 	Our World in Data – CO₂ and Greenhouse Gas Emissions Dataset → https://github.com/owid/co2-data
• 	Global Carbon Project → https://www.globalcarbonproject.org/
• 	IPCC Climate Reports → https://www.ipcc.ch/reports/

## 🌱 Sustainability Impact
- Supports **UN Sustainable Development Goal 13: Climate Action**.  
- Forecasting emissions helps policymakers design effective climate strategies.  
- Identifying high‑emission clusters guides targeted interventions.  
- Demonstrates how **AI can be leveraged for environmental sustainability**.

---

## 📊 Dataset
- **File:** `global_carbon_emissions_1960_2026.csv`  
- **Columns:**  
  - `Country` → India, USA, China, EU, Brazil, Japan, Russia, Africa  
  - `Year` → 1960–2026  
  - `CO2_Emissions` → Million tons of CO₂  
  - `Population` → Total population  
  - `GDP` → Gross Domestic Product (billions USD approx.)  
  - `Data_Type` → Historical or Projected  

**Note:**  
- 1960–2020 → Historical data (World Bank, Global Carbon Project).  
- 2021–2026 → Projected using ML models.  

---

## ⚙️ Methodology
1. **Data Cleaning & Preprocessing**  
2. **Exploratory Analysis** (trend graphs)  
3. **Feature Engineering** (per capita metrics)  
4. **Model Building**  
   - Linear Regression  
   - Ridge Regression  
   - Random Forest Regressor  
   - Decision Tree Classifier  
   - K‑Means Clustering  
5. **Evaluation Metrics**  
   - R² Score  
   - Mean Squared Error (MSE)  
   - Accuracy (classification)  

---

## 📈 Results
- **Global Trend Graph** → Emissions growth across countries (1960–2026).  
- **Regression Plot** → Actual vs predicted emissions (Linear Regression).  
- **Model Comparison** → Random Forest performed best (R² ≈ 0.90).  
- **Clustering Output** → K‑Means grouped countries into 3 realistic clusters.  

**Top Emitters in 2026 (Projected):**
1. China – ~11,100 Mt  
2. USA – ~6,220 Mt  
3. EU – ~4,420 Mt  
4. India – ~2,720 Mt  
5. Africa – ~2,380 Mt  

---

