import csv

currency_rates = {'AED': 1.91, 'BRL': 1.36, 'CHF': 7.26, 'CNY': 1, 'CZK': 0.29, 'DKK': 0.94, 'EUR': 7.02, 'GBP': 8.02,
                  'HKD': 0.89, 'HRK': 0.93, 'HUF': 0.018, 'ISK': 0.05, 'JPY': 0.049, 'KRW': 0.005, 'MOP': 0.87,
                  'NOK': 0.68, 'PLN': 1.49, 'RSD': 0.06, 'SEK': 0.65, 'SGD': 4.98, 'THB': 0.19, 'TWD': 0.22, 'USD': 7.01,
                  'PEN': 1.83, 'MXN': 0.37, 'RUB': 0.12, 'CLP': 0.0078, 'ZAR': 0.41
                  }

f = open('/Users/kasperxiaomingshen/Documents/Dataset/top50_2019.csv')
reader = csv.reader(f)
header = next(reader)

f1 = open('/Users/kasperxiaomingshen/Documents/Dataset/top50_2019_transformed.csv', 'w+')
content = ''
for title in header:
    content += '{},'.format(title)

content = content[:-1]
f1.write(content)
f1.write('\n')
for line in reader:
    line[9] = currency_rates[line[10]] * int(line[9])
    line[9] = str(int(line[9]))
    line[10] = 'CNY'
    content = ''
    for item in line:
        content += '"{}",'.format(item)

    content = content[:-1]
    f1.write(content)
    f1.write('\n')

f1.close()
f.close()