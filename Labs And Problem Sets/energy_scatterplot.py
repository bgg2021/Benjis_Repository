# https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking/xq83-jr8c

'''
Energy Efficiency of Chicago Schools (35pts)
Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
We will use this data at the link above to look at schools.  
We will visualize the efficiency of schools by scatter plot.  
We hypothesize that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
An efficient school would have a large ratio of sqft to ghg.  
It would also be interesting to know where Parker lies on this graph???  Let's find out.
Make a scatterplot which does the following:  
- Plots the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (13pts)
- Includes ONLY data for K-12 Schools. (3pts)
- Labelled x and y axis and appropriate title (3pt)
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities. (3pts)
- Label Francis W. Parker. (3pts)
- Create a best fit line for schools shown. (5pts)
- Customize your graph in a discernable way using any technique discussed or one from the API (matplotlib.org). (5pts)

Challenge (for fun if you have time... not required):
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)
'''

import csv
import matplotlib.pyplot as plt
import numpy as np

with open("../Notes/data/Chicago_Energy_Benchmarking.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)
headers = data.pop(0)
print(headers)

ghg_emissions = []
sq_ft_list = []
school_list = []
ghg_intensity = []
name_list = []

for i in data:
    try:
        buildings = i[2]
        if i[6] == "K-12 School":
            school_list.append(i)

    except ValueError:
        print("value error")

for school in school_list:
    try:
        sq_ft = float(school[7])
        ghg = float(school[20])
        intensity = float(school[21])
        name = str(school[2])
        sq_ft_list.append(sq_ft)
        ghg_emissions.append(ghg)
        ghg_intensity.append(intensity)
        name_list.append(name)
    except ValueError:
        print("value error")


plt.scatter(sq_ft_list, ghg_emissions, s=19, alpha=0.6, marker="p", edgecolors="black", )

m, b = np.polyfit(sq_ft_list, ghg_emissions, 1)
fit_x = [0, 700000]
fit_y = [b, m * 700000 + b]
plt.plot(fit_x, fit_y, color="red")
plt.title("GHG Emissions vs Square Footage For Buildings In Chicago")
plt.xlabel("Building Size in Square Feet")
plt.ylabel("GHG Emissions")
plt.annotate("Francis Parker", xy=(sq_ft_list[476], ghg_emissions[476]))


print(school_list[476])
plt.show()


