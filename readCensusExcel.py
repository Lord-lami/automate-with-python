import openpyxl, shelve, pprint

wb = openpyxl.load_workbook('censuspopdata.xlsx')

sheet = wb['Population by Census Tract']

state_2_county_2_tracts_pop = dict()

for r in sheet.rows:
    state = r[1].value
    county = r[2].value
    if state == "State":
        continue
    population = r[3].value

    # If the current state is not in the dictionary keys 
    # add it with an empty dictionary as its value
    state_2_county_2_tracts_pop.setdefault(state, {})

    # If the country is not in the current state's dictionary keys
    # add it with the populationa and tracts dictionary as its value
    state_2_county_2_tracts_pop[state].setdefault(county, {"pop": 0, "tracts": 0})


    state_2_county_2_tracts_pop[state][county]["pop"] += int(population)
    state_2_county_2_tracts_pop[state][county]["tracts"] += 1

# print(state_2_county_2_tracts_pop)

with shelve.open("censuspopdata") as censusdata:
    censusdata["data"] = state_2_county_2_tracts_pop

# Open a new text file and write the contents of county_data to it.
print('Writing results...')
with open('census2010.py', 'w') as result_file:
    result_file.write('allData = ' + pprint.pformat(state_2_county_2_tracts_pop))
print('Done.')