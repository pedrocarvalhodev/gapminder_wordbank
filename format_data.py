
# coding: utf-8

# In[1]:


import numpy as np
import datetime


# In[2]:


from bokeh.sampledata.gapminder import fertility, life_expectancy, population, regions


# In[3]:


import wbdata


# In[4]:


def process_data():
    from bokeh.sampledata.gapminder import fertility, life_expectancy, population, regions

    # Make the column names ints not strings for handling
    columns = list(fertility.columns)
    years = list(range(int(columns[0]), int(columns[-1])))
    rename_dict = dict(zip(columns, years))

    fertility = fertility.rename(columns=rename_dict)
    life_expectancy = life_expectancy.rename(columns=rename_dict)
    population = population.rename(columns=rename_dict)
    regions = regions.rename(columns=rename_dict)

    regions_list = list(regions.Group.unique())

    # Turn population into bubble sizes. Use min_size and factor to tweak.
    scale_factor = 200
    population_size = np.sqrt(population / np.pi) / scale_factor
    min_size = 3
    population_size = population_size.where(population_size >= min_size).fillna(min_size)

    return fertility, life_expectancy, population_size, regions, years, regions_list


# In[5]:


# Make the column names ints not strings for handling
columns = list(fertility.columns)
years = list(range(int(columns[0]), int(columns[-1])))
rename_dict = dict(zip(columns, years))

fertility = fertility.rename(columns=rename_dict)
life_expectancy = life_expectancy.rename(columns=rename_dict)
population = population.rename(columns=rename_dict)
regions = regions.rename(columns=rename_dict)

regions_list = list(regions.Group.unique())

# Turn population into bubble sizes. Use min_size and factor to tweak.
scale_factor = 200
population_size = np.sqrt(population / np.pi) / scale_factor
min_size = 3
population_size = population_size.where(population_size >= min_size).fillna(min_size)


# ### 1. 

# In[6]:


fertility.head(2)


# In[7]:


life_expectancy.head(2)


# In[8]:


population.head(2)


# In[9]:


regions.head(2)


# In[10]:


#set up the countries I want
countries = ["CL","UY","HU"]
 
#set up the indicator I want (just build up the dict if you want more than one)
indicators = {'NY.GNP.PCAP.CD':'GNI per Capita'}
 
#grab indicators above for countires above and load into data frame
df = wbdata.get_dataframe(indicators, country=countries, convert_date=False)

#df is "pivoted", pandas' unstack fucntion helps reshape it into something plottable
dfu = df.unstack(level=0)


# In[11]:


df.head(2)


# In[12]:


dfu.head(2)


# In[13]:


wbdata.get_source()


# In[14]:


# 1 DOing Business
wbdata.get_indicator(source=1)


# In[15]:


wbdata.search_countries("Brazil")


# In[16]:


#wbdata.get_data(indicator, country=u'all', data_date=None, convert_date=False, pandas=False, 
#column_name=u'value', keep_levels=False)
wbdata.get_data("IC.BUS.EASE.XQ", country=u'BRA')[:3]


# In[17]:


data_date = (datetime.datetime(2010, 1, 1), datetime.datetime(2011, 1, 1))
wbdata.get_data("IC.BUS.EASE.XQ", country=("USA", "BRA"), data_date=data_date)


# In[76]:


wbdata.search_indicators("gdp")


# In[19]:


wbdata.get_incomelevel()


# In[20]:


indicators = {"IC.BUS.EASE.XQ": "doing_business", "NY.GDP.PCAP.PP.KD": "gdppc"}
df = wbdata.get_dataframe(indicators, country=countries, convert_date=True)
df.describe()


# In[21]:


df.head(2)


# In[22]:


#dfa = df.dropna()
#dfa.gdppc.corr(dfa.doing_business)


# In[23]:


df.tail()


# In[24]:


fertility.head(2)


# In[130]:


fertility.columns


