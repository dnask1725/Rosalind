#The DNA molecule is made up of two strands, running in opposite directions.
#Each base bonds to a base in the opposite strand. Adenine always bonds with thymine, and cytosine always bonds with guanine; the complement of a base is the base to which it always bonds;
#The two strands are twisted together into a long spiral staircase structure called a double helix.

#The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
#First reverse the strand then take the complement

dna="TAGTCCAACTTGACATTAATTGGGTATGGGGGGGTCTGATAGTTCAGGTTATAGCGGTAGGGTCGAGGGGGAGTCGAGCTTGATAGAAGGACTGTGAAGAACAGGACGGTTTGGCGAGTACATGAGGGGTGAGTCTAAATACTTAAACGTAAATGCACATATGCTAAGGGAAATTAAAAGGCCCAATATCTCAGGTACTCCCATACGTTTACACTGGCAACAAATCTAGGAAATACGATGTCTCTACGATCATCTCATTAGTCCCATACCTATACCCGTTCCTCGTCGAATGTAAGCCCAACTGGATATGTCTTTGTAGGTCGGTTATGAATCTCTGAGCGAATTTGCGTGCAATCCGTGATAGTTGAACTGTCGGTGAAGTAAATAGGCTGTTGAGTGGCAGGTTAACCAGCCCCAGGCTGGCGATCCCGCATCCCTCGTGTGCCGCCTATTCTCAGAAAGAGATACCGGTGTCAAGAGCGTTGACCCAATAGTTAGAATTTCATTTTGCCACTCTATCCCCGCGTCGCAACTCAGGTTGATAAGGGCGCGTGGCGAGTCAAACCACGATGTGCTACCAGTCACCACTCGGCACAATCGCGAGCCGGTAACTAATCATCAGCGTCGTCGCACGTACGTATATCGCACTGCCAAAACTGAAGTCTGTAGCATTCGAGTTGCGTTTCGCGTAACATAGGGCGTCATTTGTGCATGAGACCACGCGAAGCGGTTTATTTACCTGCTATCCAGCAAAGGCAGTTATGGTGGCAATGCAGCTAACAGACTAATCTCTTTGTCCTATCGACACCAGAATGGTAAACCAAGGTGGGTTGATGCGTTACCGTCGCTGCTGTCTTCATGTACGAAGTCGGAATGGATATATTCTATTCCAGAAAATCCAACAGAAAACCCCAGTCCCCGGATGCTC" #sample

# to reverse
revc=dna[::-1]    

# to complement                              
dna_comp=revc.replace("A","t").replace("G","c").replace("C","g").replace("T","a")
print(dna_comp.upper())
