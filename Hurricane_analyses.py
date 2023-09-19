# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille',
            'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September',
            'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977,
            1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
                    175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], [
    'Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M',
            'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
            2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
                "B": 1000000000}

# test function by updating damages


def convert_to_flout(damges_list):
    new_list_damge = []
    for damge in damges_list:
        if damge[-1] == 'M':
            num_str = damge
            num_str = num_str.replace(',', '')  # remove any commas
            num_str = num_str.replace('M', '')  # remove the word "million"
            num_float = float(num_str)  # convert to a float
            num_float *= 10**6  # multiply by 10^6 to get the actual value
            new_list_damge.append(num_float)
            conversion[damge] = num_float
        elif damge[-1] == 'B':
            num_str = damge
            num_str = num_str.replace(',', '')  # remove any commas
            num_str = num_str.replace('B', '')
            num_float = float(num_str)  # convert to a float
            num_float *= 10**9  # multiply by 10^6 to get the actual value
            new_list_damge.append(num_float)
            conversion[damge] = num_float
        else:
            new_list_damge.append('Missing Data')
            if damge not in conversion:
                conversion['Missing Data'] = "Damages not recorded"

    return new_list_damge


# 2
# Create a Table
hurricannes_data_byName = {}
# Create and view the hurricanes dictionary


def hurricane_data_func(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    for name, month, year, sust_wind, area, damge, num_of_death in zip(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
        herrcanne = {}
        herrcanne.update({
            'Name': name,
            'Month': month,
            'Year': year,
            'Max Sustained Wind': sust_wind,
            'Areas Affected': area,
            'Damges': damge,
            'Deaths': num_of_death
        })
        hurricannes_data_byName.update({name: herrcanne})
    return hurricannes_data_byName


hurricane_data_func(names, months, years, max_sustained_winds,
                    areas_affected, damages, deaths)


# Organizing by Year
hurricanes_data_byYear = {}

# create a new dictionary of hurricanes with year as key


def organize_hurricanes_by_year(hurricannes_data_byName):
    for name in hurricannes_data_byName:
        hurricanes_data_byYear.update(
            {hurricannes_data_byName[name]["Year"]: [hurricannes_data_byName[name]]})
    return hurricanes_data_byYear


hurricanes_data_byYear = organize_hurricanes_by_year(hurricannes_data_byName)


# 4
# Counting Damaged Areas
counting_damaged_areas = {}
# create dictionary of areas to store the number of hurricanes involved in


def count_damage_area_func(areas_affected):
    for areas in areas_affected:
        for j in areas:
            if j in counting_damaged_areas:
                counting_damaged_areas[j] += 1
            else:
                counting_damaged_areas.update({j: 0})
                counting_damaged_areas[j] += 1
    return counting_damaged_areas


count_damage_area_func(areas_affected)


# 5
# Calculating Maximum Hurricane Count
def Maximum_Hurricane_Count(counting_damaged_areas):
    target_value = max(counting_damaged_areas.values())
    list_for_area_hit = [
        key for key, value in counting_damaged_areas.items() if value == target_value]
    maximum_area = list_for_area_hit[0]
    new_dict_most_hit = {}
    new_dict_most_hit.update({maximum_area: target_value})
    return new_dict_most_hit


# find most frequently affected area and the number of hurricanes involved in
print(Maximum_Hurricane_Count(counting_damaged_areas))
# 6

maximum_death_herricane = {}
# Calculating the Deadliest Hurricane


def maximum_herricane_deaths(names, deaths):

    max_death = max(deaths)
    max_death_index = deaths.index(max_death)
    maximum_death_herricane[names[max_death_index]] = max_death
    return maximum_death_herricane


# find highest mortality hurricane and the number of deaths
print(maximum_herricane_deaths(names=names, deaths=deaths))

# 7 rated by their windspeed,
mortality_scale = {
    0: 0,
    1: 100,
    2: 500,
    3: 1000,
    4: 10000}
# Rating Hurricanes by Mortality
hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
# categorize hurricanes in new dictionary with mortality severity as key


def rating_herricanes_by_widns(names, max_sustained_winds):

    for i in range(len(names)):
        max_winds = max_sustained_winds[i]
        name = names[i]
        if max_winds >= 0 and max_winds <= 99:
            hurricanes_by_mortality[0].append(name)
        elif max_winds >= 100 and max_winds <= 499:
            hurricanes_by_mortality[1].append(name)
        elif max_winds >= 500 and max_winds <= 999:
            hurricanes_by_mortality[2].append(name)
        elif max_winds >= 1000 and max_winds <= 9999:
            hurricanes_by_mortality[3].append(name)
        elif max_winds >= 1000:
            hurricanes_by_mortality[4].append(name)
            print(hurricanes_by_mortality)
    return hurricanes_by_mortality


print(rating_herricanes_by_widns(names=names,
        max_sustained_winds=max_sustained_winds))
# 8
# Calculating Hurricane Maximum Damage

hurricane_maximum_damge = {}


def Hurricane_Maximum_Damage(conversion, hurricannes_data_byName):
    new_list_damage = []
    for i in conversion.values():
        print(i)
        if type(i) == float:
            new_list_damage.append(i)
    max_damge = max(new_list_damage)
    for key1, value1 in conversion.items():
        for key2, value2 in hurricannes_data_byName.items():
            if key1 == value2['Damges'] and float(value1) == max_damge:
                hurricane_maximum_damge[key2] = value1
    return hurricane_maximum_damge


print(Hurricane_Maximum_Damage(conversion, hurricannes_data_byName))


damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key


def Hurricane_Maximum_Damage_list(conversion, hurricannes_data_byName):
    hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    hurricane_maximum_damge = {}
    new_list_damage = []
    for i in conversion.values():
        if type(i) == float:
            new_list_damage.append(i)
    max_damge = max(new_list_damage)
    for key1, value1 in conversion.items():
        for key2, value2 in hurricannes_data_byName.items():
            if key1 == value2['Damges']:
                hurricane_maximum_damge[key2] = value1
    for name, damge in hurricane_maximum_damge.items():
        if damge >= 0 and damge < 100000000:
            hurricanes_by_damage[0].append(name)
        elif damge >= 100000000 and damge < 1000000000:
            hurricanes_by_damage[1].append(name)
        elif damge >= 1000000000 and damge < 10000000000:
            hurricanes_by_damage[2].append(name)
        elif damge >= 10000000000 and damge < 50000000000:
            hurricanes_by_damage[3].append(name)
        elif damge >= 50000000000:
            hurricanes_by_damage[4].append(name)
    return hurricanes_by_damage


Hurricane_Maximum_Damage_list(conversion, hurricannes_data_byName)


