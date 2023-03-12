points = int(input())
bonus = 0

if points <= 100:
    bonus = 5
elif 100 < points <= 1000:
    bonus = points*0.2
elif points > 1000:
    bonus = points*0.1

if points % 2 == 0:
    bonus_final = bonus + 1
    total_points = points + bonus + 1
    print(bonus_final)
    print(total_points)
elif points % 10 == 5:
    total_points = points + bonus + 2
    print(bonus+2)
    print(total_points)
else:
    print(bonus)
    print(bonus+points)

