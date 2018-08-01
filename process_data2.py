
# coding: utf-8

# In[1]:


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
from process_data import process_data


# In[2]:


#fertility_df, life_expectancy_df, population_df_size, regions_df, years, regions_list = process_data()
x_dim, y_dim, bubble_dim, regions_df, years, regions_list, dims = process_data()


# In[3]:


print(dims[0])
print("-"*60)
print(x_dim.head(), x_dim.shape)
print("/"*50)
print(dims[1])
print("-"*60)
print(y_dim.head(), y_dim.shape)
print("/"*50)
print(dims[2])
print("-"*60)
print(bubble_dim.head(), bubble_dim.shape)
print("/"*50)


# In[4]:


p = pd.Panel({dims[0]: x_dim, dims[1]: x_dim, dims[2]: bubble_dim})


# In[8]:


x_dim.index


# In[13]:


regions_df[regions_df.index.isin(list(x_dim.index))].Group.name


# In[14]:


data = {}


# In[15]:


region_name = regions_df[regions_df.index.isin(list(x_dim.index))].Group
region_name.name = 'region'


# In[16]:


for year in years:
    df = pd.concat([p.loc[:, :, year], region_name], axis=1).reset_index()
    data[year] = df.to_dict('series')


# In[17]:


print('saved')
source = ColumnDataSource(data=data[years[0]])
# Palette length does not match number of factors. ['East Asia & Pacific', 'North America'] will be assigned to `nan_color` gray
# warnings.warn("Palette length does not match number of factors. %s will be assigned to `nan_color` %s" % (extra_factors, self.nan_color))


plot = figure(x_range=(245, 136000), y_range=(0.5, 26.5), title='Gapminder Data', plot_height=300)
plot.xaxis.ticker = SingleIntervalTicker(interval=15000)
plot.xaxis.axis_label = "GDP Per Capita ($USD)"
plot.yaxis.ticker = SingleIntervalTicker(interval=1)
plot.yaxis.axis_label = "Unemployment Rate"

label = Label(x=1.1, y=18, text=str(years[0]), text_font_size='70pt', text_color='#eeeeee')
plot.add_layout(label)

color_mapper = CategoricalColorMapper(palette=Spectral6, factors=regions_list)
plot.circle(
    x='gdp_per_capita',
    y='unemployment',
    size='tech_export_rate',
    source=source,
    fill_color={'field': 'region', 'transform': color_mapper},
    fill_alpha=0.8,
    line_color='#7c7e71',
    line_width=0.5,
    line_alpha=0.5,
    legend=field('region'),
)
plot.add_tools(HoverTool(tooltips="@index", show_arrow=False, point_policy='follow_mouse'))


def animate_update():
    year = slider.value + 1
    if year > years[-1]:
        year = years[0]
    slider.value = year


def slider_update(attrname, old, new):
    year = slider.value
    label.text = str(year)
    source.data = data[year]

slider = Slider(start=years[0], end=years[-1], value=years[0], step=1, title="Year")
slider.on_change('value', slider_update)

callback_id = None

def animate():
    global callback_id
    if button.label == '► Play':
        button.label = '❚❚ Pause'
        callback_id = curdoc().add_periodic_callback(animate_update, 200)
    else:
        button.label = '► Play'
        curdoc().remove_periodic_callback(callback_id)

button = Button(label='► Play', width=60)
button.on_click(animate)

layout = layout([
    [plot],
    [slider, button],
], sizing_mode='scale_width')

curdoc().add_root(layout)
curdoc().title = "Gapminder"

