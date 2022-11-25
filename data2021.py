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

f_origin = open("/Users/kasperxiaomingshen/Documents/Dataset/michelin_my_maps2021.csv", "r")
f_main = open("/Users/kasperxiaomingshen/Documents/visuProjData/michelin_2021_v2_main.csv", "w")
f_main.write('name, address, country, city, minPrice, maxPrice,longitude, latitude, award\n')
f_cuisine = open("/Users/kasperxiaomingshen/Documents/visuProjData/michelin_2021_v2_cuisine.csv", "w")
f_cuisine.write('name, address, cuisine, region\n')
f_service = open("/Users/kasperxiaomingshen/Documents/visuProjData/michelin_2021_v2_service.csv", "w")
f_service.write('name, address, service\n')
reader = csv.reader(f_origin)
header = next(reader)
for line in reader:
    if line[5] != '':
        name = line[0]
        address = line[1]
        country = address.split(", ")[-1]
        city = line[2]
        if line[3] == '':
            line[3] = "-1"
        if line[4] == '':
            line[4] = "-1"

        minPrice = int(int(line[3].replace(",", "")) * currency_rates[line[5]])
        maxPrice = int(int(line[4].replace(",", "")) * currency_rates[line[5]])
        cuisines = line[6].split(',')
        longitude = line[7]
        latitude = line[8]
        award = line[12]
        services = line[13].split(',')
        cuisine_region = ''

        # 遵循一个中国 我辈义不容辞
        if country == 'China Mainland':
            country = 'China'
        elif country == 'Hong Kong':
            country = 'China'
        elif country == 'Macau':
            country = 'China'
        elif country == 'Taipei & Taichung':
            country = 'China'
        elif country == 'Dubai':
            country = 'UAE'

        for cuisine in cuisines:
            if cuisine in region_dict:
                cuisine_region = region_dict[cuisine]
                f_cuisine.write('"{}","{}",{},{}\n'.format(name, address, cuisine, cuisine_region))
            else:
                cuisine_region = 'Others'


        for service in services:
            f_service.write('"{}","{}",{}\n'.format(name, address, service))


        f_main.write('"{}","{}",{},{},{},{},{},{},{}\n'.format(name, address, country, city, minPrice, maxPrice, longitude, latitude, award))

f_main.close()
f_cuisine.close()
f_service.close()

