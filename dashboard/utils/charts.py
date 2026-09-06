import plotly.graph_objects as go

PLOT_LAYOUT = dict(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(family="DM Sans", color="#e8dddb"), margin=dict(l=10, r=10, t=45, b=10), legend=dict(bgcolor="rgba(0,0,0,0)"))


def style(fig: go.Figure) -> go.Figure:
    fig.update_layout(**PLOT_LAYOUT)
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(gridcolor="rgba(255,255,255,.08)")
    return fig