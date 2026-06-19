import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("Varanasi_AQI.csv")
print(data.tail())

# drop the specific column
data = data.drop(columns=['Prominent Pollutant', 'No. Stations'])

# Convert date in date-time

data['date'] = pd.to_datetime(data['date'])


# create the column of year
data['Year'] = data['date'].dt.year

# Create the gaping data table


yearly_aqi = data.groupby('Year')['Index Value'].mean().reset_index()

gap_data = pd.DataFrame({
    'Year': [2024,2025,2026],
    'Index Value': [86.0,120.1233,184.43553]
})

yearly_aqi = pd.concat([yearly_aqi, gap_data], ignore_index=True)




# # Start fiting the model values
X = yearly_aqi['Year'].values.reshape(-1,1)
y = yearly_aqi['Index Value'].values

model = LinearRegression()
model.fit(X,y)

# new_data = model.predict({'Year': [2027]})

print(model.predict([[2027]]))

