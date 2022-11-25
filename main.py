import csv
import pymysql

currency_rates = {'AED': 1.91, 'BRL': 1.36, 'CHF': 7.26, 'CNY': 1, 'CZK': 0.29, 'DKK': 0.94, 'EUR': 7.02, 'GBP': 8.02,
                  'HKD': 0.89, 'HRK': 0.93, 'HUF': 0.018, 'ISK': 0.05, 'JPY': 0.049, 'KRW': 0.005, 'MOP': 0.87,
                  'NOK': 0.68, 'PLN': 1.49, 'RSD': 0.06, 'SEK': 0.65, 'SGD': 4.98, 'THB': 0.19, 'TWD': 0.22, 'USD': 7.01
                  }


def insert_to_restuarant(db, name, address, country, city, minPrice, maxPrice, Longi, Lati, award, year):
    cursor = db.cursor()

    value = 0

    sql = "insert into restaurant (name, address, country, city, minPrice, maxPrice, Longitude, Latitude, award, year) values (\"{}\", \"{}\", \"{}\", \"{}\", {}, {}, \"{}\", \"{}\", \"{}\", \"{}\")".format(
        name, address, country, city, minPrice, maxPrice, Longi, Lati, award, year)
    try:
        cursor.execute(sql)
        db.commit()
        print("\rSuccess for executing {}".format(sql), end='')
        value = 1
    except:
        print("\nFailed for executing {}".format(sql))
        db.rollback()

    return value

def insert_to_restuarant_2019(db, name, country, city, price, Longi, Lati, award):
    cursor = db.cursor()

    value = 0

    sql = "insert into restaurant_2019 (name, Latiitude, Longitude, city, country, price, award) values (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", {}, \"{}\")".format(
        name, Lati, Longi, city, country, price, award)
    try:
        cursor.execute(sql)
        db.commit()
        print("\rSuccess for executing {}".format(sql), end='')
        value = 1
    except:
        print("\nFailed for executing {}".format(sql))
        db.rollback()

    return value

def insert_into_cuisine(db, address, name, year, cuisine_list):
    value = 0
    for cuisine in cuisine_list:

        cursor = db.cursor()
        sql = "insert into cuisine (address, name, year, cuisine) values (\"{}\", \"{}\", \"{}\", \"{}\")".format(address, name, year, cuisine)
        try:
            cursor.execute(sql)
            db.commit()
            print("\rSuccess for executing {}".format(sql), end='')
            value += 1
        except:
            print("\nFailed for executing {}".format(sql))
            db.rollback()

    return value


def insert_into_service(db, address, name, year, service_list):
    value = 0
    for service in service_list:

        cursor = db.cursor()
        sql = "insert into service (address, name, year, service) values (\"{}\", \"{}\", \"{}\", \"{}\")".format(address, name, year, service)
        try:
            cursor.execute(sql)
            db.commit()
            print("\rSuccess for executing {}".format(sql), end='')
            value += 1
        except:
            print("\nFailed for executing {}".format(sql))
            db.rollback()

    return value


if __name__ == "__main__":

    total_num = 0
    success_num = 0
    total_cuisine = 0
    success_cuisine = 0
    total_service = 0
    success_service = 0

    f = open("/Users/kasperxiaomingshen/Documents/michelin_my_maps.csv")

    db = pymysql.connect(host="124.223.97.211", user="user1", password="hijodeputa", database="michelin")

    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        name = row[0]
        address = row[1]
        country = row[1].split(', ')[-1]
        city = row[2]
        if row[3] == '':
            row[3] = '0'

        if row[4] == '':
            row[4] = '0'

        if row[5] != '':
            minPrice = int(currency_rates[row[5]] * int(row[3].replace(',', '')))
            maxPrice = int(currency_rates[row[5]] * int(row[4].replace(',', '')))
        else:
            minPrice = 0
            maxPrice = 0

        cuisines = row[6].split(', ')
        longi = row[7]
        lati = row[8]
        award = row[12]
        services = row[13].split(',')

        success_num += insert_to_restuarant(db, name, address, country, city, minPrice, maxPrice, longi, lati, award, "2021")
        success_service += insert_into_service(db, address, name, "2021", services)
        success_cuisine += insert_into_cuisine(db, address, name, "2021", cuisines)

        total_num += 1

    michelins_2019 = [('/Users/kasperxiaomingshen/Documents/Dataset/one-star-michelin-restaurants2019.csv', '1 MICHELIN Star'),
                      ('/Users/kasperxiaomingshen/Documents/Dataset/two-stars-michelin-restaurants2019.csv', '2 MICHELIN Stars'),
                      ('/Users/kasperxiaomingshen/Documents/Dataset/three-stars-michelin-restaurants2019.csv', '3 MICHELIN Stars')]

    for file in michelins_2019:
        f = open(file[0])
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            name = row[0]
            year = row[1]
            lati = row[2]
            longi = row[3]
            city = row[4]
            region = row[5]
            cuisine = [row[7]]
            price = len(row[8])
            award = file[1]

            success_num += insert_to_restuarant_2019(db, name, country, city, price, longi, lati, award)
            success_cuisine += insert_into_cuisine(db, address, name, "2019", cuisines)

            total_num += 1



    db.close()
    print(
        "total {}, success {}, success rate: {}".format(total_num, success_num, float(success_num) / float(total_num)))
    print("cuisine data {}, service data {}".format(success_cuisine, success_service))

    f.close()

