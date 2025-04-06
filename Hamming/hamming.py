# # 
# Example Input	Expected Ouput
# strand1 = "GAGCCTACTAACGGGAT"
# strand2 = "CATCGTAATGACGGCCT"	7

def hamming_distance(strand1, strand2):
    if not isinstance(strand1, str) or not isinstance(strand2, str):
        return 0
    
    if len(strand1) != len(strand2):
        return 0
    
    strand1 = strand1.upper()
    strand2 = strand2.upper()
    
    total_of_diff = 0
    
    valid_dna_letters = ['A', 'T', 'G', 'C']
    for i in range(0, len(strand1)):
        
        if strand1[i] not in valid_dna_letters:
            raise ValueError (f"'{strand1[i]}' is not allowed in DNA")
        if strand2[i] not in valid_dna_letters:
            raise ValueError (f"'{strand2[i]}' is not allowed in DNA")
        
        if strand1[i] != strand2[i]:
            total_of_diff += 1
    return total_of_diff   


print(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))
# print(hamming_distance("gAGCCTACTAACGGGAT","cATCGTAATGACGGCCT"))
# print(hamming_distance("GAGCCTACTAACGGGAT","IATCGTAATGACGGCCT"))
# print(hamming_distance(9,"CATCGTAATGACGGCCT"))