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