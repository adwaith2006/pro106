import csv
import plotly.express as px
import numpy as np
with open('students.csv') as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x='Marks',y='Days')
    fig.show()

def getDataSource(data_path):
    marks=[]
    days=[]
    with open('students.csv') as f:
        df=csv.DictReader(f)
        for row in df:
            marks.append(float(row['Marks']))
            days.append(float(row['Days']))
    return {'x':marks,'y':days}

def findCorellation(data_source):
    corellation=np.corrcoef(data_source['x'],data_source['y'])
    print('corellation between marks in percentage and days present:',corellation[0,1])

def setUp():
    data_path='students.csv'
    data_source=getDataSource(data_path)
    findCorellation(data_source)

setUp()