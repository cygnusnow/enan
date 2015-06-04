import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
import tushare as ts
import sys

DATAFILENAME = 'F:/stock/ENAN/data/test.xlsx'
fobj=open(DATAFILENAME,'wb+')
fobj.close()

#hisData = ts.get_hist_data('160217')
#print hisData

df = ts.get_index()

df.to_excel(DATAFILENAME, sheet_name='history')





