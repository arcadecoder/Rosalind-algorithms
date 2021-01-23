"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

sample_dataset = "AAAACCCGGT"
sample_output_compare = "ACCGGGTTTT"
question_dataset = """CGGCCCCAGCGGCTATAATTTATTCGGGCAGTATATAGCCACCAATACGAGCACACTTGAGGCATCGGTGGTGTAAGTACGGGATTTGGGAGGTGAACTGAAAACCCAGCCGAATAGAGGGTTTTAACTAATGCGTTATGGATACAATACTCCCGGTAGTGCTACTTCGTCTAATTTACCGCAACCGGCGCTCATCTACCTCTGTGCCCTACACCGTTAACTTTAACTTCTCTAGCACTTTGTGGGACCCGATACCTAGTTACGGTCATTCGTCTTTCATCTTACTCAGATGTAAATAGCTTCTAGTTACTTGTCGCATACGGCACCAAGCACAAGGAGACTTGTTCGTATACGTAGATTTAAATGTTATATACACGTTAGTCTAACAAAAGATCATGAAAGTGATTCGCAAACACAGCCCTAATGACCGACCCGCTGCTCATTCCACGAACAACAGGATCGGAACGCAGTCGTTGACCGATATATAACGTCGTCTCCACCATTCAACGAGACCCTGGCTAATTGGTTGCGGTGTACGGGAGGTTGCGTATTAGTACAAGGCGAGTTCCAATCGCTGGGCTGTGCTGAAGGCGTCCATTCAGTTACCCTGACTCTACTGAATGGGTTGGCCGCGAATCGACGAACGCTAAGGCTTTTCGGAAGTTCAGCGCACAGCGCCCAGTAGGATTCCAGCCTACAGTTGTGACTGCAATTGGTGTTGGCAGCTATGACTGAAGCGATGGCTGGGATCATTTTCTGGGCGACCACGACGTCGGGTACGCGTTCATCAACCAATTTTTTTCTCGTAATGCCCGACTCGGGTGGGGCACTTTCAGGACGGCGGATAGTGCATGTGGATTCTCCGACAGATGACAATACCGCTGCTTGTCCCCCCTTTCGCTTCCCCTTTGGGCGGTTG
"""


def return_complementary_strand(string):
    reverse = string[::-1]
    # print(reverse)
    complement = reverse.translate(str.maketrans(
        {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}))
    print(complement)
    return reverse


return_complementary_strand(question_dataset)
