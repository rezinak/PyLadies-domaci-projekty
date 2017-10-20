# 8. Pomocí cyklu for napiš program, který vypíše:
# 0 na druhou je 0
# 1 na druhou je 1
# 2 na druhou je 4
# 3 na druhou je 9
# 4 na druhou je 16
# Jak pojmenuješ proměnnou cyklu?

mocnenec = 0
for x in range(5):
    print(mocnenec, "na druhou je", mocnenec ** 2)
    mocnenec = mocnenec + 1
