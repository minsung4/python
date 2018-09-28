import FinanceDataReader as fdr 
import numpy as np 
import matplotlib 
import pandas as pd 



df = fdr.DataReader('138040', '2012-01-01') #메리츠금융지주#

print(df)