# In[131]:


fertility.index


# In[29]:


wbdata.get_incomelevel()


# In[ ]:


#"6.0.GDP_usd": "GDP (constant 2005 $)"


# In[ ]:


#indicators = {"IC.BUS.EASE.XQ": "doing_business", "NY.GDP.PCAP.PP.KD": "gdppc"}
#df = wbdata.get_dataframe(indicators, country=countries, convert_date=True)
#df.describe()


# In[27]:


wbdata.search_indicators("doing")


# In[30]:


countries = [i['id'] for i in wbdata.get_country(incomelevel="HIC", display=False)]


# In[32]:


countries[:3]


# In[110]:


county_list = wbdata.get_country


# In[129]:


#type(wbdata.get_country())
#type(county_list())
#wbdata.get_country(country_id=None, incomelevel=None, lendingtype=None, display=False)
#[{'id': 'ABW',
#  'iso2Code': 'AW',
#  'name': 'Aruba',
#  'region': {'id': 'LCN', 'value': 'Latin America & Caribbean '},
#  'adminregion': {'id': '', 'value': ''},
#  'incomeLevel': {'id': 'HIC', 'value': 'High income'},
#  'lendingType': {'id': 'LNX', 'value': 'Not classified'},
#  'capitalCity': 'Oranjestad',
#  'longitude': '-70.0167',
# 'latitude': '12.5167'},


# In[120]:


countries[:3]
#['ABW',
# 'AND',
# 'ARE',
# 'ARG',
# 'ATG',


# In[121]:


countries = [i['id'] for i in wbdata.get_country(display=False)]
indicators = {"IC.BUS.EASE.XQ": "doing_business", "NY.GDP.PCAP.PP.KD": "gdp_pc", "6.0.GDP_usd":"gdp"}


# In[145]:


df = wbdata.get_dataframe(indicators, country="all", convert_date=True)
df = df.reset_index(drop=False)
df.rename(index=str, columns={"country": "Country", "date": "Year"}, inplace=True)
df['Year'] = df['Year'].apply(lambda x : str(x.year))
df_gdp = df.pivot(index='Country', columns='Year', values='gdp')
df_db = df.pivot(index='Country', columns='Year', values='doing_business')

## GDP Per capita
df_pc = df.pivot(index='Country', columns='Year', values='gdp_pc')
df_pc = df_pc.loc[:,'1990':'2017'].dropna(axis='rows')


# In[148]:


df_pc.sort_values(by="2016", ascending=False).iloc[:20, -5:]


# In[ ]:


wbdata.get_indicator(source=1)


# In[203]:


def get_indicator(x, y):
    indicators = {x: y}
    df = wbdata.get_dataframe(indicators, country="all", convert_date=True)
    df = df.reset_index(drop=False)
    df.rename(index=str, columns={"country": "Country", "date": "Year"}, inplace=True)
    df['Year'] = df['Year'].apply(lambda x : str(x.year))
    df = df.pivot(index='Country', columns='Year', values=y)
    df = df.loc[:,'1990':'2016'].dropna(axis='rows')
    print(df.shape)
    return df


# In[205]:


get_indicator(x="UNEMPSA_", y="unemployment")


# In[208]:


#Market capitalization of listed domestic companies (% of GDP)
get_indicator(x="CM.MKT.LCAP.GD.ZS", y="mktcap_gdp")


# In[211]:


#TX.VAL.TECH.CD       	High-technology exports (current US$)
get_indicator(x="TX.VAL.TECH.CD", y="tech_exp")


# In[212]:


#TX.VAL.TECH.MF.ZS    	High-technology exports (% of manufactured exports)
#TX.VAL.TECH.MANF.ZS  	High-technology exports (% of manufactured exports)
get_indicator(x="TX.VAL.TECH.MF.ZS", y="tech_exp")


# In[213]:


#wbdata.search_indicators(query="gdp")

