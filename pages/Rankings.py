import streamlit as st
import pandas as pd
from db import init_connection

def show(): 
    connect = init_connection()
    st.markdown("<h4>Rankings data</h4>", unsafe_allow_html=True)
    query = """ SELECT r.ranking_id,r.season_id,r.poll_id,r.week,t.name as team_name,r.rank,r.points,r.fp_votes,r.wins,r.losses FROM public."Rankings" 
    as r JOIN "Teams" as t on r.team_id = t.team_id;"""
    df = pd.read_sql(query, connect)

    # Put filters side by side
    col1, col2, col3 = st.columns(3)

    with col1:
        seasonList = df["season_id"].unique()
        seasonFilter = st.selectbox("Filter by Season", options=["All"] + list(seasonList))

    with col2:
        weekList = df["week"].unique()
        weekFilter = st.selectbox("Filter by Week", options=["All"] + list(weekList))

    with col3:
        # Range slider for numbers 
        start, end = st.slider( "Select a range of Rank", min_value=0, max_value=100, value=(0, 20) )
    
    # Apply dropdown filters
    if seasonFilter != "All":
        df = df[df["season_id"] == seasonFilter]

    if weekFilter != "All":
        df = df[df["week"] == weekFilter]

    df = df[(df["rank"] >= start) & (df["rank"] <= end)]

    # Search box
    search_text = st.text_input("Search by team name")

    if search_text:
        df = df[df["team_name"].str.contains(search_text, case=False, na=False)]

    print(st.dataframe(df, use_container_width=True))