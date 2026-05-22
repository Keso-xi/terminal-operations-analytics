import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Terminal Ops Dashboard", layout="wide")

st.title("Terminal Operations Analytics Dashboard")

# ======================
# LOAD DATA
# ======================

df = pd.read_csv("terminal_data.csv")
df["Hour"] = pd.to_datetime(df["Timestamp"], errors="coerce").dt.hour

# ======================
# SIDEBAR FILTERS
# ======================

st.sidebar.header("Filters")

route_filter = st.sidebar.multiselect(
    "Route",
    options=df["Route"].unique(),
    default=df["Route"].unique()
)

vehicle_filter = st.sidebar.multiselect(
    "Vehicle Type",
    options=df["Vehicle_Type"].unique(),
    default=df["Vehicle_Type"].unique()
)

filtered_df = df[
    (df["Route"].isin(route_filter)) &
    (df["Vehicle_Type"].isin(vehicle_filter))
]

# ======================
# KPI ROW (EXECUTIVE STYLE)
# ======================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Vehicles", len(filtered_df))
col2.metric("Avg Congestion", round(filtered_df["Congestion_Level"].mean(), 2))
col3.metric("Avg Dwell Time", round(filtered_df["Dwell_Time"].mean(), 2))
col4.metric("Peak Hour", filtered_df.groupby("Hour")["Congestion_Level"].mean().idxmax())

# ======================
# HEATMAP (CORE UPGRADE)
# ======================

st.subheader("Congestion Heatmap (Hour vs Congestion Level)")

heatmap_data = filtered_df.pivot_table(
    index="Hour",
    values="Congestion_Level",
    aggfunc="mean"
)

st.bar_chart(heatmap_data)

# ======================
# VEHICLE DISTRIBUTION
# ======================

st.subheader("Vehicle Flow Distribution")
st.bar_chart(filtered_df["Vehicle_Type"].value_counts())

# ======================
# ROUTE PRESSURE
# ======================

st.subheader("Route Pressure Index")
route_pressure = filtered_df.groupby("Route")["Queue_Size"].mean()
st.bar_chart(route_pressure)

# ======================
# PEAK INTELLIGENCE
# ======================

st.subheader("Peak Congestion Intelligence")

hourly = filtered_df.groupby("Hour")["Congestion_Level"].mean()

peak_hour = hourly.idxmax()
peak_value = hourly.max()

st.write(f"**Peak Hour:** {peak_hour}:00")
st.write(f"**Peak Congestion Level:** {round(peak_value, 2)}")

# ======================
# SYSTEM STATUS ENGINE
# ======================

avg_cong = filtered_df["Congestion_Level"].mean()

if avg_cong >= 4:
    st.error("SYSTEM STATUS: CRITICAL")
elif avg_cong >= 3:
    st.warning("SYSTEM STATUS: HIGH LOAD")
else:
    st.success("SYSTEM STATUS: STABLE")

# ======================
# RAW DATA (PORTFOLIO READY)
# ======================

st.subheader("Filtered Dataset")

st.dataframe(filtered_df)

# Download button
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_terminal_data.csv",
    mime="text/csv"
)