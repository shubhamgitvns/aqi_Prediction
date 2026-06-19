import pandas as pd

data = pd.read_csv("Varanasi_AQI.csv")
print(data.head())
# Remove nan values
data = data.dropna(subset=['No. Stations'])

print(data.isnull().sum())