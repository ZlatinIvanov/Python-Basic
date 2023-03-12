pages_in_book = int(input())
pages_per_hour = int(input())
days_to_read_the_book = int(input())
time_to_read = pages_in_book / pages_per_hour
needed_time = time_to_read / days_to_read_the_book
print(int(needed_time))
