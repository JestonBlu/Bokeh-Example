import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

dta = pd.read_csv("~/Projects/pi-cluster/data/rpi_stats.csv")

output_notebook()

p = figure(plot_width = 800, plot_height = 400)
p.line(x=dta.index, y=dta.rpi1_cpu_tmp)
show(p)
