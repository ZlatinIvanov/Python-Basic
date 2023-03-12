b = int(input("Bitcoins: "))
yuan = int(input("Yuans: "))
c = float(input("Komisionna: "))
commission = c / 100
l = b * 1168
y = yuan * 0.15 * 1.76
lv = l + y
evro = (lv / 1.95)
sum = evro - (evro*commission)
print(round(sum,2))
