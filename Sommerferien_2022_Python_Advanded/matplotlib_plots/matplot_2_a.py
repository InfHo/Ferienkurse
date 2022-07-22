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

print(x)
print(y_2016)

##plt.plot(x, y_2016,
##         color= 'g',
##         linestyle = 'dashed',
##         marker = 'o',
##         label = "Bodenfläche")

plt.bar(x, y_2016,
         color= 'hot',
        width= 0.8,
         label = "Bodenfläche")

plt.xlabel = "Nutzungsarten"
plt.ylabel = "31.12.2016"
plt.xticks(rotation=90)

##plt.grid()
plt.legend()
plt.show()

