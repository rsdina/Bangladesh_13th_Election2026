import streamlit as st

from utils.data import load_election_data
from utils.styles import hero, section_label

df = load_election_data()
hero("Constituency explorer", "Search a constituency, filter by division or party, and inspect the reported contest profile.")
section_label("Filters")
left, middle, right = st.columns(3)
with left:
    query = st.text_input("Search name or number", placeholder="e.g. Panchagarh-1")
with middle:
    division = st.selectbox("Division", ["All"] + sorted(df.division.dropna().unique().tolist()))
with right:
    party = st.selectbox("Winning party", ["All"] + sorted(df.winner_party.dropna().unique().tolist()))
filtered = df.copy()
if query:
    filtered = filtered[filtered.constituency_name.str.contains(query, case=False, na=False) | filtered.constituency_no.astype(str).eq(query)]
if division != "All":
    filtered = filtered[filtered.division == division]
if party != "All":
    filtered = filtered[filtered.winner_party == party]
st.caption(f"{len(filtered):,} constituencies match the current filters")
columns = ["constituency_no", "constituency_name", "division", "winner_candidate", "winner_party", "winner_votes", "runner_party", "runner_votes", "margin", "winner_share_top2", "competitiveness"]
st.dataframe(filtered[columns].style.format({"winner_votes": "{:,.0f}", "runner_votes": "{:,.0f}", "margin": "{:,.0f}", "winner_share_top2": "{:.1f}%"}), use_container_width=True, hide_index=True)