import streamlit as st

def render_valuation_tab(df):
    st.subheader("Opportunity Finder & Data Table")
    st.markdown("ตารางแสดงรายการอสังหาริมทรัพย์แบบเจาะลึก เพื่อค้นหาบ้านหรือคอนโดที่คุ้มค่าที่สุดในแต่ละย่าน")
    
    st.dataframe(
        df[['Province', 'District', 'Property Type', 'Price', 'Price per Sqm', 'Living Space (sqm)', 'Bedrooms', 'Bathrooms', 'Year Built']].sort_values(by="Price per Sqm", ascending=True),
        use_container_width=True,
        height=500
    )
