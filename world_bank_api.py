import wbdata
import pandas
import datetime

#set up the countries I want
countries = ["CL","UY","HU"]

#set up the indicator I want (just build up the dict if you want more than one)
indicators = {'NY.GNP.PCAP.CD':'GNI per Capita'}

#grab indicators above for countires above and load into data frame
df = wbdata.get_dataframe(indicators, country=countries, convert_date=False)

#df is "pivoted", pandas' unstack fucntion helps reshape it into something plottable
#df = df.unstack(level=0)
print(df.head())
