#https://www-genesis.destatis.de/genesis/online?operation=abruftabelleBearbeiten&levelindex=2&levelid=1658485898327&auswahloperation=abruftabelleAuspraegungAuswaehlen&auswahlverzeichnis=ordnungsstruktur&auswahlziel=werteabruf&code=33111-0001&auswahltext=&werteabruf=starten#abreadcrumb


import csv
import matplotlib.pyplot as plt
import numpy as np


x = []
y_2016 = []
y_2017 = []
y_2018 = []
y_2019 = []
y_2020 = []

with  open('file.csv') as File:
    lines = csv.reader(File, delimiter=';')
    start = 7
##    print(type(lines))
    for i, row in enumerate(lines):
        if 38 >= i >= start:
##            print(i, row)
            x.append(row[0])
            y_2016.append(float(row[1].replace(",",".")))
            y_2017.append(float(row[2].replace(",",".")))
            y_2018.append(float(row[3].replace(",",".")))
            y_2019.append(float(row[4].replace(",",".")))
            y_2020.append(float(row[5].replace(",",".")))

X_axis = np.arange(len(x))
  
plt.bar(X_axis - 0.2, y_2016, 0.2, label = 'a')
plt.bar(X_axis + 0.2, y_2017, 0.2, label = 'b')
plt.bar(X_axis + 0.4, y_2018, 0.2, label = 'b')
plt.bar(X_axis + 0.6, y_2019, 0.2, label = 'b')
plt.bar(X_axis + 0.8, y_2020, 0.2, label = 'b')
  
plt.xticks(X_axis, x)

##plt.title("Number of Students in each group")
plt.xlabel = "Nutzungsarten"
plt.ylabel = "31.12.2016"
plt.xticks(rotation=90)

plt.legend()
plt.show()
