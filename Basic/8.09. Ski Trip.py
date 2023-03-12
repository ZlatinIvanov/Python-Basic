days = int(input()) - 1
type_of_room = str(input())
feedback = str(input())

room_sum = 18 * days
apartment_sum = 25 * days
president_apartment_sum = 35 * days
total_sum = 0
if days < 10:
    apartment_sum *= 0.7
    president_apartment_sum *= 0.9
elif 10 < days < 15:
    apartment_sum *= 0.65
    president_apartment_sum *= 0.85
else:
    apartment_sum *= 0.5
    president_apartment_sum *= 0.8

if type_of_room == "room for one person":
    if feedback == "positive":
        total_sum = room_sum + (room_sum*0.25)
        print(f"{total_sum:.2f}")
    elif feedback == "negative":
        total_sum = room_sum - (room_sum * 0.10)
        print(f"{total_sum:.2f}")
elif type_of_room == "apartment":
    if feedback == "positive":
        total_sum = apartment_sum + (apartment_sum * 0.25)
        print(f"{total_sum:.2f}")
    elif feedback == "negative":
        total_sum = apartment_sum - (apartment_sum * 0.10)
        print(f"{total_sum:.2f}")
elif type_of_room == "president apartment":
    if feedback == "positive":
        total_sum = president_apartment_sum + (president_apartment_sum * 0.25)
        print(f"{total_sum:.2f}")
    elif feedback == "negative":
        total_sum = president_apartment_sum - (president_apartment_sum * 0.10)
        print(f"{total_sum:.2f}")


