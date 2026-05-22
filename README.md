# Terminal Operations Analytics Dashboard

## Project Overview
This project is a simulated operations analytics system for a multi-modal transport terminal in Iloilo, Philippines. It analyzes vehicle flow, congestion behavior, queue formation, dwell time, and route-level pressure across different transport modes including Jeepneys, Modern Jeepneys, UV Express vans, and Provincial Buses.

The goal is to understand how terminal congestion forms and how operations can be optimized using data-driven insights.

---

## Problem Statement
Transport terminals often experience:
- unpredictable jeepney arrival patterns
- peak-hour congestion spikes
- inefficient lane utilization
- long dwell times during high-demand periods
- route-level overcrowding

This project models these issues using synthetic operational data and provides analytical insights and a dashboard interface.

---

## Tools Used
- Python
- Streamlit
- Pandas
- NumPy
- GitHub
- Google Sheets (for data generation)

---

## Features

### 1. Interactive Dashboard
- Filters by route and vehicle type
- Dynamic KPI updates

### 2. Key Metrics
- Total vehicles processed
- Average congestion level
- Average dwell time
- Peak congestion hour detection

### 3. Visual Analytics
- Vehicle type distribution
- Congestion over time (hourly)
- Route pressure analysis
- Congestion heatmap

### 4. Operational Intelligence
- System status indicator (Stable / High Load / Critical)
- High-risk route detection
- Peak hour congestion analysis

---

## Key Insights
- Jeepneys dominate terminal flow and drive congestion clustering
- Peak congestion occurs during morning (7–9 AM) and afternoon (4–7 PM)
- Route demand is uneven, with certain corridors consistently overloaded
- Dwell time increases significantly during peak congestion periods
- System performance is highly sensitive to arrival clustering behavior

---

## Project Structure

```text
terminal-operations-analytics/
│
├── app.py
├── requirements.txt
├── README.md
│
└── data/
    └── terminal_data.csv
How to Run Locally
1. Install dependencies
pip install -r requirements.txt
2. Run Streamlit app
streamlit run app.py
Purpose of Project

This project was built as a portfolio case study for data analytics and operations analytics roles, demonstrating skills in:

data cleaning
exploratory data analysis
dashboard development
operational insight generation
real-world system modeling
Author

Student project focused on transportation systems, operations analytics, and data-driven decision making.# Terminal Operations Analytics Dashboard

## Project Overview
This project is a simulated operations analytics system for a multi-modal transport terminal in Iloilo, Philippines. It analyzes vehicle flow, congestion behavior, queue formation, dwell time, and route-level pressure across different transport modes including Jeepneys, Modern Jeepneys, UV Express vans, and Provincial Buses.

The goal is to understand how terminal congestion forms and how operations can be optimized using data-driven insights.

---

## Problem Statement
Transport terminals often experience:
- unpredictable jeepney arrival patterns
- peak-hour congestion spikes
- inefficient lane utilization
- long dwell times during high-demand periods
- route-level overcrowding

This project models these issues using synthetic operational data and provides analytical insights and a dashboard interface.

---

## Tools Used
- Python
- Streamlit
- Pandas
- NumPy
- GitHub
- Google Sheets (for data generation)

---

## Features

### 1. Interactive Dashboard
- Filters by route and vehicle type
- Dynamic KPI updates

### 2. Key Metrics
- Total vehicles processed
- Average congestion level
- Average dwell time
- Peak congestion hour detection

### 3. Visual Analytics
- Vehicle type distribution
- Congestion over time (hourly)
- Route pressure analysis
- Congestion heatmap

### 4. Operational Intelligence
- System status indicator (Stable / High Load / Critical)
- High-risk route detection
- Peak hour congestion analysis

---

## Key Insights
- Jeepneys dominate terminal flow and drive congestion clustering
- Peak congestion occurs during morning (7–9 AM) and afternoon (4–7 PM)
- Route demand is uneven, with certain corridors consistently overloaded
- Dwell time increases significantly during peak congestion periods
- System performance is highly sensitive to arrival clustering behavior

---

## Project Structure

terminal-operations-analytics/
│
├── app.py
├── requirements.txt
├── README.md
│
└── data/
    └── terminal_data.csv
How to Run Locally
1. Install dependencies
pip install -r requirements.txt
2. Run Streamlit app
streamlit run app.py

Purpose of Project
This project was built as a portfolio case study for data analytics and operations analytics roles, demonstrating skills in:

data cleaning
exploratory data analysis
dashboard development
operational insight generation
real-world system modeling

Author
Student project focused on transportation systems, operations analytics, and data-driven decision making.
