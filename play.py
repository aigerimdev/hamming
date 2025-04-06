
"""Option 1: 
Use a for loop with index
Loop through from 0 to length of the string
Compare letter at position i in both strands
"""

# def hamming_distance(strand1, strand2):
#     total = 0
#     for i in range(0, len(strand1)):
#         if strand1[i] != strand2[i]:
#             total += 1
#     return total
# print(hamming_distance("GAGCCTACTAACGGGAT","CATCGTAATGACGGCCT"))

"""
Option 2: 
Use a for-each loop with zip
Pair letters from both strings together
Compare each pair
"""

# def hamming_distance(strand1, strand2):
#     total = 0
#     for char1, char2 in zip(strand1, strand2):
#         if char1 != char2:
#             total += 1
#     return total
# print(hamming_distance("GAGCCTACTAACGGGAT","CATCGTAATGACGGCCT"))


# ls1 = ['apple', 'banana', 'cherry', 'bean']
# ls2 = ['banana', 'apple', 'cherry', 'bean']


# def hamming_distance(ls1, ls2):
#     different = []
#     for i in range (0, len(ls1)):
#         if ls1[i] != ls2[i]:
#             different.append(i)
#     return different
# print(hamming_distance(['apple', 'banana', 'cherry', 'bean'], ['banana', 'apple', 'cherry', 'banana']))