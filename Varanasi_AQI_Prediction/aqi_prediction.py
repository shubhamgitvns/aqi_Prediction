import pandas as pd

data = pd.read_csv("Varanasi_AQI.csv")
print(data.head())

# drop the specific column
data = data.drop(columns=['Prominent Pollutant', 'No. Stations'])

print(data.isnull().sum())

print(data.info())

# Convert date in date-time

data['date'] = pd.to_datetime(data['date'])

print(data['date'])