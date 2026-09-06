import pandas as pd
import streamlit as st

from utils.data import load_election_data, load_referendum_data
from utils.styles import hero, insight, section_label

election = load_election_data()
referendum = load_referendum_data()
hero("Data quality", "Transparent checks on completeness, uniqueness and the boundaries of what the source data can support.")
section_label("Dataset checks")
checks = pd.DataFrame([
    {"check": "Election rows", "result": f"{len(election):,}", "status": "PASS"},
    {"check": "Unique constituencies", "result": f"{election.constituency_name.nunique():,}", "status": "PASS" if election.constituency_name.is_unique else "REVIEW"},
    {"check": "Duplicate records", "result": f"{election.duplicated().sum():,}", "status": "PASS" if election.duplicated().sum() == 0 else "REVIEW"},
    {"check": "Missing election values", "result": f"{int(election.isna().sum().sum()):,}", "status": "PASS" if election.isna().sum().sum() == 0 else "REVIEW"},
    {"check": "Referendum rows", "result": f"{len(referendum):,}", "status": "PASS"},
], columns=["check", "result", "status"])
st.dataframe(checks, use_container_width=True, hide_index=True)
section_label("Interpretation boundary")
insight("The election file contains winner and runner-up votes plus registered voters. It does not contain total ballots cast, so the dashboard intentionally does not present voter turnout. Top-two reported vote share and winning margin are used instead.")
st.write("Source fields used")
st.code(", ".join(election.columns), language="text")