from readEDWfile import readEDW
import os
import plotly
from math import sin, cos, tan 
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

app_dir = os.path.join(os.getcwd(), 'Ex5')

x,y = readEDW(os.path.join(app_dir, r'data\2197_5.edw'))

# fig = make_subplots(rows=2, cols=2)
fig = go.Figure()

fig.update_yaxes(range=[min(y), max(y)], zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
fig.update_xaxes(range=[min(x), max(x)], zeroline=True, zerolinewidth=2, zerolinecolor='#008000')

for i in range(0,len(x)):
    fig.add_trace(go.Scatter(x=x[i], y=y[i],  name='Цикл {}'.format(i+1)))

# fig.add_trace(go.Scatter(x=x[0], y=y[0],  name='Цикл 1'), 1, 1)
# fig.add_trace(go.Scatter(x=x[1], y=y[1],  name='Цикл 2'), 1, 2)
# fig.add_trace(go.Scatter(x=x[2], y=y[2],  name='Цикл 3'), 2, 1)
# fig.add_trace(go.Scatter(x=x[3], y=y[3],  name='Цикл 4'), 2, 2) 

# fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',  name='f(x)=x<sup>2</sup>'), 1, 2)
# fig.add_trace(go.Scatter(x=x, y=x, mode='markers',name='g(x)=x',
#                          marker=dict(color='LightSkyBlue', size=20, line=dict(color='MediumPurple', width=3))), 1, 2)
# fig.update_layout(legend_orientation="h",
#                   legend=dict(x=.5, xanchor="center"),
#                   hovermode="x",
#                   margin=dict(l=0, r=0, t=0, b=0))
fig.update_traces(hoverinfo="all", hovertemplate="Длина: %{x}<br>Нагрузка: %{y}<br>Замер #: %{i}")
fig.show()