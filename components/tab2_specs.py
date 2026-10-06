import streamlit as st
import plotly.express as px

def render_specs_tab(df):
    st.subheader("Price Distribution by Property Type")
    
    fig_box = px.box(df, x="Property Type", y="Price", color="Property Type", log_y=True,
                     title="Price Spread (Log Scale) across Property Types")
    st.plotly_chart(fig_box, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Living Space vs Price")
        fig_scatter = px.scatter(df, x="Living Space (sqm)", y="Price", color="Property Type", 
                                 log_x=True, log_y=True, trendline="ols",
                                 title="Space vs Price Correlation (Log Scale)")
        st.plotly_chart(fig_scatter, use_container_width=True)
        
    with col2:
        st.subheader("Year Built Trends")
        # Filter realistic years
        trend_df = df[(df['Year Built'] > 1950) & (df['Year Built'] <= 2026)]
        yearly_avg = trend_df.groupby("Year Built")["Price"].mean().reset_index()
        fig_line = px.line(yearly_avg, x="Year Built", y="Price", title="Average Price by Year Built")
        st.plotly_chart(fig_line, use_container_width=True)
