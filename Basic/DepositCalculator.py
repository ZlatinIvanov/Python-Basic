deposit = float(input())
deposit_months = int(input())
annual_percentage = float(input()) / 100
total_amount = deposit + deposit_months*(deposit*annual_percentage/12)
print(total_amount)
