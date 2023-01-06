""" Code for first parts of active-learning exercise #3 """

my_book = input('What book would you like to read? ')
my_open_book = open('txts/' + my_book)

while True:
    the_line = my_open_book.readline()
    print(the_line, end='')
    if the_line == '':
        # We've read the entire book!
        print("\nThe End.")
        break

    my_open_book.close()   # Wrong place to close the file
my_open_book.close()       # Right place to close the file
