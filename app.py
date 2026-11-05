import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Sales Insights Dashboard", page_icon="📊", layout="wide")
st.title("📊 Sales Insights Dashboard")
st.caption("Task 3 — Data Visualization | Explore sales, profit, products and regions.")

DATA = Path(__file__).parent / "data" / "sales_data.csv"
df = pd.read_csv(DATA)
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime("%b %Y")

st.sidebar.header("Dashboard Filters")
regions = st.sidebar.multiselect("Region", sorted(df["Region"].unique()), default=sorted(df["Region"].unique()))
categories = st.sidebar.multiselect("Category", sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))
products = st.sidebar.multiselect("Product", sorted(df["Product"].unique()), default=sorted(df["Product"].unique()))
filtered = df[df["Region"].isin(regions) & df["Category"].isin(categories) & df["Product"].isin(products)]

if filtered.empty:
    st.warning("No rows match these filters. Select at least one region, category and product.")
    st.stop()

revenue = filtered["Revenue_INR"].sum()
profit = filtered["Profit_INR"].sum()
units = filtered["Quantity"].sum()
margin = (profit / revenue * 100) if revenue else 0

c1,c2,c3,c4 = st.columns(4)
c1.metric("Total Revenue", f"₹{revenue:,.0f}")
c2.metric("Total Profit", f"₹{profit:,.0f}")
c3.metric("Units Sold", f"{units:,}")
c4.metric("Profit Margin", f"{margin:.1f}%")

monthly = filtered.groupby("Month", sort=False)[["Revenue_INR","Profit_INR"]].sum().reset_index()
monthly["MonthSort"] = pd.to_datetime(monthly["Month"], format="%b %Y")
monthly = monthly.sort_values("MonthSort")
left,right = st.columns(2)
with left:
    st.subheader("Monthly revenue trend")
    fig = px.line(monthly, x="Month", y="Revenue_INR", markers=True, title="Revenue by month",
                  labels={"Revenue_INR":"Revenue (₹)", "Month":"Month"})
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Revenue by region")
    region = filtered.groupby("Region", as_index=False)["Revenue_INR"].sum()
    fig = px.bar(region, x="Region", y="Revenue_INR", color="Region", title="Regional performance",
                 labels={"Revenue_INR":"Revenue (₹)"})
    st.plotly_chart(fig, use_container_width=True)

left,right = st.columns(2)
with left:
    st.subheader("Product revenue share")
    product = filtered.groupby("Product", as_index=False)["Revenue_INR"].sum()
    fig = px.pie(product, names="Product", values="Revenue_INR", hole=.45)
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Profit by category")
    cat = filtered.groupby("Category", as_index=False)["Profit_INR"].sum()
    fig = px.bar(cat, x="Category", y="Profit_INR", color="Category",
                 labels={"Profit_INR":"Profit (₹)"})
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Filtered data")
st.dataframe(filtered.sort_values("Date", ascending=False), use_container_width=True)
st.download_button("⬇️ Download filtered data (CSV)", filtered.to_csv(index=False).encode("utf-8"),
                   file_name="filtered_sales_data.csv", mime="text/csv")

best_product = product.sort_values("Revenue_INR", ascending=False).iloc[0]
best_region = region.sort_values("Revenue_INR", ascending=False).iloc[0]
st.subheader("Key takeaways")
st.write(f"- Highest-revenue product in the current selection: **{best_product['Product']}**.")
st.write(f"- Highest-revenue region in the current selection: **{best_region['Region']}**.")
st.write(f"- Current selection generated **₹{revenue:,.0f} revenue** and **₹{profit:,.0f} profit**.")
