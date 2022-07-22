#https://www-genesis.destatis.de/genesis/online?operation=abruftabelleBearbeiten&levelindex=2&levelid=1658485898327&auswahloperation=abruftabelleAuspraegungAuswaehlen&auswahlverzeichnis=ordnungsstruktur&auswahlziel=werteabruf&code=33111-0001&auswahltext=&werteabruf=starten#abreadcrumb


import csv
import matplotlib.pyplot as plt


x = []
y_2016 = []

with  open('file.csv') as File:
    lines = csv.reader(File, delimiter=';')
    start = 7
##    print(type(lines))
    for i, row in enumerate(lines):
        if 38 >= i >= start:
##            print(i, row)
            x.append(row[0])
            y_2016.append(float(row[1].replace(",",".")))

##fig1, ax1 = plt.subplots()
##ax1.pie(y_2016,  labels=x, autopct='%1.1f%%',
##        shadow=True, startangle=90)
##ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
##
##plt.show()

for y in y_2016:
    print(y)
