# coding: utf-8
import pandas
import wbdata

indicator_by_code = {'x_dim': {
                        'name':'gdp_pc',
                        'code':'NY.GDP.PCAP.PP.KD'
                        },
                     'y_dim': {
                        'name':'unemployment_rate',
                        'code':'UNEMPSA_'
                        },
                     'bubble_dim': {
                        'name':'tech_export',
                        'code':'TX.VAL.TECH.MF.ZS'
                        }
                     }

def get_indicator(x, y):
    indicators = {x: y}
    df = wbdata.get_dataframe(indicators, country="all", convert_date=True)
    df = df.reset_index(drop=False)
    df.rename(index=str, columns={"country": "Country", "date": "Year"}, inplace=True)
    df['Year'] = df['Year'].apply(lambda x : int(x.year))
    df = df.pivot(index='Country', columns='Year', values=y)
    df = df.loc[:, '1990':'2016'].dropna(axis='rows')
    return df


def get_regions():
    ct = wbdata.get_country(display=False)
    regions = pandas.DataFrame([(i['id'], i['name'], i['region'].get('value'))
                              for i in ct],
                              columns=['ID', 'Country', 'Group'])

    regions.index = regions.Country
    regions.drop('Country', axis=1, inplace=True)
    return regions


def get_data():
    x_dim = get_indicator(x=indicator_by_code['x_dim'].get('code'), 
                          y=indicator_by_code['x_dim'].get('name'))
    y_dim = get_indicator(x=indicator_by_code['y_dim'].get('code'), 
                          y=indicator_by_code['x_dim'].get('name'))
    bubble_dim = get_indicator(x=indicator_by_code['bubble_dim'].get('code'), 
                               y=indicator_by_code['x_dim'].get('name'))
    years = list(x_dim.columns)
    
    a=list(x_dim.index)
    b=list(y_dim.index)
    c=list(bubble_dim.index)
    main_countries=list(set(a) & set(b) & set(c))

    x_dim = x_dim[x_dim.index.isin(main_countries)]
    y_dim = y_dim[y_dim.index.isin(main_countries)]
    bubble_dim = bubble_dim[bubble_dim.index.isin(main_countries)]

    regions_df = get_regions()
    regions_list=list(regions_df[regions_df.index.isin(list(x_dim.index))].Group.unique())

    return x_dim, y_dim, bubble_dim, regions_df, years, regions_list, [indicator_by_code['x_dim'].get('name'), 
                                                                       indicator_by_code['y_dim'].get('name'), 
                                                                       indicator_by_code['bubble_dim'].get('name')] 
