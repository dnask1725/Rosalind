# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
#Link : https://rosalind.info/problems/dna/


s="AGGTTGTTCTTTTCTGCACCATTCCCACCAGACCTCCATTTTTGGACATGTAATAGGA"  #sample
T=s.count("T")
G=s.count("G")
C=s.count("C")
print(A,T,G,C) 

# OR

s="AGGTTGTTCTTTTCTGCACCATTCCCACCAGACCTCCATTTTTGGACATGTAATAGGA" #sample

print(s.count("A"), s.count("C"),s.count("G"),s.count("T"))
