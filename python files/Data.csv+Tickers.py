#!/usr/bin/env python
# coding: utf-8

# In[158]:


import pandas as pd
import numpy as np
mergr = pd.read_csv('/Users/eje/Desktop/Data.csv',decimal =',')
mergr_na = mergr.dropna(subset=['Target', 'Investor(s)','Deal Value (USD/MLNS)'])
mergr_na = mergr_na.drop(mergr_na[mergr_na.Target == 'Target'].index)
mergr_na = mergr_na.drop(['Address','City','State/Province','Zip','Phone','Url','EV/Revenue','EV/EBITDA','Seller(s)'], axis = 1)
'''
Investors_sym = [np.nan for i in range(mergr_na.shape[0])]
Target_sym = [np.nan for i in range(mergr_na.shape[0])]
Target_Names_in_API = [np.nan for i in range(mergr_na.shape[0])]
Investors_Names_in_API = [np.nan for i in range(mergr_na.shape[0])]

mergr_na['Target_symbol'] = Target_sym
mergr_na['Investors_symbol'] = Investors_sym
mergr_na['Target_Names_in_API'] = Target_Names_in_API
mergr_na['Investors_Names_in_API'] = Investors_Names_in_API'''


# In[159]:


print(mergr_na.shape)
mergr_na.head(5)


# In[161]:


all_tickers_and_names = pd.read_csv('/Users/eje/Desktop/new_all_tickers_and_names.csv', decimal =',', engine='python')
all_tickers_and_names = all_tickers_and_names.dropna(subset=['name'])


# In[162]:


all_tickers_and_names.shape


# In[103]:


list(all_tickers_and_names.name)


# In[165]:


symbol_Target_list =[]
symbols_Targetlist =[]

c=0

for j in list(mergr_na.Target):
    for i in list(all_tickers_and_names.name):
        
        if len(j) <= len(i) and j in i:
            print('-------',i)
            print('-------',j)
            symbol_Target_list.append(i)
            something =all_tickers_and_names['name'].values == i
            df_new = all_tickers_and_names.loc[something]
            print('-------', list(df_new.symbol)[0])
            symbols_Targetlist.append(list(df_new.symbol)[0])
            #print('-------',symbol_Target_list)
            break
        
        elif len(i)<len(j) and i in j:
            print('---',i)
            print('---',j)
            symbol_Target_list.append(i)
            something =all_tickers_and_names['name'].values == i
            df_new = all_tickers_and_names.loc[something] 
            print('---', list(df_new.symbol)[0])
            symbols_Targetlist.append(list(df_new.symbol)[0])
            #print('---',symbol_Target_list)
            break
            
        
    else : 
        c =c+1
        print(c)
        symbol_Target_list.append(np.nan)
        symbols_Targetlist.append(np.nan)
        #symbol_Investors_list.append(np.nan)

        


# In[163]:


'''
mergr_na['Target_symbol'] = symbols_Targetlist

mergr_na['Target_Names_in_API'] = symbol_Target_list
list(mergr_na['Target_Names_in_API'])
'''


# In[166]:


symbol_Investors_list =[]
symbols_Investorslist =[]


Investors_sym = []
Investors_Names_in_API = []
c=0

for j in list(mergr_na['Investor(s)']):
    for i in list(all_tickers_and_names.name):
        
        if len(j) <= len(i) and j in i:
            print('-------',i)
            print('-------',j)
            symbol_Investors_list.append(i)
            something =all_tickers_and_names['name'].values == i
            df_new = all_tickers_and_names.loc[something]
            print('-------', list(df_new.symbol)[0])
            symbols_Investorslist.append(list(df_new.symbol)[0])
            #print('-------',symbol_Target_list)
            break
        
        elif len(i)<len(j) and i in j:
            print('---',i)
            print('---',j)
            symbol_Investors_list.append(i)
            something =all_tickers_and_names['name'].values == i
            df_new = all_tickers_and_names.loc[something] 
            print('---', list(df_new.symbol)[0])
            symbols_Investorslist.append(list(df_new.symbol)[0])
            #print('---',symbol_Target_list)
            break
            
        
    else : 
        c =c+1
        print(c)
        symbol_Investors_list.append(np.nan)
        symbols_Investorslist.append(np.nan)
        #symbol_Investors_list.append(np.nan)


# In[169]:


mergr_na['Target_symbol'] = symbols_Targetlist
mergr_na['Investors_symbol'] = symbols_Investorslist
mergr_na['Target_Name_in_API'] = symbol_Target_list
mergr_na['Investors_Name_in_API'] = symbol_Investors_list
mergr_na = mergr_na.drop(['Target_Names_in_API','Investors_Names_in_API'], axis = 1)


# In[171]:


print(mergr_na.shape)
mergr_na.head(-50)


# In[172]:


mergr_na.index = [i for i in range(22327)]


# In[173]:


print(mergr_na.shape)
mergr_na.head(50)


# In[175]:


lis =[]
for i in range(22327):
    if mergr_na.Target_symbol[i] is np.nan and mergr_na.Investors_symbol[i] is np.nan and mergr_na.Target_Name_in_API[i] is np.nan and mergr_na.Investors_Name_in_API[i] is np.nan:
        lis.append(mergr_na.index[i])


# In[180]:


mergr_na = mergr_na.drop(lis, axis =0)
mergr_na['Date']= pd.to_datetime(mergr_na['Date'])


# In[181]:


mergr_na.to_csv('PreProcess_mergrdata_and_symbols.csv', index = False)


# In[182]:


mergr_na.shape

