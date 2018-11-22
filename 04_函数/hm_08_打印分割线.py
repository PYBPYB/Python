def print_line(char, times):

    print(char * times)

def print_lines(char, times):


    row = 0

    while row <= times:

        print_line(char, row)

        row += 1

print_lines("*", 6)

