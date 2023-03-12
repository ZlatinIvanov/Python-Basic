first_seconds = int(input())
second_seconds = int(input())
third_seconds = int(input())
sum_seconds = first_seconds + second_seconds + third_seconds
minutes_convert = sum_seconds // 60
seconds_leftovers = sum_seconds % 60
if seconds_leftovers % 60 >= 10:
    print(f"{minutes_convert}:{seconds_leftovers}")
if seconds_leftovers % 60 < 10:
    print(f"{minutes_convert}:0{seconds_leftovers}")