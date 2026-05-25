import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Page setup
st.set_page_config(
    page_title="Panem Demand Dashboard",
    layout="wide"
)

st.title("Panem Sales and Demand Prediction Dashboard")

st.write(
    "This dashboard uses the Excel datasource created from the Panem machine learning challenge. "
    "It includes historical sales data, model performance results, and business scenario predictions."
)

# Load Excel file
excel_file = "Panem_Dashboard_Datasource.xlsx"

if not os.path.exists(excel_file):
    st.error("Excel file not found. Make sure Panem_Dashboard_Datasource.xlsx is in the same folder as app.py.")
    st.stop()

daily_sales = pd.read_excel(excel_file, sheet_name="Daily_Sales")
model_results = pd.read_excel(excel_file, sheet_name="Model_Results")
scenario_predictions = pd.read_excel(excel_file, sheet_name="Scenario_Predictions")

# Clean column names
daily_sales.columns = daily_sales.columns.str.strip()
model_results.columns = model_results.columns.str.strip()
scenario_predictions.columns = scenario_predictions.columns.str.strip()

# Fix missing branch column
if "branch" not in daily_sales.columns:
    branch_dummy_cols = [col for col in daily_sales.columns if col.startswith("branch_")]

    if len(branch_dummy_cols) > 0:
        daily_sales["branch"] = daily_sales[branch_dummy_cols].idxmax(axis=1).str.replace("branch_", "")
        daily_sales.loc[daily_sales[branch_dummy_cols].sum(axis=1) == 0, "branch"] = "Reference branch"
    else:
        daily_sales["branch"] = "All branches"

# Fix basic column names if needed
if "item" not in daily_sales.columns:
    possible_item_cols = ["product", "Product", "item_name", "name"]
    for col in possible_item_cols:
        if col in daily_sales.columns:
            daily_sales = daily_sales.rename(columns={col: "item"})
            break

if "quantity" not in daily_sales.columns:
    possible_quantity_cols = ["Quantity", "units", "Units Sold", "units_sold"]
    for col in possible_quantity_cols:
        if col in daily_sales.columns:
            daily_sales = daily_sales.rename(columns={col: "quantity"})
            break

if "operating_date" not in daily_sales.columns:
    possible_date_cols = ["date", "Date", "fecha", "operating day"]
    for col in possible_date_cols:
        if col in daily_sales.columns:
            daily_sales = daily_sales.rename(columns={col: "operating_date"})
            break

# Stop if required columns are still missing
required_columns = ["operating_date", "branch", "item", "quantity"]

missing_columns = [col for col in required_columns if col not in daily_sales.columns]

if missing_columns:
    st.error(f"Missing required columns: {missing_columns}")
    st.write("Available columns in Daily_Sales:")
    st.write(daily_sales.columns.tolist())
    st.stop()

# Prepare date and day columns

daily_sales["operating_date"] = pd.to_datetime(daily_sales["operating_date"], errors="coerce")
daily_sales = daily_sales.dropna(subset=["operating_date"])

if "day_of_week" not in daily_sales.columns:
    daily_sales["day_of_week"] = daily_sales["operating_date"].dt.dayofweek

day_names = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

daily_sales["day_name"] = daily_sales["day_of_week"].map(day_names)


# Sidebar filters

st.sidebar.header("Filters")

selected_branches = st.sidebar.multiselect(
    "Select branch",
    options=sorted(daily_sales["branch"].dropna().unique()),
    default=sorted(daily_sales["branch"].dropna().unique())
)

selected_products = st.sidebar.multiselect(
    "Select product",
    options=sorted(daily_sales["item"].dropna().unique()),
    default=sorted(daily_sales["item"].dropna().unique())[:5]
)

date_range = st.sidebar.date_input(
    "Select date range",
    value=[
        daily_sales["operating_date"].min().date(),
        daily_sales["operating_date"].max().date()
    ]
)

# Filter data

filtered_data = daily_sales[
    (daily_sales["branch"].isin(selected_branches)) &
    (daily_sales["item"].isin(selected_products))
]

if len(date_range) == 2:
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

    filtered_data = filtered_data[
        (filtered_data["operating_date"] >= start_date) &
        (filtered_data["operating_date"] <= end_date)
    ]

if filtered_data.empty:
    st.warning("No data available with the selected filters.")
    st.stop()


# Main KPIs

