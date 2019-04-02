# CTA Ridership (28pts)

#  Get the csv from the following data set.
#  https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
#  This shows CTA ridership by year going back to the 80s


#1  Make a plot of rail usage for the most current 10 year period.  (year on x axis, and ridership on y) (5pts)
#2  Plot bus usage for the same years as a second line on your graph. (5pts)
#3  Plot bus and rail usage together on a third line on your graph. (5pts)
#4  Add a title and label your axes. (5pts)
#5  Add a legend to show data represented by each of the three lines. (5pts)
#6  What trend or trends do you see in the data?  Offer at least two hypotheses which might explain the trend(s). (3pts)

import csv
import matplotlib.pyplot as plt
import numpy as np

with open("../Notes/data/CTA_-_Ridership_-_Annual_Boarding_Totals.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

headers = data.pop(0)
data = [x for x in data[-10:]]
print(data)

year_list = []
bus_rider_list = []
rail_rider_list = []
total_rider_list = []

for i in data:
    try:
        year = int(i[0])
        bus_riders = int(i[1])
        rail_riders = int(i[-2])
        total_riders = int(i[4])
        year_list.append(year)
        bus_rider_list.append(bus_riders)
        rail_rider_list.append(rail_riders)
        total_rider_list.append(total_riders)
    except ValueError:
        print("Incomplete")


plt.title("CTA Rider Count In The Last 10 Years")
plt.xlabel("Year")
plt.ylabel("Number Of Riders")
plt.plot(year_list, rail_rider_list, label="Rail Riders")
plt.plot(year_list, bus_rider_list, label="Bus Riders", color="red")
plt.plot(year_list, total_rider_list, label="Total Riders", color="black")
plt.legend()

plt.show()

'''
The amount of rail riders has increased, and bus riders have decreased. As train travel has become more accessible, 
bus riders are transferring over because of its speed?
    
Another hypothesis is that train travel has become cheaper and more of a good alternative to buses:
         
On the other hand, maybe new riders all prefer trains so there is more growth in train travel than bus travel
'''
