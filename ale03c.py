""" Code for last part of active-learning exercise #3 """

my_book = input('What book would you like to read? ')

with open('txts/' + my_book) as my_open_book:
    while True:
        the_line = my_open_book.readline()
        print(the_line, end='')

        # Check for EOF
        if the_line == '':
            break

print("The End.")
