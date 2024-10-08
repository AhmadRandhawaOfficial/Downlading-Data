import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Get dates, high and low temperatures from the file.
filename = 'sitka_weather_07-2018.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # Read the first line (header) of the file.

    dates, highs, lows = [], [], []
    for row in reader:
        # Parse the date and high temperature.
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(int(row[5]))  # Convert temperature to an integer
        lows.append(int(row[6]))

    # Plot the data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

# Format the plot.
plt.title("Daily High and Low Temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # Rotate date labels for better readability.
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# Show the plot.
plt.show()
