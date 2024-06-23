my_open_book = open('CatInTheHat.txt')

# Print every line in the book
while True:
    the_line = my_open_book.readline()
    print(the_line, end='')

    # Check for EOF
    if the_line == '':
        break

print("The End.")
