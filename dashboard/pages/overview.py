import plotly.express as px
import streamlit as st

from utils.charts import style
from utils.data import division_summary, fmt_number, load_election_data
from utils.styles import hero, insight, section_label

df = load_election_data()
hero("The shape of the vote", "A clear, evidence-led view of constituency results, demographics and the socioeconomic landscape.")
metrics = [("Constituencies", fmt_number(df.constituency_name.nunique())), ("Registered voters", fmt_number(df.total_voters.sum())), ("Avg. poverty rate", f"{df.poverty_rate.mean():.1f}%"), ("Avg. literacy rate", f"{df.literacy_rate.mean():.1f}%"), ("Avg. winning margin", fmt_number(df.margin.mean())), ("Winning parties", fmt_number(df.winner_party.nunique()))]
cols = st.columns(6)
for col, (label, value) in zip(cols, metrics):
    col.metric(label, value)
section_label("National overview")
left, right = st.columns([1.15, 1])
with left:
    divisions = df.division.value_counts().rename_axis("division").reset_index(name="constituencies")
    fig = px.bar(divisions, x="division", y="constituencies", title="Constituencies by division", color_discrete_sequence=["#e84855"])
    st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
with right:
    parties = df.winner_party.value_counts().rename_axis("party").reset_index(name="wins")
    fig = px.pie(parties, names="party", values="wins", title="Party-wise constituency wins", hole=.55, color_discrete_sequence=["#f47778", "#e84855", "#c63245", "#7d202e", "#35131b"])
    st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
left, right = st.columns(2)
with left:
    fig = px.histogram(df, x="margin", nbins=24, title="Winning-margin distribution", color_discrete_sequence=["#e84855"])
    st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
with right:
    summary = division_summary(df)
    fig = px.scatter(summary, x="poverty_rate", y="literacy_rate", size="registered_voters", text="division", title="Division socioeconomic profile", color="average_margin", color_continuous_scale="Reds")
    fig.update_traces(textposition="top center")
    st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
insight("These figures describe reported top-two contest results and registered voters. They do not estimate turnout, because the dataset does not include total ballots cast.")