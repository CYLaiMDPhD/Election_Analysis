counties = ["Arapahoe","Denver","Jefferson"]
#if counties [1] =='Denver':
    #print(counties[1])

#if "Arapahoe" in counties or "El Paso" in counties:
    #print ("Yes")
#else:
    #print ("No")

#for county in counties:
    #print(county)


counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

#for county in counties_dict:
    #print(county)

#for voters in counties_dict.values():
    #print(county)
    #print(voters)

#for county,voters in counties_dict.items():
    #print(county," county has ", voters, " registered voters")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    #print(county_dict)
    print(f"{county_dict['county']} county has {county_dict['registered_voters']} registered voters/")
    #for values in county_dict.values():
    #   print(values)
    #   print(county_dict[county])

#for county, voters in counties_dict.items():
    #print(f"{county} county has {voters} registered voters.")