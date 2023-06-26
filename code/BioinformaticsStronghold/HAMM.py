#The simplest and most common type of nucleic acid mutation is a point mutation, which replaces one base with another at a single nucleotide. In the case of DNA, a point mutation must change the complementary base accordingly
#Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t


def hamming_distance(s, t):
    if len(s) != len(t):
        raise ValueError("Input strings must have equal length.")
    
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    
    return count

s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

distance = hamming_distance(s, t)
print("Hamming distance:", distance)