st.subheader("Main Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Units Sold", f"{filtered_data['quantity'].sum():,.0f}")
col2.metric("Products Selected", filtered_data["item"].nunique())
col3.metric("Branches Selected", filtered_data["branch"].nunique())
col4.metric("Average Units per Record", f"{filtered_data['quantity'].mean():.2f}")


# Historical sales analysis

st.subheader("Historical Sales Analysis")

col1, col2 = st.columns(2)

branch_sales = (
    filtered_data
    .groupby("branch")["quantity"]
    .sum()
    .reset_index()
)

fig_branch = px.bar(
    branch_sales,
    x="branch",
    y="quantity",
    title="Total Units Sold by Branch",
    text_auto=True
)

col1.plotly_chart(fig_branch, use_container_width=True)

top_products = (
    filtered_data
    .groupby("item")["quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_products = px.bar(
    top_products,
    x="quantity",
    y="item",
    orientation="h",
    title="Top 10 Products by Units Sold",
    text_auto=True
)

col2.plotly_chart(fig_products, use_container_width=True)

sales_time = (
    filtered_data
    .groupby("operating_date")["quantity"]
    .sum()
    .reset_index()
)

fig_time = px.line(
    sales_time,
    x="operating_date",
    y="quantity",
    title="Units Sold Over Time"
)

st.plotly_chart(fig_time, use_container_width=True)

weekday_sales = (
    filtered_data
    .groupby(["day_of_week", "day_name"])["quantity"]
    .sum()
    .reset_index()
    .sort_values("day_of_week")
)

fig_weekday = px.bar(
    weekday_sales,
    x="day_name",
    y="quantity",
    title="Units Sold by Day of the Week",
    text_auto=True
)

st.plotly_chart(fig_weekday, use_container_width=True)

with st.expander("View filtered historical data"):
    st.dataframe(filtered_data)


# Machine learning model results

st.subheader("Machine Learning Model Results")

st.write(
    "This section shows how the Gradient Boosting model performed compared with a simple baseline. "
    "Lower RMSE means better prediction performance."
)

with st.expander("View model results table"):
    st.dataframe(model_results)

if "product" not in model_results.columns:
    model_results = model_results.rename(columns={model_results.columns[0]: "product"})

col1, col2 = st.columns(2)

if "RMSE" in model_results.columns and "Baseline_RMSE" in model_results.columns:
    fig_rmse = px.bar(
        model_results,
        x="product",
        y=["Baseline_RMSE", "RMSE"],
        barmode="group",
        title="Baseline RMSE vs Model RMSE"
    )

    col1.plotly_chart(fig_rmse, use_container_width=True)
else:
    col1.warning("RMSE columns were not found in Model_Results.")

if "Improvement_%" in model_results.columns:
    fig_improvement = px.bar(
        model_results,
        x="product",
        y="Improvement_%",
        title="Model Improvement Percentage",
        text_auto=True
    )

    col2.plotly_chart(fig_improvement, use_container_width=True)
else:
    col2.warning("Improvement_% column was not found in Model_Results.")


# Business scenario predictions

st.subheader("Business Scenario Predictions")

st.write(
    "This section connects the machine learning model to business decisions. "
    "It compares predicted demand against the baseline for different scenarios."
)

with st.expander("View scenario predictions table"):
    st.dataframe(scenario_predictions)

required_scenario_cols = ["scenario", "predicted_quantity", "baseline", "difference"]

missing_scenario_cols = [
    col for col in required_scenario_cols
    if col not in scenario_predictions.columns
]

if missing_scenario_cols:
    st.warning(f"Some scenario columns are missing: {missing_scenario_cols}")
    st.write("Available columns in Scenario_Predictions:")
    st.write(scenario_predictions.columns.tolist())
else:
    fig_scenario = px.bar(
        scenario_predictions,
        x="scenario",
        y=["predicted_quantity", "baseline"],
        barmode="group",
        title="Predicted Quantity vs Baseline by Scenario"
    )

    st.plotly_chart(fig_scenario, use_container_width=True)

    fig_difference = px.bar(
        scenario_predictions,
        x="scenario",
        y="difference",
        title="Difference Between Prediction and Baseline",
        text_auto=True
    )

    st.plotly_chart(fig_difference, use_container_width=True)


# Final interpretation

st.subheader("Dashboard Interpretation")

st.write(
    "The dashboard helps Panem understand which branches and products generate the most demand, "
    "how sales change over time, and how the machine learning model can support inventory and promotion decisions. "
    "The model results show whether the predictive model performs better than a basic baseline, while the scenario "
    "predictions translate the model into practical business cases."
)