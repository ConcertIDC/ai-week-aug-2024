import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
data = """
Date,META_Close,TESLA_Close,META_YTD_Change,TESLA_YTD_Change
2024-01-02,346.2900085449219,248.4199981689453,0.0,0.0
...
2024-08-21,535.1599731445312,223.27000427246094,0.5454098008580243,-0.10123981193889384
"""
data = [line.split(',') for line in data.split('\n')[1:] if line]
df = pd.DataFrame(data[1:], columns=data[0])
for col in df.columns[1:]:
    df[col] = df[col].astype(float)
df['Date'] = pd.to_datetime(df['Date'])

# Perform basic analysis
meta_close_mean = df['META_Close'].mean()
tesla_close_mean = df['TESLA_Close'].mean()
meta_close_median = df['META_Close'].median()
tesla_close_median = df['TESLA_Close'].median()
meta_close_std = df['META_Close'].std()
tesla_close_std = df['TESLA_Close'].std()

meta_ytd_change_mean = df['META_YTD_Change'].mean()
tesla_ytd_change_mean = df['TESLA_YTD_Change'].mean()
meta_ytd_change_median = df['META_YTD_Change'].median()
tesla_ytd_change_median = df['TESLA_YTD_Change'].median()
meta_ytd_change_std = df['META_YTD_Change'].std()
tesla_ytd_change_std = df['TESLA_YTD_Change'].std()

# Plot the closing prices over time
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['META_Close'], label='META')
plt.plot(df['Date'], df['TESLA_Close'], label='TESLA')
plt.title('Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()

# Plot the year-to-date changes over time
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['META_YTD_Change'], label='META')
plt.plot(df['Date'], df['TESLA_YTD_Change'], label='TESLA')
plt.title('Year-to-Date Changes Over Time')
plt.xlabel('Date')
plt.ylabel('Year-to-Date Change')
plt.legend()
plt.show()