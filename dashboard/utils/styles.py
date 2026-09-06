import streamlit as st


def inject_styles() -> None:
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
    :root { --ink:#f7f3f1; --muted:#a99f9c; --red:#e84855; --panel:rgba(35,24,27,.72); }
    html, body, [class*="css"] { font-family:'DM Sans',sans-serif; }
    .stApp { background:radial-gradient(circle at 80% 0%,#4d1d27 0,transparent 32%),linear-gradient(135deg,#110e12 0%,#1b1217 52%,#290e16 100%); color:var(--ink); }
    .stApp:before { content:''; position:fixed; inset:0; pointer-events:none; opacity:.14; background-image:linear-gradient(rgba(255,255,255,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.06) 1px,transparent 1px); background-size:46px 46px; mask-image:linear-gradient(to bottom,black,transparent 80%); }
    h1,h2,h3 { font-family:'Space Grotesk',sans-serif !important; letter-spacing:0 !important; }
    h1 { font-size:clamp(2rem,4vw,3.7rem) !important; line-height:1.02 !important; }
    [data-testid="stSidebar"] { background:rgba(18,13,16,.9); border-right:1px solid rgba(255,255,255,.09); }
    [data-testid="stMetric"] { background:var(--panel); border:1px solid rgba(255,255,255,.11); border-radius:14px; padding:18px 20px; box-shadow:0 16px 40px rgba(0,0,0,.18); backdrop-filter:blur(15px); }
    [data-testid="stMetricLabel"] { color:var(--muted); } [data-testid="stMetricValue"] { color:#fff; font-family:'Space Grotesk',sans-serif; }
    .hero { padding:1.4rem 0 1.8rem; border-bottom:1px solid rgba(255,255,255,.1); margin-bottom:1.4rem; }
    .eyebrow,.section-label { color:#ff7a82; text-transform:uppercase; letter-spacing:.14em; font-size:.72rem; font-weight:700; }
    .subtitle { color:var(--muted); max-width:720px; font-size:1.05rem; } .section-label { margin:1.4rem 0 .5rem; }
    .insight { background:linear-gradient(105deg,rgba(232,72,85,.2),rgba(53,27,34,.5)); border-left:3px solid var(--red); border-radius:0 12px 12px 0; padding:15px 18px; color:#e7dcda; }
    </style>
    """, unsafe_allow_html=True)


def hero(title: str, description: str, eyebrow: str = "BANGLADESH • 13TH ELECTION") -> None:
    st.markdown(f'<div class="hero"><div class="eyebrow">{eyebrow}</div><h1>{title}</h1><div class="subtitle">{description}</div></div>', unsafe_allow_html=True)


def section_label(text: str) -> None:
    st.markdown(f'<div class="section-label">{text}</div>', unsafe_allow_html=True)


def insight(text: str) -> None:
    st.markdown(f'<div class="insight">{text}</div>', unsafe_allow_html=True)