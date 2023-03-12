chicken_menu_count = int(input())
fish_menu_count = int(input())
vegi_menu_count = int(input())
price_chicken_menu = chicken_menu_count * 10.35
price_fish_menu = fish_menu_count * 12.40
price_vegi_menu = vegi_menu_count * 8.15
food_price = price_vegi_menu + price_chicken_menu + price_fish_menu
total_price = food_price + (food_price*0.2) + 2.50
print(total_price)