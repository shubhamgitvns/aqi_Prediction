import pandas as pd

data = pd.read_csv("Varanasi_AQI.csv")
print(data.head())

# drop the specific column
data = data.drop(columns=['Prominent Pollutant', 'No. Stations'])
print(data.columns)