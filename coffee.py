import csv
import plotly.express as px
import numpy as np
with open('coffee.csv') as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x='Coffee',y='Hours')
    fig.show()

def getDataSource(data_path):
    coffee=[]
    hours=[]
    with open('coffee.csv') as f:
        df=csv.DictReader(f)
        for row in df:
            coffee.append(float(row['Coffee']))
            hours.append(float(row['Hours']))
    return {'x':coffee,'y':hours}

def findCorellation(data_source):
    corellation=np.corrcoef(data_source['x'],data_source['y'])
    print('corellation between amount of coffee and hours of sleep is:',corellation[0,1])

def setUp():
    data_path='coffee.csv'
    data_source=getDataSource(data_path)
    findCorellation(data_source)

setUp()