packs_pens = float(input())
packs_markers = float(input())
board_liquid_liters = float(input())
discount = float(input()) / 100
total_price_pens = packs_pens * 5.80
total_price_markers = packs_markers * 7.20
total_price_board_liquid = board_liquid_liters * 1.20
amount = total_price_board_liquid + total_price_markers + total_price_pens
total_amount = amount - (amount*discount)
print(total_amount)

