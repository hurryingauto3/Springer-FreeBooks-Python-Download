import requests
import wget
import pandas as pd
import os

try:
    os.mkdir(os.getcwd() + "/download")
except OSError:
    print("Creation of the directory %s failed" % os.getcwd() + "/download")
else:
    print("Successfully created the directory %s " %
          os.getcwd() + "/download")

# wget.download("https: // resource-cms.springernature.com/springer-cms/rest/v1/content/17858272/data/v4", 
# "Free+English+textbooks.xlxs")


df = pd.read_excel("Free+English+textbooks.xlsx")
for index, row in df.iterrows():
    # loop through the excel list
    file_name = f"{row.loc['Book Title']}_{row.loc['Edition']}".replace(
        '/', '-').replace(':', '-')
    url = f"{row.loc['OpenURL']}"
    r = requests.get(url)
    download_url = f"{r.url.replace('book','content/pdf')}.pdf"
    wget.download(download_url, f"./download/{file_name}.pdf")
    print(f"downloading {file_name}.pdf Complete ....")
