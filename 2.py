list = [1, 2, 3, 4, 5, 6]
size = 3
for index in range(0, len(list) - size):
    for second_index in range(0, size):
        print list[index + second_index]
    print "----"
    print list[index + size]
    print "----"
