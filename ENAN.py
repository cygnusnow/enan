#!/bin/python
import time
from datetime import date
import math
import tushare as ts
import pandas as pd
import numpy as np


df = ts.get_hist_data('000875')
df.to_excel('F:/stock/ENAN/data/test.xlsx')


