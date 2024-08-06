### chap01/ale05a.py
my_book = input('What book would you like to read? ')
my_open_book = open(my_book)

# Read the first line in the book, if it exists
the_line = my_open_book.readline()

# Loop printing every line in the book
while the_line != '':
    # REPLACE ME with the correct loop body

print("The End.")
