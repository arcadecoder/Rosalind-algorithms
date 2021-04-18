# The base of the rabbits algorithim is fibonnaci-sequence
#  To do this using a generator
def fibonnaci_loop(number):
    new = 1
    old = 1
    fib_list = []
    for itr in range(number - 1):
        temp = new
        new = old
        old = old + temp
        fib_list.append(new)
    print(fib_list)
    return new


fibonnaci_loop(12)


 string_tuple = zip(string1, string2)
    string_dictionary = dict(string_tuple)
    print(string_dictionary)