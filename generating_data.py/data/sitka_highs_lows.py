import csv
from datetime import datetime


import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high and low temperatures from this file.

    dates, rains = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rain = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            rains.append(rain)

    # Plot the high and low temperatures
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, rains, c='red', alpha=0.5)

    # Format plot.
    title = "Daily Precipitation - 2018\nSitka, AL"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Precipitation (%)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    
    plt.show()