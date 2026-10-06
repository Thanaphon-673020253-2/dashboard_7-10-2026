import streamlit as st
import plotly.express as px

def render_spatial_tab(df):
    st.subheader("Interactive Property Map")
    st.markdown("แผนที่แสดงทำเลที่ตั้งของอสังหาริมทรัพย์ ขนาดของจุดคือราคา สีคือประเภทอสังหาฯ")
    
    # We take a sample if the dataset is too large to prevent the browser from crashing
    map_data = df.copy()
    if len(map_data) > 5000:
        st.warning(f"Showing a sample of 5000 points from {len(map_data)} selected properties to optimize performance.")
        map_data = map_data.sample(5000, random_state=42)
        
    fig = px.scatter_mapbox(
        map_data, 
        lat="Latitude", 
        lon="Longitude", 
        color="Property Type",
        size="Price",
        hover_name="District",
        hover_data={"Price": True, "Price per Sqm": True, "Bedrooms": True, "Latitude": False, "Longitude": False},
        color_discrete_sequence=px.colors.qualitative.Set1,
        zoom=5, 
        height=600
    )
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Top 10 Districts by Average Price per Sqm")
    top_districts = df.groupby("District")["Price per Sqm"].mean().sort_values(ascending=False).head(10).reset_index()
    fig_bar = px.bar(top_districts, x="Price per Sqm", y="District", orientation='h', title="Top 10 Expensive Districts")
    fig_bar.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_bar, use_container_width=True)
