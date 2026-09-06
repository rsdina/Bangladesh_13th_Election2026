import plotly.express as px
import streamlit as st

from utils.charts import style
from utils.data import fmt_number, load_referendum_data
from utils.styles import hero, section_label

df = load_referendum_data()
hero("Referendum analysis", "A compact view of the referendum result included in the research dataset.")
section_label("Reported referendum result")
yes = df.loc[df.choice.eq("Yes"), "votes"].iloc[0] if (df.choice == "Yes").any() else 0
no = df.loc[df.choice.eq("No"), "votes"].iloc[0] if (df.choice == "No").any() else 0
a, b, c = st.columns(3)
a.metric("Yes votes", fmt_number(yes))
b.metric("No votes", fmt_number(no))
c.metric("Reported votes", fmt_number(df.votes.sum()))
left, right = st.columns(2)
with left:
    fig = px.bar(df, x="choice", y="votes", text="percentage", title="Votes by choice", color="choice", color_discrete_sequence=["#e84855", "#7d202e"])
    st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
with right:
    fig = px.pie(df, names="choice", values="votes", hole=.55, title="Share of reported referendum votes", color_discrete_sequence=["#e84855", "#7d202e"])
    st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
st.dataframe(df, use_container_width=True, hide_index=True)