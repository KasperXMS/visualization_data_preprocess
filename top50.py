from wordcloud import WordCloud
import os
import pandas as pd

root = "/Users/kasperxiaomingshen/Documents/top50Review"
def get_file_list(path):
    for root, dirs, files in os.walk(path):
        print(files)

    return files

file_names = get_file_list(root)

success_file_list = []
vocabulary = ""

for filename in file_names:
    path = root + "/" + filename
    try:
        df = pd.read_excel(path)
        success_file_list.append(path)
        for value in df["review_text"].values:
            if value.startswith("(Translated by Google)"):
                value = value.split("(Original)")[0]
                value = value.replace("\n", "")
                value = value.replace("(Translated by Google)", "")

            vocabulary += value

    except:
        print()

cloud = WordCloud(width=800, height=600).generate(vocabulary)
imcloud = cloud.to_image()
imcloud.show()
