import streamlit as st
import pages.Coaches as Coaches
import pages.Players as Players
import pages.Rankings as Rankings
import pages.Seasons as Seasons
import pages.Teams as Teams
import pages.Venues as Venues

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>NCAAFB Data Analysis</h1>", unsafe_allow_html=True)

# Read query parameter to decide which page to show 
page = st.query_params.get("page") or "Teams"

# Navbar HTML
st.markdown(f"""
    <style>
        .navbar {{
            display: flex;
            justidfy-content: center !important;
            gap: 20px;
            background-color: #f0f0f0;
            padding: 10px;
        }}
        .nav-item {{
            padding: 8px 16px;
            text-decoration: none !important;
            border-radius: 4px;
        }}
        .nav-item.active {{
            background-color: green;
            color: white;
        }}
    </style>
    <div class="navbar">
        <a class="nav-item {'active' if page=='Teams' else ''}" href="?page=Teams">Teams</a>
        <a class="nav-item {'active' if page=='Coaches' else ''}" href="?page=Coaches">Coaches</a>
        <a class="nav-item {'active' if page=='Players' else ''}" href="?page=Players">Players</a>
        <a class="nav-item {'active' if page=='Rankings' else ''}" href="?page=Rankings">Rankings</a>
        <a class="nav-item {'active' if page=='Seasons' else ''}" href="?page=Seasons">Seasons</a>
        <a class="nav-item {'active' if page=='Venues' else ''}" href="?page=Venues">Venues</a>
    </div>
""", unsafe_allow_html=True)

# Page content
if page == "Teams":
    Teams.show()
elif page == "Coaches":
    Coaches.show()
elif page == "Players":
    Players.show()
elif page == "Rankings":
    Rankings.show()
elif page == "Seasons":
    Seasons.show()
elif page == "Venues":
    Venues.show()





