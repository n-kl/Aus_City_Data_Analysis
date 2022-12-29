# Prints 20 most populous cities in Australia, then 5 most populous
# by state, noting also the csv file is already sorted by population.
import pandas as pd

STATES = ["New South Wales", "Northern Territory", "Queensland",
          "South Australia", "Tasmania", "Victoria", "Western Australia"]


# Retrieving data from CSV
def GetData(fileName):
    return pd.read_csv(fileName, header=0, index_col="city")


city_data = GetData("AustralianCities.csv")


# Iterating to find most populous Australian Cities
print("20 Most Populous Australian Cities")
num = 0
for index, row in city_data.iterrows():
    num += 1
    print(num, index, row["population"])
    if(num == 20):
        break

# Iterating to find most populous cities in each state (ignoring Canberra)
for state in STATES:
    in_state = 0

    print(f"\nThe 5 most populous cities in {state}:")
    for index, row in city_data.iterrows():
        if(row["state"] == state):
            in_state += 1
            print(in_state, index, row["population"])
        if(in_state == 5):
            break
