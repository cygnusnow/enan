#!/bin/python
import time
from datetime import date
import math
import tushare as ts
import pandas as pd
import numpy as np

def enanSaveData2Excel(df):
    t = date.today()
    print t
    fileName = r"F:\\stock\\ENAN\\data\\" + str(t) + r".xlsx"
    df.to_excel(fileName)


df = ts.get_tick_data('600848',date='2015-05-23')
df.head(10)
enanSaveData2Excel(df)


