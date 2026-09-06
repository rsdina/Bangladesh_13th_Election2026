import plotly.express as px
import streamlit as st

from utils.charts import style
from utils.data import load_election_data
from utils.styles import hero, section_label

df = load_election_data()
hero("Demographic analysis", "A view of the registered voter profile across gender groups and divisions.")
section_label("Registered voter composition")
a, b, c = st.columns(3)
a.metric("Male voters", f"{df.male_voters.sum():,.0f}")
b.metric("Female voters", f"{df.female_voters.sum():,.0f}")
c.metric("Transgender voters", f"{df.transgender_voters.sum():,.0f}")
division_gender = df.groupby("division", as_index=False)[["male_pct", "female_pct", "transgender_pct"]].mean().melt("division", var_name="group", value_name="share")
fig = px.bar(division_gender, x="division", y="share", color="group", barmode="group", title="Average registered voter share by division", color_discrete_sequence=["#e84855", "#f47778", "#e8dddb"])
st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
left, right = st.columns(2)
with left:
    fig = px.box(df, x="division", y="gender_gap", title="Gender gap by division", color="division", color_discrete_sequence=["#e84855", "#f47778", "#a82b3d", "#7d202e", "#c63245", "#d95a62", "#91313d"])
    st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
with right:
    fig = px.scatter(df, x="female_pct", y="gender_gap", size="total_voters", color="division", hover_name="constituency_name", title="Female share and gender gap")
    st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})