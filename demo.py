import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file

dta = pd.read_csv("~/Projects/pi-cluster/data/rpi_stats.csv")

p = figure(plot_width = 800, plot_height = 400)
p.line(x=dta.index, y=dta.rpi1_cpu_tmp, line_alpha=.3)
p.circle(x=dta.index, y=dta.rpi1_cpu_tmp, alpha=.3)

output_file('index.html')
show(p)
