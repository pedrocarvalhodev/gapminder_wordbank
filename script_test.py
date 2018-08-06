
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
import pandas as pd

from bokeh.core.properties import field
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models import (ColumnDataSource, 
                          HoverTool, 
                          SingleIntervalTicker,
                          Slider, Button, Label, 
                          CategoricalColorMapper)
from bokeh.palettes import Spectral6
from bokeh.plotting import figure

#import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument("-s", "--save_data", action="store_true", 
#    help="-s : save info to data file")
#parser.add_argument("-r", "--read_data", action="store_true",
#    help="-r : read info to data file")

#args = parser.parse_args()

path='/home/pedro/repos/github_repos/gapminder_wordbank/data/'


# In[1]:


from process_data import get_data, indicator_by_code
x_dim, y_dim, bubble_dim, regions_df, years, regions_list, dims = get_data()


# In[2]:


indicator_by_code


# In[3]:


[indicator_by_code['x_dim'].get('name'),
indicator_by_code['y_dim'].get('name'),
indicator_by_code['bubble_dim'].get('name')]


# In[ ]:


x_dim.iloc[:2,-5:]


# In[ ]:


y_dim.iloc[:2,-5:]


# In[ ]:


bubble_dim.iloc[:2,-5:]


# In[ ]:


regions_df.iloc[:2,-5:]


# In[ ]:


years[:3]


# In[ ]:


regions_list[:3]


# In[ ]:


dims[:3]


# In[ ]:


x_dim.to_csv(path+'x_dim.csv') 
y_dim.to_csv(path+'y_dim.csv')
bubble_dim.to_csv(path+'bubble_dim.csv')
regions_df.to_csv(path+'regions_df.csv')
#years.to_csv(path+'years.txt')
#regions_list.to_csv(path+'regions_list.csv')
#dims.to_csv(path+'dims.csv')


# In[ ]:


x_dim.to_csv(path+'x_dim.csv', index=True) 


# In[ ]:


x_dim2 = pd.read_csv(path+'x_dim.csv', index_col='Country')


# In[ ]:


x_dim.iloc[:2,:5]


# In[ ]:


x_dim2.iloc[:2,:5]


# In[ ]:


y_dim.to_csv(path+'y_dim.csv', index=True)
y_dim2 = pd.read_csv(path+'y_dim.csv', index_col='Country')


# In[ ]:


y_dim.iloc[:2,:5]


# In[ ]:


y_dim2.iloc[:2,:5]


# In[ ]:


regions_df.to_csv(path+'regions_df.csv', index=True)
    regions_df2 = pd.read_csv(path+'regions_df.csv', index_col='Countries')


# In[ ]:


regions_df.iloc[:2,:5]


# In[ ]:


regions_df2.iloc[:2,:5]


# In[ ]:


indicator_by_code = {'x_dim': {'gdp_pc':'NY.GDP.PCAP.PP.KD'},
                     'y_dim': {'unemployment':'UNEMPSA_'},
                     'bubble_dim': {'tech_exp':'TX.VAL.TECH.MF.ZS'}
                     }


# In[ ]:


indicator_by_code['x_dim'].get('gdp_pc')


# In[ ]:


indicator_by_code['x_dim'].keys()


# In[ ]:


list(indicator_by_code['x_dim'].keys())[0]


# In[ ]:


indicator_by_code = {'x_dim': {'name':'gdp_pc','code':'NY.GDP.PCAP.PP.KD'},
                     'y_dim': {'name':'unemployment','code':'UNEMPSA_'},
                     'bubble_dim': {'name':'tech_exp','code':'TX.VAL.TECH.MF.ZS'}
                     }


# In[ ]:


indicator_by_code['x_dim'].get('code')


# In[ ]:


indicator_by_code['x_dim'].get('name')


# In[ ]:


import process_data


# In[ ]:


from process_data import indicator_by_code as indicator_by_code2


# In[ ]:


process_data.indicator_by_code


# In[ ]:


[process_data.indicator_by_code['x_dim'].get('name'),
process_data.indicator_by_code['y_dim'].get('name'),
process_data.indicator_by_code['bubble_dim'].get('name')]

