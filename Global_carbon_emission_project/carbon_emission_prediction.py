import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import r2_score, accuracy_score

# Ensure results folder exists
if not os.path.exists("results"):
    os.makedirs("results")

# Load dataset
data = pd.read_csv("global_carbon_emissions_1960_2020.csv")
data.dropna(inplace=True)

# Global Trend
plt.figure(figsize=(12,6))
sns.lineplot(x="Year", y="CO2_Emissions", data=data, hue="Country", marker="o")
plt.title("Global Carbon Emissions (1960–2020)")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions (Million Tons)")
plt.grid(True)
plt.savefig("results/global_trend.png")
plt.close()

# Feature Engineering
data["Emissions_per_capita"] = data["CO2_Emissions"] / data["Population"]
data["GDP_per_capita"] = data["GDP"] / data["Population"]

# Regression Models
X = data[["Year", "Population", "GDP", "GDP_per_capita"]]
y = data["CO2_Emissions"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

lr_model = LinearRegression().fit(X_train, y_train)
ridge_model = Ridge(alpha=1.0).fit(X_train, y_train)
rf_model = RandomForestRegressor(n_estimators=100, random_state=42).fit(X_train, y_train)

y_pred_lr = lr_model.predict(X_test)
y_pred_ridge = ridge_model.predict(X_test)
y_pred_rf = rf_model.predict(X_test)

print("Linear Regression R²:", r2_score(y_test, y_pred_lr))
print("Ridge Regression R²:", r2_score(y_test, y_pred_ridge))
print("Random Forest R²:", r2_score(y_test, y_pred_rf))

# Regression Plot
plt.figure(figsize=(10,6))
plt.scatter(X_test["Year"], y_test, color="blue", label="Actual")
plt.scatter(X_test["Year"], y_pred_lr, color="red", label="Predicted (Linear Regression)")
plt.title("Linear Regression Prediction of Carbon Emissions")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions")
plt.legend()
plt.savefig("results/regression_plot.png")
plt.close()

# Model Comparison Plot
plt.figure(figsize=(10,6))
plt.plot(y_test.values, label="Actual", marker="o")
plt.plot(y_pred_lr, label="Linear Regression", marker="x")
plt.plot(y_pred_ridge, label="Ridge Regression", marker="s")
plt.plot(y_pred_rf, label="Random Forest", marker="^")
plt.title("Model Comparison: Actual vs Predicted Emissions")
plt.xlabel("Test Samples")
plt.ylabel("CO2 Emissions")
plt.legend()
plt.savefig("results/model_comparison.png")
plt.close()

# Decision Tree Classification
def categorize_emission(value):
    if value > 5000: return "High"
    elif value > 2000: return "Medium"
    else: return "Low"

data["Emission_Category"] = data["CO2_Emissions"].apply(categorize_emission)

X_class = data[["Year", "Population", "GDP", "GDP_per_capita"]]
y_class = data["Emission_Category"]

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_class, y_class, test_size=0.3, random_state=42)

dt_model = DecisionTreeClassifier(max_depth=6, random_state=42).fit(X_train_c, y_train_c)
y_pred_c = dt_model.predict(X_test_c)

print("Decision Tree Accuracy:", accuracy_score(y_test_c, y_pred_c))

# K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(data[["CO2_Emissions", "GDP", "Population"]])
data["Cluster"] = clusters

plt.figure(figsize=(8,6))
sns.scatterplot(x="GDP", y="CO2_Emissions", hue="Cluster", data=data, palette="Set1", s=100)
plt.title("K-Means Clustering of Global Emission Patterns")
plt.xlabel("GDP")
plt.ylabel("CO2 Emissions")
plt.savefig("results/clustering_output.png")
plt.close()

# Insights
print("\n--- Insights ---")
print("Top Emitters in 2020:")
print(data[data["Year"] == 2020].sort_values("CO2_Emissions", ascending=False).head(5))