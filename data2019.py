import csv

currency_rates = {'AED': 1.91, 'BRL': 1.36, 'CHF': 7.26, 'CNY': 1, 'CZK': 0.29, 'DKK': 0.94, 'EUR': 7.02, 'GBP': 8.02,
                  'HKD': 0.89, 'HRK': 0.93, 'HUF': 0.018, 'ISK': 0.05, 'JPY': 0.049, 'KRW': 0.005, 'MOP': 0.87,
                  'NOK': 0.68, 'PLN': 1.49, 'RSD': 0.06, 'SEK': 0.65, 'SGD': 4.98, 'THB': 0.19, 'TWD': 0.22, 'USD': 7.01,
                  'PEN': 1.83, 'MXN': 0.37, 'RUB': 0.12, 'CLP': 0.0078, 'ZAR': 0.41
                  }

region_dict = {'Polish': 'Poland', 'Japanese': 'Japan', 'Regional Cuisine': 'Other', 'French': 'France', 'Italian': 'Italy',
               'Mediterranean Cuisine': 'Mediterranean', 'Modern French': 'France', 'Chinese': 'China', 'Cantonese': 'China',
               'Classic French': 'France', 'Thai': 'Thailand', 'Modern British': 'United Kingdom', 'French Contemporary': 'France',
               'American': 'USA', 'Mexican': 'Mexico', 'Sichuan': 'China', 'Indian': 'India', 'Californian': 'USA', 'Asian': 'Asia',
               'Spanish': 'Spain', 'Korean': 'South Korea', 'Creative French': 'France', 'Italian Contemporary': 'Italy',
               'Taiwanese': 'China', 'Piedmontese': 'Italy', 'Shanghainese': 'China', 'European Contemporary': 'Europe',
               'Traditional British': 'United Kingdom', 'Middle Eastern': 'Middle Eastern', 'Vietnamese': 'Vietnam',
               'Sicilian': 'Italy', 'American Contemporary': 'USA', 'Southern Thai': 'Thailand', 'Portuguese': 'Portugal',
               'Beijing Cuisine': 'China', 'Provençal': 'France', 'Swiss': 'Switzerland', 'Japanese Contemporary': 'Japan',
               'Asian Influences': 'Asia', 'Peruvian': 'Peru', 'Brazilian': 'Brazil', 'Catalan': 'Spain', 'Alsatian': 'France',
               'Cuisine from Abruzzo': 'Italy', 'Austrian': 'Austria', 'Taizhou': 'China', 'Chao Zhou': 'China', 'Scandinavian': 'Other',
               'Latin American': 'Other', 'Campanian': 'Italy', 'Ligurian': 'Italy', 'Northern Thai': 'Thialand', 'Okonomiyaki': 'Japan',
               'Asian Contemporary': 'Other', 'Huaiyang': 'China', 'Jiangzhe': 'China', 'Spanish Contemporary': 'Spain',
               'Indonesian': 'Indonesia', 'Kushiage': 'Japan', 'Naengmyeon': 'South Korea', 'Lombardian': 'Italy',
               'Creative British': 'United Kingdom', 'Hunanese': 'China', 'Basque': 'Spain', 'Singaporean': 'Singapore',
               'Belgian': 'Belgium', 'Greek': 'Greece', 'Cantonese Roast Meats': 'China', 'Galician': 'Spain', 'Calabrian': 'Italy',
               'Sardinian': 'Italy', 'German': 'Germany', 'Lebanese': 'Lebanon', 'Apulian': 'Italy', 'Malaysian': 'Malaysia',
               'Isan': 'Thailand', 'Roman': 'Italy', 'British Contemporary': 'United Kingdom', 'Swedish': 'Sweden', 'Shandong': 'China',
               'Andalusian': 'Spain', 'Sri Lankan': 'Sri Lanka', 'Bavarian': 'Germany', 'Mandu': 'South Korea', 'Fujian': 'China',
               'Korean Contemporary': 'South Korea', 'Danish': 'Denmark', 'Colombian': 'Colombia', 'Filipino': 'Philippine',
               'Scottish': 'United Kingdom', 'Chinese Contemporary': 'China', 'Ningbo': 'China', 'Thai contemporary': 'Thailand',
               'Cuisine from Romagna': 'Italy', 'Venetian': 'Italy', 'Moroccan': 'Morocco', 'European': 'Other', 'Smørrebrød': 'Norway',
               'Norwegian': 'Norway', 'Turkish': 'Turkey', 'Cuban': 'Cuba', 'Lao': 'Laos', 'Ethiopian': 'Ethiopia', 'Chiu Chow': 'China',
               'Dubu': 'South Korea', 'Kalguksu': 'South Korea', 'Memil-guksu': 'South Korea', 'Cuisine from Valtellina': 'Italy',
               'Umbrian': 'Italy', 'Castilian': 'Spain', 'Corsican': 'France', 'Irish': 'Ireland', 'Zhejiang': 'China', 'Sukiyaki': 'Japan',
               'Hang Zhou': 'China', 'Hungarian': 'Hungary', 'English': 'United Kingdom', 'Breton': 'France', 'Persian': 'Iran',
               'Shun Tak': 'China', 'Chankonabe': 'Japan', 'Gomtang': 'South Korea', 'Jokbal': 'South Korea', 'Seolleongtang': 'South Korea',
               'Gejang': 'South Korea', 'Dwaeji-gukbap': 'South Korea', 'Cuisine from Basilicata': 'Italy', 'Mantuan': 'Italy',
               'Cuisine from Lazio': 'Italy', 'Czech': 'Czech Republic', 'Obanzai': 'Japan', 'Burmese': 'Myanmar', 'Teochew': 'China',
               'Finnish': 'Finland', 'Russian': 'Russia', 'Israeli': 'Israel', 'Dongbei': 'China', 'Emirati Cuisine': 'UAE',
               'Cuisine from South West France': 'France', 'Caribbean': 'Other', 'Afghan': 'Afghanistan', 'South American': 'Other',
               'Cuisine from Franche-Comté': 'France', 'Savoyard': 'Italy', 'Cajun': 'USA', 'South Indian': 'India', 'South African': 'South Africa',
               'Indian Vegetarian': 'India', 'Hubei': 'China', 'Macanese': 'China', 'Xinjiang': 'China', 'Cuisine from Alentejo': 'Portugal',
               'Okinawa Cuisine': 'Japan', 'Onigiri': 'Japan', 'Yukhoe': 'South Korea', 'Bulgogi': 'South Korea', 'Chueotang': 'South Korea',
               'Doganitang': 'South Korea', 'Sujebi': 'South Korea', 'Friulian': 'Italy', 'Pakistani': 'Pakistan', 'Milanese': 'Italy',
               'Xibei': 'China', 'Hakkanese': 'China', 'Yunnanese': 'China', 'Tibetan': 'China', 'Croatian': 'Croatia'

               }

