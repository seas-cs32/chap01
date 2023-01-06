my_open_book = open('CatInTheHat.txt')
while True:
    the_line = my_open_book.readline()
    print(the_line, end='')
    if the_line == '':
        print("The End.")
        break
