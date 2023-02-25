# Import any necessary modules below.


# DO NOT MODIFY BoroughPopulation CLASS DEFINITION.
# Import necessary modules
import pandas as pd

# Define BoroughPopulation class
class BoroughPopulation:
    def __init__(self, p1970, p1980, p1990, p2000, p2010):
        self.pop = dict()
        self.pop[1970] = p1970
        self.pop[1980] = p1980
        self.pop[1990] = p1990
        self.pop[2000] = p2000
        self.pop[2010] = p2010

    def __str__(self):
        result = ""
        for key in self.pop:
            result += str(key) + "->" + str(self.pop[key]) + " "
        return result


# 1. Write the code that reads nyc_population.xml using pandas.read_xml
# functions. Use xpath parameter of read_xml function to correct parse
# the file. Assign the dataframe to the variable named 'df'. [10 pts]

df = pd.read_xml("nyc_population.xml", xpath="/response/row/row")


# 2. Write the code that will add an additional column 'popChangePct' into df
# whose values are defined as the % change in population from 1970 to 2010.
# i.e., popChangePct = (population2010 - population1970) / population1970 * 100
# [10 pts]

df["_1970_population"] = pd.to_numeric(df["_1970_population"])
df["_2010_population"] = pd.to_numeric(df["_2010_population"])

df["popChangePct"] = (
    (df["_2010_population"] - df["_1970_population"]) / df["_1970_population"]
) * 100


# 3. Write the code that creates a dictionary whose key is borough, and the
# value is an object of BoroughPopulation. When creating an object of
# BoroughPopulation, 5 arguments are passed: p1970, p1980, p1990, p2000, p2010.
# For example, p1970 value is the sum of populations in all cd_name's
# under one borough for the year 1970. Assign this dictionary to the variable
# populationDict. [20 pts]

populationDict = {}
for borough in df["borough"].unique():
    borough_df = df[df["borough"] == borough]
    p1970 = borough_df["_1970_population"].sum()
    p1980 = borough_df["_1980_population"].sum()
    p1990 = borough_df["_1990_population"].sum()
    p2000 = borough_df["_2000_population"].sum()
    p2010 = borough_df["_2010_population"].sum()
    borough_population = BoroughPopulation(p1970, p1980, p1990, p2000, p2010)
    populationDict[borough] = borough_population

# Display the populationDict dictionary
for borough, population in populationDict.items():
    print(f"{borough}: {population}")
