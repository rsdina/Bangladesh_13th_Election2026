from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "processed"
TABLE_DIR = ROOT / "tables"


@st.cache_data
def load_election_data() -> pd.DataFrame:
    frame = pd.read_csv(DATA_DIR / "election_clean.csv")
    numeric_columns = ["constituency_no", "poverty_rate", "literacy_rate", "winner_votes", "runner_votes", "margin", "total_voters", "male_voters", "female_voters", "transgender_voters", "top2_votes", "winner_share_top2", "margin_pct_top2", "male_pct", "female_pct", "transgender_pct", "gender_gap"]
    for column in numeric_columns:
        if column in frame:
            frame[column] = pd.to_numeric(frame[column], errors="coerce")
    return frame


@st.cache_data
def load_referendum_data() -> pd.DataFrame:
    frame = pd.read_csv(DATA_DIR / "gonovote_clean.csv")
    for column in ("votes", "percentage"):
        if column in frame:
            frame[column] = pd.to_numeric(frame[column], errors="coerce")
    return frame


def fmt_number(value: float, decimals: int = 0) -> str:
    if pd.isna(value):
        return "—"
    return f"{value:,.{decimals}f}"


def division_summary(frame: pd.DataFrame) -> pd.DataFrame:
    return frame.groupby("division", as_index=False).agg(
        constituencies=("constituency_name", "count"),
        registered_voters=("total_voters", "sum"),
        poverty_rate=("poverty_rate", "mean"),
        literacy_rate=("literacy_rate", "mean"),
        average_margin=("margin", "mean"),
    ).sort_values("constituencies", ascending=False)