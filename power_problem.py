'''
Use the power_data.csv file AND the zipcode database
to answer the questions below.  Make sure all answers
are printed in a readable format.
(i.e. "The city with the highest electricity cost in Illinois is XXXXX."

The power_data dataset, compiled by NREL using data from ABB,
the Velocity Suite and the U.S. Energy Information
Administration dataset 861, provides average residential,
commercial and industrial electricity rates by zip code for
both investor owned utilities (IOU) and non-investor owned
utilities. Note: the file includes average rates for each
utility, but not the detailed rate structure data found in the
OpenEI U.S. Utility Rate Database.

This is a big data set.
Below are some questions that you likely would not be able
to answer without some help from a programming language.
It's good geeky fun.  Enjoy

FOR ALL THE RATES, ONLY USE THE BUNDLED VALUES (NOT DELIVERY).
This rate includes transmission fees and grid fees that are part of the true rate.
'''

#1  What is the average residential rate for YOUR zipcode?
# You will need to read the power_data into your program to answer this.  (7pts)
import csv
from operator import itemgetter
power_data = open("power_data.csv")
def read(file, big_list, illinois):
    reader = csv.reader(file, delimiter = ",")
    for line in reader:
        big_list.append(line)
    for i in range(len(big_list)):
        if big_list[i][3] == "IL":
            illinois.append(big_list[i])
all_data = []
my_zipcode = []
data = []
read(power_data, all_data, data)

data.sort(key = itemgetter(0))
for j in range(len(data)):
    if data[j][0] == "60657" and data[j][4] == "Bundled":
        my_zipcode.append(float(data[j][8]))

total = 0
print(my_zipcode)
for l in range(len(my_zipcode)):
    total += my_zipcode[l]

average = total/len(my_zipcode)
print("The average residential rate for " + str(60657) + " is " + str(total))

#2 What is the MEDIAN rate for all BUNDLED RESIDENTIAL rates in Illinois?
# Use the data you extracted to check all "IL" zipcodes to answer this. (10pts)

IL = []
for k in range(len(data)):
    if data[k][3] == "IL":
        IL.append(data[k])

IL.sort(key = itemgetter(8))
print("The median rate of the bundled residential rates in Illinois is: " + str(IL[len(IL)//2][8]))

#3 What city in Illinois has the lowest residential rate?  Which has the highest?
# You will need to go through the database and compare each value for this one.
# Then you will need to reference the zipcode dataset to get the city.  (15pts)

zip_file = open("free-zipcode-database-Primary.csv")
zip_data = []
zip_bundled = []

read(zip_file, zip_data, zip_bundled)

lowest_rate_zip = IL[0][0]
highest_rate_zip = IL[len(IL)-1][0]
print(lowest_rate_zip, highest_rate_zip)

print(zip_bundled)

#FOR #4  CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS. The first one is easier than the second.
#4  (Easier) USING ONLY THE ZIP CODE DATA...
# Make a scatterplot of all the zip codes in Illinois according to their Lat/Long.
# Make the marker size vary depending on the population contained in that zip code.
# Add an alpha value to the marker so that you can see overlapping markers.

#4 (Harder) USING BOTH THE ZIP CODE DATA AND THE POWER DATA... Make a scatterplot of all
# zip codes in Illinois according to their Lat/Long.  Make the marker red for the top 25% in residential power rate.
# Make the marker yellow for the middle 25 to 50 percentile. Make the marker green if customers pay
# a rate in the bottom 50% of residential power cost.  This one is very challenging.
# You are using data from two different datasets and merging them into one.  There are many ways to solve. (20pts)

