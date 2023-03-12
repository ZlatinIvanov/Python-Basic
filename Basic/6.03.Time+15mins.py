hours = int(input())
minutes = int(input())
total_minutes = minutes + 15
final_minutes = 0
total_hours = hours
final_hours = 0
if total_minutes >= 60:
    total_hours = hours + 1
    final_minutes = total_minutes - 60
else:
    total_hours = hours
    final_minutes = total_minutes

if total_hours >= 24:
    total_hours = 0
else:
    total_hours = total_hours

if final_minutes < 10:
    print(f"{total_hours}:0{final_minutes}")
else:
    print(f"{total_hours}:{final_minutes}")
