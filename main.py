mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

missionTotal = 0
successTotal = 0
beforeY2K = []

for i in mission_names:
    missionTotal += 1
print("Total number of missions: " + str(missionTotal))

for i in mission_success:
    if i == True:
        successTotal += 1
print("Number of successful missions: " + str(successTotal))

print("Success rate: " + str(round(successTotal / missionTotal * 100, 2)) + "%")

print("Missions launched before the year 2000: ")
for i in mission_years:
    if i < 2000:
        x = mission_years.index(i)
        print("- " + str(mission_names[x]))