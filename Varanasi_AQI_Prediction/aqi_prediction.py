import pandas as pd

data = pd.read_csv("Varanasi_AQI.csv")
print(data.tail())

# drop the specific column
data = data.drop(columns=['Prominent Pollutant', 'No. Stations'])

# Convert date in date-time

data['date'] = pd.to_datetime(data['date'])


# create the column of year
data['Year'] = data['date'].dt.year

yearly_aqi = data.groupby('Year')['Index Value'].mean()
yearly_aqi = yearly_aqi.reset_index()

print(yearly_aqi['Index Value'])