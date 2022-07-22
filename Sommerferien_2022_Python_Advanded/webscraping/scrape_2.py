import requests
from bs4 import BeautifulSoup

url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

url_2 = "http://infho.eu/oiwrhwuihfgu"

result = requests.get(url)

#print(result.text)

doc = BeautifulSoup(result.text, "html.parser")

preise = doc.find_all(text="$")

print(preise)

print(preise[0].parent)

preis_dollar = preise[0].parent.find("strong")

print(preis_dollar.string)
