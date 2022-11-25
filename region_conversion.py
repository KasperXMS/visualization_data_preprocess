import csv

name_dict = {'Poland': 'Polish', 'Japan': 'Japanese', 'France': 'French', 'Italy': 'Italian', 'China': 'Chinese',
             'Thailand': 'Thai', 'United Kingdom': 'British', 'USA': 'American', 'Mexico': 'Mexican', 'India': 'Indian',
             'Asia': 'Asian', 'Spain': 'Spanish', 'South Korea': 'South Korean', 'Europe': 'European',
             'Portugal': 'Portuguese', 'Vietnam': 'Vietnamese', 'Switzerland': 'Swiss', 'Peru': 'Peruvian',
             'Brazil': 'Brazilian', 'Indonesia': 'Indonesian', 'Singapore': 'Singaporean', 'Belgium': 'Belgian',
             'Greece': 'Greek', 'Germany': 'German', 'Lebanon': 'Lebanese', 'Malaysia': 'Malaysian', 'Sweden': 'Swedish',
             'Sri Lanka': 'Sri Lankan', 'Denmark': 'Danish', 'Colombian': 'Colombia', 'Philippine': 'Filipino',
             }

def change_region(filepath, col):
    f = open(filepath, 'r')
    f1 = open(filepath[:-4] + "_" + filepath[-4:], 'w')
    reader = csv.reader(f)
    writer = csv.writer(f1)
    header = next(reader)
    writer.writerow(header)
    for line in reader:
        if line[col] in name_dict:
            line[col] = name_dict[line[col]]

        writer.writerow(line)

    f.close()
    f1.close()

if __name__ == "__main__":

    filelist = [('/Users/kasperxiaomingshen/Documents/visuProjData/new/changed_regional_cuisine.csv', 2),
                ('/Users/kasperxiaomingshen/Documents/visuProjData/new/region_cuisine_2019_not_2021.csv', 2),
                ('/Users/kasperxiaomingshen/Documents/visuProjData/new/region_cuisine_2021_not_2019.csv', 2),
                ('/Users/kasperxiaomingshen/Documents/visuProjData/new/michelin_2019_v2_cuisine.csv', 2),
                ('/Users/kasperxiaomingshen/Documents/visuProjData/new/michelin_2021_v2_cuisine.csv', 3)]

    for file in filelist:
        change_region(file[0], file[1])