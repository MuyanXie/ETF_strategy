#!/usr/bin/env python
# coding: utf-8

# In[18]:


def systematic_error_check():
    flag = True
    
    # check if the name_list.in is the same size as the number of files contained in the data folder
    import glob
    config_file_number = len(glob.glob("/Users/apple/Documents/Jupyter/ETF_quantitative_strategy/data/*.in"))
    total_file_number = len(glob.glob("/Users/apple/Documents/Jupyter/ETF_quantitative_strategy/data/**"))
    fin = open("/Users/apple/Documents/Jupyter/ETF_quantitative_strategy/data/name_list.in")
    name_list = fin.readlines()
    fin.close()
    if len(name_list) != total_file_number - config_file_number:
        flag = False
        print("ERRInconsistent data file actually collected and documented in the name_list.in file, we record",len(name_list), "files but", total_file_number-config_file_number, "is actually collected")

    
    return flag
    print(config_file_number)


# In[19]:





# In[ ]:




