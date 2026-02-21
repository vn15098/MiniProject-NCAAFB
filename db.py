import streamlit as st
import psycopg2 

#configure postgres
def init_connection():
    return psycopg2.connect(**st.secrets["DB"]) 
