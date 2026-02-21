import streamlit as st
import pandas as pd
from db import init_connection

def show(): 
    connect = init_connection()
    st.markdown("<h4>Venues data</h4>", unsafe_allow_html=True)
    query = """ SELECT name,city,state,capacity,roof_type FROM public."Venues";"""
    df = pd.read_sql(query, connect)

    # Put filters side by side
    col1, col2 = st.columns(2)

    with col1:
        stateList = df["state"].unique()
        stateFilter = st.selectbox("Filter by State", options=["All"] + list(stateList))

    with col2:
        roofList = df["roof_type"].unique()
        roofFilter = st.selectbox("Filter by Roof Type", options=["All"] + list(roofList))
    
    # Apply dropdown filters
    if stateFilter != "All":
        df = df[df["state"] == stateFilter]

    if roofFilter != "All":
        df = df[df["roof_type"] == roofFilter]

    # Display final filtered dataframe
    st.dataframe(df, use_container_width=True, hide_index=True)