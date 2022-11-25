import csv, re, wordcloud

files = ["/Users/kasperxiaomingshen/Documents/Dataset/2019comments/19OneStar_.txt",
        "/Users/kasperxiaomingshen/Documents/Dataset/2019comments/19TwoStar_.txt",
        "/Users/kasperxiaomingshen/Documents/Dataset/2019comments/19ThreeStar_.txt"
        ]

material = ""

for file in files:
    f = open(file)
    lines = f.readlines()

    for line in lines:
        material += line


material = material.replace("’s", "")
material = material.replace("restaurant", "")

cloud = wordcloud.WordCloud(width=800, height=600).generate(material)
cloud.to_file("/Users/kasperxiaomingshen/Desktop/2019comments.jpg")
imcloud = cloud.to_image()
imcloud.show()
imcloud.s