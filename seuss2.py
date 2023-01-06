my_book = input('What book would you like to read? ')
my_open_book = open(my_book)
while True:
    the_line = my_open_book.readline()
    print(the_line, end='')
    if the_line == '':
        print("The End.")
        break
