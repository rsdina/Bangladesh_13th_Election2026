import plotly.express as px
import streamlit as st

from utils.charts import style
from utils.data import division_summary, load_election_data
from utils.styles import hero, section_label

df = load_election_data()
summary = division_summary(df)
hero("Socioeconomic analysis", "Explore how poverty, literacy and electoral margins move across the country’s divisions.")
section_label("Division indicators")
left, right = st.columns(2)
with left:
    fig = px.bar(summary.sort_values("poverty_rate"), x="poverty_rate", y="division", orientation="h", title="Average poverty rate", color="poverty_rate", color_continuous_scale="Reds")
    st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
with right:
    fig = px.bar(summary.sort_values("literacy_rate"), x="literacy_rate", y="division", orientation="h", title="Average literacy rate", color="literacy_rate", color_continuous_scale="Reds")
    st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
fig = px.scatter(df, x="poverty_rate", y="literacy_rate", size="total_voters", color="margin", hover_name="constituency_name", title="Poverty and literacy by constituency", color_continuous_scale="Reds")
st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
st.dataframe(summary.style.format({"poverty_rate": "{:.1f}%", "literacy_rate": "{:.1f}%", "average_margin": "{:,.0f}", "registered_voters": "{:,.0f}"}), use_container_width=True, hide_index=True)