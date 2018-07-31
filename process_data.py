# coding: utf-8

import pandas
import numpy as np
import datetime
import wbdata

def get_indicator(x, y):
    indicators = {x: y}
    df = wbdata.get_dataframe(indicators, country="all", convert_date=True)
    df = df.reset_index(drop=False)
    df.rename(index=str, columns={"country": "Country", "date": "Year"}, inplace=True)
    df['Year'] = df['Year'].apply(lambda x : int(x.year))
    df = df.pivot(index='Country', columns='Year', values=y)
    df = df.loc[:,'1990':'2016'].dropna(axis='rows')
    return df


def get_regions():
    ct = wbdata.get_country(display=False)
    regions = pandas.DataFrame([(i['id'],i['name'], i['region'].get('value')) for i in ct],
                             columns = ['ID','Countries','Group'])

    regions.index = regions.Countries
    regions.drop('Countries', axis=1, inplace=True)
    return regions


def process_data():
    x_dim      = get_indicator(x="NY.GDP.PCAP.PP.KD", y="gdp_pc")
    y_dim      = get_indicator(x="UNEMPSA_", y="unemployment")
    bubble_dim = get_indicator(x="TX.VAL.TECH.MF.ZS", y="tech_exp")
    years = list(x_dim.columns)

    regions = get_regions()
    regions_list = list(regions.Group.unique())

    return x_dim, y_dim, bubble_dim, regions, years, regions_list, ["gdp_pc", "unemployment_rate", "tech_export"] 