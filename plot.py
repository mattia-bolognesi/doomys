import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def main_graph(df: pd.DataFrame):
    fig = px.scatter(df,
                    x='risk_score',
                    y='return_score',
                    color="chain",
                    hover_data=["lp_name","protocol"],
                    labels={
                        "lp_name":"Liquidity Pool",
                        "return_score": "Return Score",
                        "risk_score": "Risk Score",
                        "chain": "Blockchain",
                        "protocol":"Protocol"
                    },
                    color_discrete_sequence=px.colors.qualitative.T10
                    )

    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    fig.update_traces(marker=dict(size=13,
                                line=dict(width=0.6,
                                            color='DarkSlateGrey')),
                    selector=dict(mode='markers'))

    fig.add_shape(type="line",
        x0=0, y0=11, x1=0, y1=0,
        line=dict(color="DarkSlateGrey",width=0.5)
    )

    fig.add_shape(type="line",
        x0=0, y0=0, x1=10, y1=0,
        line=dict(color="DarkSlateGrey",width=0.5)
    )

    fig.update_layout(
                xaxis=dict(title_text="(-) «──────────── Risk ────────────» (+)", showgrid=False, showticklabels=False, rangemode='tozero', mirror=True, linewidth=2),
                yaxis=dict(title_text="(-) «──────── Return ────────» (+)", showgrid=False, showticklabels=False, rangemode='tozero', mirror=True, linewidth=2),
    )
    fig.update_layout(width=1000, height=500)

    return fig

def lp_insights(df_lp: pd.DataFrame)-> go.Figure:
    
    fig = go.Figure()
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(
            x=df_lp["date"],
            y=df_lp["tvl"],
            name="TVL",
        ),
        secondary_y=True,
    )
    fig.update_traces(
        marker_color="rgb(252,149,79)",
        marker_line_color="rgb(20,76,157)",
        marker_line_width=0.5,
        opacity=0.4,
    )
    fig.add_trace(
        go.Scatter(
            x=df_lp["date"],
            y=df_lp["base"],
            name="Base APY",
        ),
    secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=df_lp["date"],
            y=df_lp["reward"],
            name="Reward Token",
        ),
    secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=df_lp["date"],
            y=df_lp["apy"],
            name="Total APY",
        ),
    secondary_y=False,
    )
    fig.update_layout(
        legend=dict(
            orientation="h",
            y=-0.1,
            x=0.25,
        )
    )
    fig.update_yaxes(showgrid=False, tickformat='0%',title_text="Base APY & Reward Token", secondary_y=False)
    fig.update_yaxes(showgrid=False, title_text="TVL", secondary_y=True)
    fig.update_layout(width=1000, height=500, plot_bgcolor="rgb(255,255,255)")

    return fig

def reward_token_insights(reward_token_timeseries)-> go.Figure:

    fig = go.Figure()
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(
            x=reward_token_timeseries['date'],
            y=reward_token_timeseries['market_cap'],
            name="Market Cap",
        ),
        secondary_y=True,
    )
    fig.update_traces(
        marker_color="rgb(252,149,79)",
        marker_line_color="rgb(20,76,157)",
        marker_line_width=0.5,
        opacity=0.4,
    )
    fig.add_trace(
        go.Scatter(
            x=reward_token_timeseries['date'],
            y=reward_token_timeseries['price'],
            name="Price",
        ),
    secondary_y=False,
    )
    fig.update_layout(
        legend=dict(
            orientation="h",
            y=-0.1,
            x=0.25,
        )
    )
    fig.update_yaxes(showgrid=False, title_text="Price", secondary_y=False)
    fig.update_yaxes(showgrid=False, title_text="Market Cap", secondary_y=True)
    fig.update_layout(width=1000, height=500, plot_bgcolor="rgb(255,255,255)")
    return fig