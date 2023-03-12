plastic_sheets_in_sq_m = int(input()) + 2
paint_liters = int(input())
thinner_liters = int(input())
hours_to_finish_painting = int(input())
additional_paint = paint_liters + (paint_liters*0.1)
bags = 0.40
price_paint = additional_paint * 14.50
price_thinner = thinner_liters * 5.00
price_plastic_sheets = plastic_sheets_in_sq_m * 1.50
material_price = price_plastic_sheets + price_paint + bags + price_thinner
work_price_per_hour = material_price * 0.3
total_price = material_price + (work_price_per_hour*hours_to_finish_painting)
print(total_price)



