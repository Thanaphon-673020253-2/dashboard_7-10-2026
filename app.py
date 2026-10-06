import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).parent))

from utils.data_loader import load_real_estate_data
from components.tab1_spatial import render_spatial_tab
from components.tab2_specs import render_specs_tab
from components.tab3_valuation import render_valuation_tab

# Page Config
st.set_page_config(page_title="Thailand Real Estate Dashboard", layout="wide", page_icon="🏠")

st.title("🏠 Thailand Real Estate Dashboard")
st.markdown("ระบบติดตามและวิเคราะห์ตลาดอสังหาริมทรัพย์ในประเทศไทย")

# Load Data
@st.cache_data
def get_data():
    return load_real_estate_data()

try:
    df = get_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Filter Panel (Sidebar)
st.sidebar.header("🔍 Filters")

# Property Type Filter
prop_types = st.sidebar.multiselect("Property Type", options=df["Property Type"].unique(), default=df["Property Type"].unique())

# Province Filter
provinces = st.sidebar.multiselect("Province", options=sorted(df["Province"].unique()), default=[])
if not provinces:
    provinces = df["Province"].unique()

# Price Range Filter
min_price = float(df["Price"].min())
max_price = float(df["Price"].max())
price_range = st.sidebar.slider("Price Range (Baht)", min_value=min_price, max_value=max_price, value=(min_price, max_price), step=100000.0)

# Filter Data
filtered_df = df[
    (df["Property Type"].isin(prop_types)) &
    (df["Province"].isin(provinces)) &
    (df["Price"] >= price_range[0]) &
    (df["Price"] <= price_range[1])
]

# Top KPIs
st.subheader("Key Performance Indicators")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric(label="Total Properties", value=f"{len(filtered_df):,}")
kpi2.metric(label="Average Price", value=f"฿{filtered_df['Price'].mean():,.0f}")
kpi3.metric(label="Median Price/Sqm", value=f"฿{filtered_df['Price per Sqm'].median():,.0f}")
kpi4.metric(label="Average Space (sqm)", value=f"{filtered_df['Living Space (sqm)'].mean():,.1f}")

st.markdown("---")

# Tabs
tab1, tab2, tab3 = st.tabs(["🗺️ Spatial Analysis", "📊 Price Drivers", "💡 Opportunity Finder"])

with tab1:
    render_spatial_tab(filtered_df)
    
with tab2:
    render_specs_tab(filtered_df)
    
with tab3:
    render_valuation_tab(filtered_df)
