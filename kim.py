import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

seventeen = pd.read_json("https://missingmigrants.iom.int/global-figures/2017/json")
# sixteen = pd.read_json("https://missingmigrants.iom.int/global-figures/2016/json")
# fifteen = pd.read_json("https://missingmigrants.iom.int/global-figures/2015/json")
# fourteen = pd.read_json("https://missingmigrants.iom.int/global-figures/2014/json")

# frames = [seventeen,sixteen,fifteen,fourteen]

# df = pd.concat(frames)
df = seventeen
df = df.replace('', 0,regex=True)


df['Reported Date'] = pd.to_datetime(df['Reported Date'])

# df['UNSD Geographical Grouping'] = pd.Categorical(df['UNSD Geographical Grouping']).codes
# `

df['UNSD Geographical Grouping'], geoIndex = pd.Series(df['UNSD Geographical Grouping']).factorize()
df['Migrant Route'], migrantIndex = pd.Series(df['Migrant Route']).factorize()
df['Region of Incident'], regionIndex = pd.Series(df['Region of Incident']).factorize()

# fourteen = df[(df['Reported Date'] >= '2014-01-01') & (df['Reported Date'] < '2015-01-01')]
print("here")
print("here")

# pd.to_datetime(df['Reported Date'])