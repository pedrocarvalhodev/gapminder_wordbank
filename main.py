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

path='/home/pedro/repos/github_repos/gapminder_wordbank/data/'


x_dim, y_dim, bubble_dim, regions_df, years, regions_list, dims = process_data()


print("Loaded Data.")
list(regions_df[regions_df.index.isin(list(x_dim.index))].Group.unique())
p = pd.Panel({dims[0]: (x_dim / 1000).astype(int), 
              dims[1]: y_dim.astype(int), 
              dims[2]: bubble_dim.astype(int)})

data = {}
for year in years:
    df = pd.concat([p.loc[:, :, year], region_name], axis=1).reset_index()
    data[year] = df.to_dict('series')

print('saved')
print("1.")
source = ColumnDataSource(data=data[years[0]])
print("2.")
plot = figure(x_range=(7, 68), y_range=(0.0, 28), title='Gapminder Data', plot_height=250)
plot.xaxis.ticker = SingleIntervalTicker(interval=5)
plot.xaxis.axis_label = "GDP Per Capita ($USD)"
plot.yaxis.ticker = SingleIntervalTicker(interval=1)
plot.yaxis.axis_label = "Unemployment Rate"
print("3.")
label = Label(x=1.1, y=18, text=str(years[0]), text_font_size='70pt', text_color='#eeeeee')
plot.add_layout(label)
print("4.")
print(regions_list)
print(Spectral6)
color_mapper = CategoricalColorMapper(palette=Spectral6, factors=regions_list)

plot.circle(
    x='gdp_pc',
    y='unemployment_rate',
    size='tech_export',    
    source=source,
    fill_color={'field': 'region', 'transform': color_mapper},
    fill_alpha=0.8,
    line_color='#7c7e71',
    line_width=0.5,
    line_alpha=0.5,
    legend=field('region'),
)
plot.add_tools(HoverTool(tooltips="@index", show_arrow=False, point_policy='snap_to_data')) #'follow_mouse'))

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
        callback_id = curdoc().add_periodic_callback(animate_update, 400)
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
