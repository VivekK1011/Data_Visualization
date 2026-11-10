# Data Visualization Portfolio Project

A beginner-friendly sales analytics project using **Python, Pandas, Matplotlib, Seaborn and Streamlit**.

## Project features
- Sample sales dataset (`data/sales_data.csv`)
- Exploratory analysis and three saved charts
- Interactive dashboard with region, category and product filters
- KPI cards for revenue, profit, units sold and profit margin
- Downloadable filtered data
- Automatically generated key takeaways

## 1. Open the project in VS Code
1. Extract `Data_Visualization.zip`.
2. Open VS Code.
3. Select **File → Open Folder** and choose the extracted `Data_Visualization` folder.
4. Open **Terminal → New Terminal**.

## 2. Create a virtual environment (recommended)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```
If PowerShell blocks activation, use:
```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 3. Install packages
```powershell
python -m pip install -r requirements.txt
```
If `python` is not recognized, use your Python executable path:
```powershell
& "C:\Users\YOUR_USER\AppData\Local\Programs\Python\Python314\python.exe" -m pip install -r requirements.txt
```

## 4. Generate static charts and analysis
```powershell
python analysis.py
```
The charts will be saved in the `outputs` folder:
- `monthly_revenue.png`
- `revenue_by_region.png`
- `correlation_heatmap.png`

## 5. Run the interactive dashboard
```powershell
python -m streamlit run app.py
```
Streamlit will show a local URL, usually `http://localhost:8501`. Open it in your browser.

## Dataset columns
| Column | Meaning |
|---|---|
| Date | Transaction date |
| Region | Sales region |
| Product | Product name |
| Category | Product category |
| Quantity | Units sold |
| Unit_Price_INR | Selling price per unit |
| Unit_Cost_INR | Cost per unit |
| Revenue_INR | Quantity × selling price |
| Profit_INR | Quantity × (selling price − unit cost) |

## Data story / example questions
- Which region contributes the most revenue?
- Which product contributes the most revenue?
- How does revenue change month by month?
- Which category generates the most profit?
- How do quantity, price, revenue and profit relate?

## Portfolio presentation tips
1. Run the analysis and dashboard.
2. Capture screenshots of the KPI cards and charts.
3. Add those screenshots to your project report or portfolio.
4. Explain one insight, one business implication and one recommendation.
5. Replace the sample CSV with a real dataset using the same column names to analyze your own data.

**Note:** The included data is synthetic demo data for learning and demonstration, not real company sales.
