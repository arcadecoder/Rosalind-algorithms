'''
Script that checks the Hamming distance
between two DNA strings - the number of difference
bases in the two strings.
'''

# The expected answer should  be 7
test_string1 = "GAGCCTACTAACGGGAT"
test_string2 = "CATCGTAATGACGGCCT"


def hamming_distance(s1, s2):
    # TO DO: pair each letter of the strings using zip
    # TO DO: create dictionary of the zip & empty list object
    string_tuple = list(zip(s1, s2))
    zipped_list = string_tuple[:]
    string_dictionary = dict(zipped_list)
    char_count = []
    # For loop to check if key value pairs match & count
    for entry in zipped_list:
        if entry[0] == entry[1]:
            char_count.append('*')
        else:
            char_count.append("mismatch")
    # Count the number of times * apppears in the list
    count = ''.join(char_count).count('*')

    print(char_count)
    print(count)
    print(char_count.count("mismatch"))
    return


hamming_distance(test_string1, test_string2)
