import streamlit as st
import pandas as pd
from db import init_connection

def show(): 
    connect = init_connection()
    st.markdown("<h4>Seasons data</h4>", unsafe_allow_html=True)
    query = """ SELECT s.season_id, s.start_date, s.end_date,s.status,s.year,r.ranking_id FROM "Seasons" AS s JOIN  "Rankings" AS r
    ON s.season_id = r.season_id; """ 
    df = pd.read_sql(query, connect)
    
    # Put filters side by side
    col1, col2 = st.columns(2)

    with col1:
        yearList = df["year"].unique()
        yearFilter = st.selectbox("Filter by Year", options=["All"] + list(yearList))

    with col2:
        statusList = df["status"].unique()
        statusFilter = st.selectbox("Filter by Status", options=["All"] + list(statusList))
    
    # Apply dropdown filters
    if yearFilter != "All":
        df = df[df["year"] == yearFilter]

    if statusFilter != "All":
        df = df[df["status"] == statusFilter]

    # Display final filtered dataframe
    st.dataframe(df, use_container_width=True, hide_index=True)