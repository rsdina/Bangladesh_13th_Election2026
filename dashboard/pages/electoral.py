import plotly.express as px
import streamlit as st

from utils.charts import style
from utils.data import load_election_data
from utils.styles import hero, section_label

df = load_election_data()
hero("Electoral analysis", "How close were the contests, and how much of the reported top-two vote did winners command?")
section_label("Contest profile")
a, b, c = st.columns(3)
a.metric("Very close contests", f"{(df.competitiveness == 'Very Close').sum():,}")
b.metric("Median margin", f"{df.margin.median():,.0f}")
c.metric("Median top-two share", f"{df.winner_share_top2.median():.1f}%")
left, right = st.columns(2)
with left:
    counts = df.competitiveness.value_counts().rename_axis("category").reset_index(name="constituencies")
    fig = px.bar(counts, x="category", y="constituencies", title="Competitiveness categories", color="category", color_discrete_sequence=["#f47778", "#c63245", "#7d202e", "#35131b"])
    st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
with right:
    fig = px.scatter(df, x="winner_share_top2", y="margin", color="competitiveness", hover_name="constituency_name", title="Winner share and winning margin", color_discrete_sequence=["#f47778", "#c63245", "#7d202e", "#e8dddb"])
    st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
fig = px.box(df, x="division", y="margin", color="division", title="Winning margin by division", color_discrete_sequence=["#e84855", "#f47778", "#a82b3d", "#7d202e", "#c63245", "#d95a62", "#91313d"])
st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})