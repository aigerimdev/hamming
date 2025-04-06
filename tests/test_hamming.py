import pytest
from Hamming.hamming import hamming_distance

# test 1
def test_if_the_length_of_strands_are_the_same():
    # Arrange
    strand1 = "ATCG"
    strand2 = "ATCGG"
    # Act
    with pytest.raises(ValueError) as error:
        hamming_distance(strand1, strand2)
    # Assert
    assert str(error.value) == "Strands must be the same length"

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
def test_invalid_dna_letter_in_strand1():
    strand1 = "ATBC"  # 'B' is invalid
    strand2 = "ATGC"

    with pytest.raises(ValueError) as error:
        hamming_distance(strand1, strand2)

    assert str(error.value) == "'B' is not allowed in DNA"  

# test 4  
def test_check_if_the_letter_is_upper_case():
    # Arrange
    strand1 = "aTCG"
    strand2 = "Atag"
    # Act
    result = hamming_distance(strand1, strand2)
    # Assert
    assert result == 1

# test 5
def test_checks_if_there_other_type_of_input_not_string():
    # Arrange
    strand1 = "ATCG"
    strand2 = 9
    # Act
    result = hamming_distance(strand1, strand2)
    # Assert
    assert result == 0

# test 6
def test_return_count_of_different_from_two_strands():
     # Arrange
    strand1 = "ATCG"
    strand2 = "ATCT"
    # Act
    result = hamming_distance(strand1, strand2)
    # Assert
    assert result == 1