import streamlit as st
import pandas as pd
from db import init_connection

def show(): 
    connect = init_connection()
    st.markdown("<h4>Coaches data</h4>", unsafe_allow_html=True)
    query = """ SELECT c.coach_id,c.full_name,c.position,t.name as team_name FROM "Coaches" as c join "Teams" as t on c.team_id = t.team_id;"""
    df = pd.read_sql(query, connect)

    # Search box
    search_text = st.text_input("Search by Coach Name or Team Name")

    if search_text:
        mask = (
            df["full_name"].str.contains(search_text, case=False, na=False) |
            df["team_name"].str.contains(search_text, case=False, na=False) 
        )
        df = df[mask]

    # Display final filtered dataframe
    st.dataframe(df, use_container_width=True, hide_index=True)