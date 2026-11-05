from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "sales_data.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)
sns.set_theme(style="whitegrid")


monthly = df.groupby("Month", as_index=False)["Revenue_INR"].sum()
plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly, x="Month", y="Revenue_INR", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month"); plt.ylabel("Revenue (INR)")
plt.xticks(rotation=30); plt.tight_layout()
plt.savefig(OUT / "monthly_revenue.png", dpi=160); plt.close()


region = df.groupby("Region", as_index=False)["Revenue_INR"].sum().sort_values("Revenue_INR", ascending=False)
plt.figure(figsize=(8, 5))
sns.barplot(data=region, x="Region", y="Revenue_INR")
plt.title("Revenue by Region"); plt.xlabel("Region"); plt.ylabel("Revenue (INR)")
plt.tight_layout(); plt.savefig(OUT / "revenue_by_region.png", dpi=160); plt.close()


numeric = df[["Quantity", "Unit_Price_INR", "Unit_Cost_INR", "Revenue_INR", "Profit_INR"]]
plt.figure(figsize=(8, 6))
sns.heatmap(numeric.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Sales Metrics Correlation")
plt.tight_layout(); plt.savefig(OUT / "correlation_heatmap.png", dpi=160); plt.close()


summary = {
    "Total revenue (INR)": df["Revenue_INR"].sum(),
    "Total profit (INR)": df["Profit_INR"].sum(),
    "Units sold": df["Quantity"].sum(),
    "Average order revenue (INR)": df["Revenue_INR"].mean(),
    "Rows": len(df),
    "Missing values": int(df.isna().sum().sum())
}
print("\\nSALES ANALYSIS SUMMARY")
for key, value in summary.items():
    print(f"{key}: {value:,.2f}" if isinstance(value, (int, float)) else f"{key}: {value}")
print("\\nTop product by revenue:")
print(df.groupby("Product")["Revenue_INR"].sum().sort_values(ascending=False).head(1))
print(f"\\nCharts saved in: {OUT}")
