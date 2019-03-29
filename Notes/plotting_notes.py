# PLOTTING (with matplotlib)

import matplotlib.pyplot as plt
import random

'''

plt.figure(1)  # creates a new window

plt.plot([1, 2, 4, 4])  # plots y and x against the index
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])  # plot(x_data, y_data)

plt.figure(2) # make a second window

x1 = [x for x in range(1, 101)]
y1 = [y ** 2 for y in x1]
plt.plot(x1, y1)

x2 = [x for x in range(1, 101)]
y2 = [random.randrange(1000) for y in range(100)]
plt.plot(x2, y2, color='purple', marker='o', markersize=5, linestyle='--', alpha=1)

plt.xlabel('time (seconds)', color='black')
plt.ylabel('intensity (dB)')
plt.title('Example Plot')
plt.axis([0, 50, 0, 1000]) # xmin, xmax, ymin, ymax

plt.show()

'''

import csv

with open("data/Libraries_-_2018_Visitors_by_Location (1).csv") as f:
    reader = csv.reader(f)  # makes a reader object to pull in the data
    data = list(reader)  # casts the reader as a list

header = data.pop(0)

library_names = [x[0] for x in data]

monthly_data = [x[1:-1] for x in data]

lp_data = monthly_data[library_names.index('Lincoln Park')]

try:
    lp_data = [int(x) for x in lp_data]
except:
    print("couldn't convert this data val to int")

print(lp_data)

months = [x for x in header[1:-1]]

plt.figure(3, tight_layout=True)
plt.axis([0, 12, 0, 18000])
plt.plot(lp_data, marker='o')
month_numbers = [x for x in range(12)]
plt.xticks(month_numbers, months, rotation=45) # puts text on axis
plt.show()