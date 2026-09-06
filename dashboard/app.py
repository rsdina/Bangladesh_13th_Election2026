import streamlit as st

from utils.data import load_election_data
from utils.styles import inject_styles

st.set_page_config(page_title="Bangladesh Election 2026 Analytics", page_icon="🗳️", layout="wide", initial_sidebar_state="expanded")
inject_styles()
load_election_data()

pages = [
    st.Page("pages/overview.py", title="Overview", icon="🏠"),
    st.Page("pages/electoral.py", title="Electoral Analysis", icon="🗳️"),
    st.Page("pages/demographic.py", title="Demographic Analysis", icon="👥"),
    st.Page("pages/socioeconomic.py", title="Socioeconomic Analysis", icon="📊"),
    st.Page("pages/party.py", title="Party Analysis", icon="🏛️"),
    st.Page("pages/constituency.py", title="Constituency Explorer", icon="🔎"),
    st.Page("pages/geographic.py", title="Geographic Analysis", icon="🗺️"),
    st.Page("pages/referendum.py", title="Referendum Analysis", icon="🗳️"),
    st.Page("pages/quality.py", title="Data Quality", icon="🧹"),
]
st.navigation(pages).run()