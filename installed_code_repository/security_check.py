#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def login_check(account:str, pwd:str):
    from datetime import date
    
    fin = open("/Users/apple/Documents/Jupyter/ETF_quantitative_strategy/data/security.in")
    name_list = fin.readlines()
    fin.close()
    
    fout = open("/Users/apple/Documents/Jupyter/ETF_quantitative_strategy/output/security_gateway.out", "w")
    
    for line in range(len(name_list)):
        name_list[line] = name_list[line].rstrip()
    diction = {}
    for i in name_list:
        a,b = i.split()
        diction[a] = b
    try:
        if diction[account] == pwd:
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            fout.write("TRUE"+" "+ d1)
            fout.close()
            print("Access Accepted")
        else:
            fout.write("FALSE")
            fout.close()
            print("Invalid Password,", "Access Denied")
    except:
        fout.write("FALSE")
        fout.close()
        print("Invalid Password,", "Access Denied")
        
def regular_check():
    fin = open("/Users/apple/Documents/Jupyter/ETF_quantitative_strategy/output/security_gateway.out")
    from datetime import date
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    lista = fin.readline().split()
    if lista[0] == "TRUE":
        if lista[1] == d1:
            return True
    return False


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




