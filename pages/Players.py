import streamlit as st
import pandas as pd
from db import init_connection

def show():
    connect = init_connection() 
    st.markdown("<h4>Players data</h4>", unsafe_allow_html=True)
    query = """SELECT "player_id",CONCAT(first_name, ' ', last_name) AS full_name,"position","eligibility","status","height","weight" FROM public."Players";"""
    df = pd.read_sql(query, connect)

    # Put filters side by side
    col1, col2 = st.columns(2)

    with col1:
        positionList = df["position"].unique()
        positionFilter = st.selectbox("Filter by Position", options=["All"] + list(positionList))

    with col2:
        statusList = df["status"].unique()
        statusFilter = st.selectbox("Filter by Status", options=["All"] + list(statusList))
    
    # Apply dropdown filters
    if positionFilter != "All":
        df = df[df["position"] == positionFilter]

    if statusFilter != "All":
        df = df[df["status"] == statusFilter]

    # Search box
    search_text = st.text_input("Search by Player Name")

    if search_text:
        mask = (
            df["full_name"].str.contains(search_text, case=False, na=False) 
        )
        df = df[mask]

    # Display final filtered dataframe
    st.dataframe(df, use_container_width=True, hide_index=True)