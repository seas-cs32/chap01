""" Code for steps 1-3 of active-learning exercise #3 """

my_book = input('What book would you like to read? ')
my_open_book = open('txts/' + my_book)

# Print every line in the book
while True:
    the_line = my_open_book.readline()
    print(the_line, end='')

    # Check for EOF
    if the_line == '':
        break

    my_open_book.close()   # Wrong place to close the file
my_open_book.close()       # Right place to close the file

print("The End.")
