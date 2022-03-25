import pandas as pd
import json

def get_df_lp(option, timeseries_dict: dict) -> pd.DataFrame:

    df_lp=pd.DataFrame(data=zip(timeseries_dict[option]['date'],
                        timeseries_dict[option]['base'],
                        timeseries_dict[option]['reward'],
                        timeseries_dict[option]['tvl'],
                        timeseries_dict[option]['apy']),columns=['date','base','reward','tvl','apy'])

    df_lp['date']=pd.to_datetime(df_lp['date'])
    df_lp['base']=pd.to_numeric(df_lp['base'])
    df_lp['reward']=pd.to_numeric(df_lp['reward'])
    df_lp['tvl']=pd.to_numeric(df_lp['tvl'])
    df_lp['apy']=pd.to_numeric(df_lp['apy'])

    return df_lp