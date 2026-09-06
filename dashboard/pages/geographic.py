import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components

from utils.charts import style
from utils.data import ROOT, division_summary, load_election_data
from utils.styles import hero, insight, section_label

df = load_election_data()
summary = division_summary(df)
hero("Geographic analysis", "Read the electoral landscape by division, with the repository’s published interactive map embedded where available.")
section_label("Division landscape")
fig = px.bar(summary.sort_values("registered_voters"), x="registered_voters", y="division", orientation="h", title="Registered voters by division", color="registered_voters", color_continuous_scale="Reds")
st.plotly_chart(style(fig), use_container_width=True, config={"displayModeBar": False})
map_path = ROOT / "figures" / "bangladesh_election_map.html"
if map_path.exists():
    with st.expander("Open published Bangladesh election map", expanded=True):
        components.html(map_path.read_text(encoding="utf-8"), height=620, scrolling=True)
else:
    insight("The repository does not include the published geographic HTML at the expected path. Division-level comparisons remain available above.")
st.dataframe(summary.style.format({"registered_voters": "{:,.0f}", "poverty_rate": "{:.1f}%", "literacy_rate": "{:.1f}%", "average_margin": "{:,.0f}"}), use_container_width=True, hide_index=True)