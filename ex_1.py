import FinanceDataReader as fdr 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 



df = fdr.DataReader('138040', '2012-01-01') #메리츠금융지주#

df['Open'].plot()
