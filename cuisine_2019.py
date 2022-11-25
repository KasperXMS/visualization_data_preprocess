import csv
import pymysql

region_dict = {'Polish': 'Poland', 'Japanese': 'Japan', 'Regional Cuisine': 'Other', 'French': 'France', 'Italian': 'Italy',
               'Mediterranean Cuisine': 'Mediterranean', 'Modern French': 'France', 'Chinese': 'China', 'Cantonese': 'China',
               'Classic French': 'France', 'Thai': 'Thailand', 'Modern British': 'United Kingdom', 'French Contemporary': 'France',
               'American': 'USA', 'Mexican': 'Mexico', 'Sichuan': 'China', 'Indian': 'India', 'Californian': 'USA', 'Asian': 'Asia',
               'Spanish': 'Spain', 'Korean': 'South Korea', 'Creative French': 'France', 'Italian Contemporary': 'Italy',
               'Taiwanese': 'China', 'Piedmontese': 'Italy', 'Shanghainese': 'China', 'European Contemporary': 'Europe',
               'Traditional British': 'United Kingdom', 'Middle Eastern': 'Middle Eastern', 'Vietnamese': 'Vietnam',
               'Sicilian': 'Italy', 'American Contemporary': 'USA', 'Southern Thai': 'Thailand', 'Portuguese': 'Portugal',
               'Beijing Cuisine': 'China', 'Provençal': 'France', 'Swiss': 'Switzerland', 'Japanese Contemporary': 'Japan',
               'Asian Influences': 'Asia', 'Peruvian': 'Peru', 'Brazilian': 'Brazil', 'Catalan': 'Spain'
               }

db = pymysql.connect(host='124.223.97.211', user='user1', password='hijodeputa', database='michelin')
f = open('/Users/kasperxiaomingshen/Documents/regional_cuisines_2019.csv', 'w+')
f.write('name,cuisine,city,price,longitude,latitude,award,region\n')
cursor = db.cursor()
res_list = []
regionals = 0
sql = 'SELECT r.name, c.cuisine, r.city, r.price, r.Longitude, r.Latitude, r.award ' \
    "from cuisine c, restaurant_2019 r where c.`name` = r.`name`"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for result in results:
        name = result[0]
        cuisine = result[1]
        city = result[2]
        price = result[3]
        longitude = result[4]
        latitude = result[5]
        award = result[6]
        if cuisine in region_dict:
            regionals += 1
            region = region_dict[cuisine]
        else:
            region = 'Other'
        f.write('"{}",{},"{}",{},{},{},{},{}\n'.format(name, cuisine, city, price, longitude, latitude, award, region))

except:
    print("Unable to fetch data!")

f.close()
db.close()
print(regionals)

