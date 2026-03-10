import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest

st.set_page_config(page_title="ATM Intelligence Dashboard", layout="wide")

st.title("ATM Intelligence Demand Forecasting Dashboard")

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv("atm_dataset.csv")

# Convert Date if present
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

st.header("Dataset Overview")
st.write(df.head())

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------

st.sidebar.header("Filters")

selected_day = st.sidebar.selectbox(
    "Select Day",
    df["Day_of_Week"].dropna().unique()
)

selected_location = st.sidebar.selectbox(
    "Location Type",
    df["Location_Type"].dropna().unique()
)

filtered_df = df[
    (df["Day_of_Week"] == selected_day) &
    (df["Location_Type"] == selected_location)
]

st.subheader("Filtered Data")
st.write(filtered_df)

# -----------------------------
# EDA SECTION
# -----------------------------

st.header("Exploratory Data Analysis")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Withdrawal Distribution")

    fig, ax = plt.subplots()
    sns.histplot(df["Total_Withdrawals"], kde=True, ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Deposit Distribution")

    fig, ax = plt.subplots()
    sns.histplot(df["Total_Deposits"], kde=True, ax=ax)
    st.pyplot(fig)

# Withdrawals by weekday

if "Day_of_Week" in df.columns:

    st.subheader("Withdrawals by Day of Week")

    fig, ax = plt.subplots()
    sns.barplot(x="Day_of_Week", y="Total_Withdrawals", data=df, ax=ax)
    st.pyplot(fig)

# Time trend

if "Date" in df.columns:

    st.subheader("Withdrawals Over Time")

    fig, ax = plt.subplots()
    sns.lineplot(x="Date", y="Total_Withdrawals", data=df, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Correlation heatmap

st.subheader("Correlation Heatmap")

fig, ax = plt.subplots()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# -----------------------------
# CLUSTERING ANALYSIS
# -----------------------------

st.header("ATM Clustering Analysis")

features = df[[
    "Total_Withdrawals",
    "Total_Deposits",
    "Nearby_Competitor_ATMs"
]].dropna()

scaler = StandardScaler()

scaled = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3, random_state=42)

df.loc[features.index, "Cluster"] = kmeans.fit_predict(scaled)

fig, ax = plt.subplots()

sns.scatterplot(
    x=df["Total_Withdrawals"],
    y=df["Total_Deposits"],
    hue=df["Cluster"],
    palette="viridis",
    ax=ax
)

st.pyplot(fig)

st.write("Cluster Meaning:")
st.write("Cluster 0 → Low Demand ATMs")
st.write("Cluster 1 → Medium Demand ATMs")
st.write("Cluster 2 → High Demand ATMs")

# -----------------------------
# ANOMALY DETECTION
# -----------------------------

st.header("Anomaly Detection")

model = IsolationForest(contamination=0.05)

df["Anomaly"] = model.fit_predict(
    df[["Total_Withdrawals"]]
)

fig, ax = plt.subplots()

sns.scatterplot(
    x=df.index,
    y=df["Total_Withdrawals"],
    hue=df["Anomaly"],
    palette=["blue", "red"],
    ax=ax
)

st.pyplot(fig)

st.write("Red points represent unusual withdrawal spikes.")

# -----------------------------
# ATM REFILL RECOMMENDATION
# -----------------------------

st.header("ATM Refill Recommendation")

atm_id = st.selectbox("Select ATM", df["ATM_ID"].dropna().unique())

atm_data = df[df["ATM_ID"] == atm_id]

avg_withdrawal = atm_data["Total_Withdrawals"].mean()

if pd.notna(avg_withdrawal):

    recommended_cash = avg_withdrawal * 1.25

    st.write("Average Withdrawal:", round(avg_withdrawal))

    st.write("Recommended Refill Amount:", round(recommended_cash))

else:

    st.write("Insufficient data for this ATM.")

# -----------------------------
# RISK LEVEL INDICATOR
# -----------------------------

st.header("ATM Demand Risk Level")

if pd.notna(avg_withdrawal):

    if avg_withdrawal > df["Total_Withdrawals"].quantile(0.75):

        st.error("High Risk ATM – refill urgently")

    elif avg_withdrawal > df["Total_Withdrawals"].quantile(0.50):

        st.warning("Medium Risk ATM")

    else:

        st.success("Low Risk ATM")

# -----------------------------
# AUTO INSIGHT GENERATOR
# -----------------------------

st.header("Key Insights from ATM Data")

if "Day_of_Week" in df.columns:

    highest_day = df.groupby("Day_of_Week")["Total_Withdrawals"].mean().idxmax()

    st.write(
        f"Highest average withdrawals occur on **{highest_day}**, indicating higher demand."
    )

# Safe weekend calculation

avg_weekend = df[df["Day_of_Week"].isin(["Saturday","Sunday"])]["Total_Withdrawals"].mean()

avg_weekday = df[~df["Day_of_Week"].isin(["Saturday","Sunday"])]["Total_Withdrawals"].mean()

if pd.notna(avg_weekend) and pd.notna(avg_weekday):

    st.write(
        f"Weekend withdrawals average **{round(avg_weekend)}**, compared to weekday average of **{round(avg_weekday)}**."
    )

else:

    st.write("Weekend data not available in the dataset.")

# Cluster insight

if "Cluster" in df.columns:

    high_cluster = df[df["Cluster"] == 2].shape[0]

    st.write(
        f"There are **{high_cluster} high-demand ATMs**, which may require more frequent cash refilling."
    )

st.success("Dashboard Loaded Successfully")