files = {"/Users/kasperxiaomingshen/Documents/Dataset/one-star-michelin-restaurants2019.csv": "1 MICHELIN Star",
        "/Users/kasperxiaomingshen/Documents/Dataset/two-stars-michelin-restaurants2019.csv": "2 MICHELIN Stars",
        "/Users/kasperxiaomingshen/Documents/Dataset/three-stars-michelin-restaurants2019.csv": "3 MICHELIN Stars"}

f_main = open("/Users/kasperxiaomingshen/Documents/visuProjData/michelin_2019_v2_main.csv", "w")
f_main.write('name,longitude,latitude,city,country,award,price\n')
f_cuisine = open("/Users/kasperxiaomingshen/Documents/visuProjData/michelin_2019_v2_cuisine.csv", "w")
f_cuisine.write('name,cuisine,region\n')

for file in files:
    f_origin = open(file, "r")
    reader = csv.reader(f_origin)
    header = next(reader)
    for line in reader:
        name = line[0]
        longitude = line[3]
        latitude = line[2]
        city = line[4]
        country = line[5]
        cuisine = line[7]
        price = -1
        award = files[file]
        region = "Others"

        if line[8] != 'N/A':
            price = len(line[8])

        if country == "California":
            country = "USA"
        elif country == "Chicago":
            country = "USA"
        elif country == "Hong Kong":
            country = "China"
        elif country == "Macau":
            country = "China"
        elif country == "New York City":
            country = "USA"
        elif country == "Rio de Janeiro":
            country = "Brazil"
        elif country == "Sao Paulo":
            country = "Brazil"
        elif country == "Taipei":
            country = "China"
        elif country == "Washington DC":
            country = "USA"

        if cuisine in region_dict:
            region = region_dict[cuisine]
            f_cuisine.write('"{}",{},{}\n'.format(name, cuisine, region))

        f_main.write('"{}",{},{},"{}",{},{},{}\n'.format(name, longitude, latitude, city, country, award, price))

    f_origin.close()

f_main.close()