import streamlit as st
import pandas as pd
from db import init_connection


def show(): 
    connect = init_connection()
    st.markdown("<h4>Teams data</h4>", unsafe_allow_html=True)
    query = """ SELECT 
    t.team_id,
    t.name AS team_name,
    t.alias AS team_alias,
    c.name AS conference_name,
	v.name AS venue_name,
	v.state AS venue_state
FROM "Teams" AS t
JOIN "Conferences" AS c
    ON t.conference_id = c.conference_id
JOIN "Venues" AS v
	ON t.venue_id = v.venue_id; """

    df = pd.read_sql(query, connect)

   # Put filters side by side
    col1, col2 = st.columns(2)

    with col1:
        conferencesList = df["conference_name"].unique()
        conferenceFilter = st.selectbox("Filter by Conferences", options=["All"] + list(conferencesList))

    with col2:
        stateList = df["venue_state"].unique()
        stateFilter = st.selectbox("Filter by Venue", options=["All"] + list(stateList))

    # Apply dropdown filters
    if conferenceFilter != "All":
        df = df[df["conference_name"] == conferenceFilter]

    if stateFilter != "All":
        df = df[df["venue_state"] == stateFilter]

    # Search box
    search_text = st.text_input("Search by Team Name/Alias, Conference, or Venue")

    if search_text:
        mask = (
            df["team_name"].str.contains(search_text, case=False, na=False) |
            df["team_alias"].str.contains(search_text, case=False, na=False) |
            df["conference_name"].str.contains(search_text, case=False, na=False) |
            df["venue_name"].str.contains(search_text, case=False, na=False)
        )
        df = df[mask]

    # Display final filtered dataframe
    st.dataframe(df, use_container_width=True, hide_index=True)
