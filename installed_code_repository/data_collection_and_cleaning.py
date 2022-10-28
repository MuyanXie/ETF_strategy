#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sys
sys.path.append('/Users/apple/Documents/Jupyter/ETF_quantitative_strategy/installed_code_repository')
import installed_code_repository
from security_check import regular_check
def get_data(name: str):
    if not regular_check():
        print("NO ROOT")
        return
    try:
        df = pd.read_csv("/Users/apple/Documents/Jupyter/ETF_quantitative_strategy/data/"+name+".csv")

        from datetime import date
        today = date.today()
        d1 = today.strftime("%Y-%m-%d")
        if df.at[0, "timestamp"] == d1:
            print("data already exist")
            return
    except:
        a = 1
        del a
    string1 = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="
    string2 = "&apikey=J4743RUZXDBDJ2HS&datatype=csv"
    df = pd.read_csv(string1+name+string2)
    df.to_csv("/Users/apple/Documents/Jupyter/ETF_quantitative_strategy/data/"+name+".csv")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




