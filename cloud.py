import wordcloud
from wordcloud import WordCloud
import csv
f = open("/Users/kasperxiaomingshen/Documents/top50.csv")

reader = csv.reader(f)
header = next(reader)

material = ""
for line in reader:
    material = material + line[11] + " "
f.close()
print(material)
material = material.replace("’s", "")

cloud = wordcloud.WordCloud(width=800, height=600).generate(material)
imcloud = cloud.to_image()
imcloud.show()