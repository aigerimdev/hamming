Hamming ( checking how different two things are, letter by letter)
Problem Statment
Imagine working on software that analyzes mutations in DNA.

Create a function named hamming_distance that calculates the number of differences between two DNA strands (aka two strings). This method should take in two different DNA strands of the same length as parameters. This method should have a return value of the number of differences between each string.

For example, given these two DNA strands (strings), hamming_distance should return 7 because there are 7 differences:

Example Input	Expected Ouput
strand1 = "GAGCCTACTAACGGGAT"
strand2 = "CATCGTAATGACGGCCT"	7
Explanation:

Strand #1:   GAGCCTACTAACGGGAT
Strand #2:   CATCGTAATGACGGCCT
Differences: ^ ^ ^  ^ ^    ^^

Clarifying Questions and Expected Behavior
1. What if the lengths of the strands are not the same?
→ raise an error. 
2. What if the strings contain non-alphabetical characters? 
→ Only valid DNA letters (A, T, C, G) should be allowed.


→ No, convert both to uppercase before comparing.
4. What if one or both strands are empty? 
→ Return 0, since there's nothing to compare.
5. Can we use lowercase letters like "a", "t", etc.? 
→ Yes, but convert to uppercase before comparison.
6. Should we validate that the strands contain only DNA letters (A, T, C, G)?
→ Yes, raise an error 
7. What if input is not a string (like numbers or None)?
→ Return 0 or raise an error. 


1. What if the lengths of the strands are not the same?
2. What if the strings contain non-alphabetical characters?
3. Is it case sensitive? 
4. Should we validate that the strands contain only DNA letters (A, T, C, G)?
5. What if input is not a string (like numbers or None)?