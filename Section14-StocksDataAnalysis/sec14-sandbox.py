import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from copy import copy
from scipy import stats
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import os 

os.getcwd()
os.chdir(os.path.relpath(r'Section14-StocksDataAnalysis'))
os.getcwd()

stocks_df = pd.read_csv('stock.csv')
stocks_df

# ---------------------------------------------- # 
df = stocks_df.copy()
# Sandbox 

# Let's define a function to calculate stocks daily returns (for all stocks) 

def daily_return(df):
    df_daily_returns = df.copy()
    # loop through cols
    for i in df.columns[1:]:
        # nest loop through rows to calc daily % difference  
        for j in range(1,len(df)): # second indexer j so we can reference two rows simultaneously 
            # calculation is:
            # df[stock_index][row_index]
            #  - df[stock_index][prev_row_index] 
            # / df[stock_index][prev_row_index] 
            # * 100
            df_daily_returns[i][j] = ( ( df[i][j] - df[i][j-1] ) / df[i][j-1] ) * 100
        # because we skipped index 0 in loop need to specify index 0 as 0
        df_daily_returns[i][0] = 0
    return df_daily_returns

stocks_daily_return = daily_return(stocks_df)

stocks_daily_return.iloc[:,1:].max().idxmax()



