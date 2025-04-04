from Hamming.hamming import hamming_distance
# Arrange
# Act
# Assert
# test 1
def test_if_the_length_of_strands_are_the_same():
    # Arrange
    strand1 = "ATCG"
    strand2 = "ATCG"
    # Act
    result = hamming_distance(strand1, strand2)
    # Assert
    assert len(strand1) == len(strand2)

#test2
def test_count_of_different_strands():
     # Arrange
    strand1 = "ATGC"
    strand2 = "GTAC"
    # Act
    result = hamming_distance(strand1, strand2)
    
    # Assert
    assert result == 2
    
# test3
def test_if_the_string_contain_other_than_letters_valid_dna():
    # Arrange
    strand1 = "ATGC"
    strand2 = "ADBT"
    # Act
    result = hamming_distance(strand1, strand2)
    
    # Assert
    assert result == 0
    

# test 4  
def test_check_if_the_letter_is_upper_case():
    # Arrange
    strand1 = "aTCG"
    strand2 = "Atag"
    # Act
    result = hamming_distance(strand1, strand2)
    # Assert
    assert result == 1

#test 5
def test_checks_if_there_other_type_of_input_not_string():
    # Arrange
    strand1 = "ATCG"
    strand2 = 9
    # Act
    result = hamming_distance(strand1, strand2)
    # Assert
    assert result == 0
# test 6
def test_if_both_strands_are_not_empty():
    # Arrange
    strand1 = "ATCG"
    strand2 = ""
    # Act
    result = hamming_distance(strand1, strand2)
    # Assert
    assert result == 0
# test 7
