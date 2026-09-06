import plotly.express as px
import streamlit as st

from utils.charts import style
from utils.data import load_election_data
from utils.styles import hero, section_label

df = load_election_data()
hero("Party analysis", "Compare constituency wins, the geography of support, and the margins behind each party’s results.")
section_label("Party performance")
party = df.groupby("winner_party", as_index=False).agg(wins=("constituency_name", "count"), avg_margin=("margin", "mean"), avg_share=("winner_share_top2", "mean")).sort_values("wins", ascending=False)
left, right = st.columns(2)
with left:
    fig = px.bar(party, x="wins", y="winner_party", orientation="h", title="Constituency wins", color="wins", color_continuous_scale="Reds")
    st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
with right:
    fig = px.bar(party.sort_values("avg_margin"), x="avg_margin", y="winner_party", orientation="h", title="Average winning margin", color="avg_margin", color_continuous_scale="Reds")
    st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
division_party = df.pivot_table(index="division", columns="winner_party", values="constituency_name", aggfunc="count", fill_value=0)
fig = px.imshow(division_party, text_auto=True, aspect="auto", title="Party wins by division", color_continuous_scale="Reds")
st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
st.dataframe(party.style.format({"avg_margin": "{:,.0f}", "avg_share": "{:.1f}%"}), use_container_width=True, hide_index=True)