
# baue rechnung vom anfang in schleife ein

for i in range(15):
    zahl_3 = 14
    zahl_4 = i+1
    re_7 = zahl_3 // zahl_4
    re_8 = zahl_3 % zahl_4

    re_9 = zahl_3 + zahl_4
    re_10 = zahl_3 - zahl_4
    re_11 = zahl_3 * zahl_4

    re_12 = zahl_3 ** zahl_4

    print("Division > ", zahl_3,":",zahl_4,"=",re_7, "Rest:", re_8)
    print("Addition >", zahl_3, "+", zahl_4, "=", re_9)
    print("Subtraktion >", zahl_3, "-", zahl_4, "=", re_10)
    print("Multiplikation >", zahl_3, "*", zahl_4, "=", re_11)
    print("Hochzahl >", zahl_3, "**", zahl_4, "=", re_12)
    print("")
