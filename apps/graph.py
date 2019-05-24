import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import psycopg2


conn = psycopg2.connect(host="john.db.elephantsql.com",database="hibzxjxl", user="hibzxjxl", password="BbJmB-QJQegz1z8f4jmsfsUY0GsNXehi")

cur = conn.cursor()
cur.execute("SELECT * from test_table")
# print("The number of parts: ", cur.rowcount)
row = cur.fetchone()
age=[]
sal=[]
while row is not None:
            age.append(row[1])
            sal.append(row[3])
            row = cur.fetchone()

cur.close()


from app import app

layout = html.Div([
    dcc.Link(html.H3('Home'),style={'text-decoration': 'none'}, href = '/'),
    dcc.Graph(
        id = 'graphss',
        figure = {
            'data': [
                {'x':[x for x in range(0,len(age))], 'y':[y for y in sal], 'type':'line', 'name':'Line'},
                {'x':[x for x in range(0,len(age))], 'y':[y for y in sal], 'type':'bar', 'name':'Bar  '},
                ],
                'layout': {
                'title': 'Graph for Age'
                }
        }
    ),
    dcc.Link('Go to App 1', href='/apps/app1'),
    html.Br(),
    dcc.Link('Go to App 2', href='/apps/app2')
])


