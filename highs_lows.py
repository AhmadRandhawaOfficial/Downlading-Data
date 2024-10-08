import csv
from matplotlib import pyplot as plt

# Get high temperature from files.
filename = 'sitka_weather_07-2018.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # next is used for getting 1st line of file.

    highs = []
    for row in reader:
        highs.append(int(row[5]))  # row[5] corresponds to the TMAX column
    print(highs)  # This will print the list of high temperatures as integers

# Plot Data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

# Format plot
plt.title("Daily high temperature(Max), July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
