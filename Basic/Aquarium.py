length_cm = int(input()) / 10
width_cm = int(input()) / 10
height_cm = int(input()) / 10
percent_of_usage = float(input()) / 100
volume_liters = length_cm * width_cm * height_cm
clear_volume_for_water = (volume_liters - (volume_liters*percent_of_usage))
print(clear_volume_for_water)

