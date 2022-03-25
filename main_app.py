import streamlit as st
import pandas as pd
import json
import pickle
from utils import get_df_lp
from plot import main_graph, lp_insights, reward_token_insights

st.set_page_config(layout="wide",
                    page_title="Doomy's: The De-Fi rating provider",
                    page_icon="🧊",
                    menu_items={'Get help': 'm.bolognesi95@gmail.com'})

st.title("Doomy's: The De-Fi rating provider")

st.header(
    "A _Risk Return Optimization Approach_ to find the best LPs according to your risk profile."
)

st.subheader(
    "An in-depth analysis on single stake USDC liquidity pools 📊📈"
    )

df = pd.read_excel('data/lp_risk_return.xlsx')

st.plotly_chart(
    main_graph(df)
    )

f = open('data/timeseries_dict.json')
timeseries_dict = json.load(f)

option = st.selectbox(
     'Choose the liquidity pool',
     (timeseries_dict.keys())
     )

df_lp = get_df_lp(
    option,timeseries_dict
    )

st.subheader(
    "Liquidity Pool dynamics"
)

st.plotly_chart(
    lp_insights(df_lp)
    )

with open(r'data/reward_token_timeseries.p', 'rb') as f:
    reward_token_timeseries = pickle.load(f)

try:
    st.subheader(
    "Reward Token Market Dynamics: "
    + reward_token_timeseries[df[df['lp_name']==option]
    ['reward_token'].iloc[0]]['ticker'].iloc[0]
    )
    st.plotly_chart(
        reward_token_insights(
            reward_token_timeseries[df[df['lp_name']==option]['reward_token'].iloc[0]]
            )
        )

except:
    st.write(
        'There are no reward token for this pool'
        )

st.markdown("Do you wanna know more about the model and/or the data? [Email](m.bolognesi95@gmail.com) - [LinkedIn](https://www.linkedin.com/in/mattia-bolognesi/)")
