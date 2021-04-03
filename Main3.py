import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    percentage=[]
    days_present=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            days_present.append(float(row['Days Present']))
            percentage.append(float(row['Marks In Percentage']))
    return{'x': percentage,'y': days_present}

def findCorrelation(dataSource):
    Correlation=np.corrcoef(dataSource['x'],dataSource['y'])
    print('correlation between Marks In Percentage & Days Present is =>',Correlation[0,1])

def setUp():
    data_path='M&D.csv'
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setUp()