import pandas as pd

STATES = ["New South Wales", "Northern Territory", "Queensland",
          "South Australia", "Tasmania", "Victoria", "Western Australia"]


def GetData(fileName):
    return pd.read_csv(fileName, header=0, index_col="city")


# Retrieving csv data
city_data = GetData("AustralianCities.csv")

# Sorting csv data by latitude into new sorted file
sorted_city_data = city_data.sort_values(by=["lat"], ascending=False)
sorted_city_data.to_csv("LatSortedCities.csv")

# Iterating to find most northern Australian Cities
print("20 Most Northern Australian Cities")
num = 0
for index, row in sorted_city_data.iterrows():
    num += 1
    print(num, index, row["lat"])
    if(num == 20):
        break

# Iterating to find most northern cities in each state (ignoring Canberra)
for state in STATES:
    in_state = 0

    print(f"\nThe 5 most northern cities in {state}:")
    for index, row in sorted_city_data.iterrows():
        if(row["state"] == state):
            in_state += 1
            print(in_state, index, row["lat"])
        if(in_state == 5):
            break
