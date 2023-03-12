letters = ["a","e","i","o","u","y","A","E","I","O","U","Y"]
word = input()
strongest_word = 0
counter = 0
counter_letters = 0
while word != "End of words":
   # new_word = word
    for i in word:
        i = ord(i)
        counter = counter + i
        counter_letters += 1
    if word[0] == "a":
        counter = counter * counter_letters
    else:
        counter = int(counter/counter_letters)
    if counter > strongest_word:
        strongest_word = counter
        counter = 0
    word = input()
print(strongest_word)