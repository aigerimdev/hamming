# # 
# Example Input	Expected Ouput
# strand1 = "GAGCCTACTAACGGGAT"
# strand2 = "CATCGTAATGACGGCCT"	7

def hamming_distance(strand1, strand2):
    if len(strand1) != len(strand2):
        return 0
    total_of_diff = 0
    
    for char1, char2 in zip(strand1, strand2):
        if char1 != char2:
            total_of_diff += 1
    return total_of_diff
    
    
    
# print(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))
print(hamming_distance("GAGCCTACTAACGGGAT","CATCGTAATGACGGCCT"))