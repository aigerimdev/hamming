# # 
# Example Input	Expected Ouput
# strand1 = "GAGCCTACTAACGGGAT"
# strand2 = "CATCGTAATGACGGCCT"	7

def hamming_distance(strand1, strand2):
    if not isinstance(strand1, str) or not isinstance(strand2, str):
        return 0
    
    if len(strand1) != len(strand2):
        raise ValueError("Strands must be the same length")
    
    strand1 = strand1.upper()
    strand2 = strand2.upper()
    
    valid_dna = {'A', 'T', 'G', 'C'} # faster lookup than list
    diff_count = 0
    
    
    for i in range(0, len(strand1)):
        
        if strand1[i] not in valid_dna:
            raise ValueError (f"'{strand1[i]}' is not allowed in DNA")
        if strand2[i] not in valid_dna:
            raise ValueError (f"'{strand2[i]}' is not allowed in DNA")
        
        if strand1[i] != strand2[i]:
            diff_count += 1
            
    return diff_count 


print(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))
# print(hamming_distance("gAGCCTACTAACGGGAT","cATCGTAATGACGGCCT"))
# print(hamming_distance("GAGCCTACTAACGGGAT","IATCGTAATGACGGCCT"))
# print(hamming_distance(9,"CATCGTAATGACGGCCT"))