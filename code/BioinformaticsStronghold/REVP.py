#PROBLEM
#A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.
#Given: A DNA string of length at most 1 kbp in FASTA format.
#Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.



def parse_fasta(fasta_string):
    lines = fasta_string.strip().split("\n")[1:]
    dna_sequence = "".join(lines)
    return dna_sequence

def reverse_complement(dna_sequence):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement[base] for base in reversed(dna_sequence))

def find_reverse_palindromes(dna_sequence):
    result = []
    n = len(dna_sequence)
    for i in range(n):
        for j in range(i + 4, min(i + 13, n + 1)):  # Length between 4 and 12.
            substr = dna_sequence[i:j]
            reverse_comp = reverse_complement(substr)
            if substr == reverse_comp:
                result.append((i + 1, j - i))  # Positions are 1-based.
    return result

# Test input
fasta_input = """>Rosalind_8894
TATAGGAATGAGCCTAGCCGGCCGCACCCTCAATCGCACCTCCTTTGATTGGCTTTCCAA
GGTAGGTAACAGGATTGCTCACAGAAGCATAGTCCAGTCCGTACTCGCCCATTCGGTAGT
AAGCAACGCATCGGTCGCGTATGATTATCGAACCCGCTACGTCTTACAGATATGGAGCTT
TCCCCGAGAGCGCTCGTCTTTCTCGCGTAGAGCGCGTTTGCTGTTTATGTGTCCTGGTCA
GCTGTCGTACTTTGCCCCACCTCCCGCAGTACTATGGACGACATACCTCCATACTATTAG
GCCAAACTGTTCTAGTGGTTCGCATATAAACACGAACAGTTTAGAACAGTCGATCGGAGT
GTTGTTGGCTTCGGCGGTGGTTAAGTTATTGTGGAATTTCTCTAACCCCTCCCAGCGCAC
TTGGTCGTACGACCTGATCCGCACCGTGGCGTCAAAATTCTCGTCCTTTGAGCCCTTCGG
GGCCGTGGGCCTTCGACTCCAGGGAATGGGCCGCGCACGTCTAACCGTCGTGTCGAAAAT
GGGGAAGAGCGAAGAGGTAACTGGCCCCGGAATAAGAAATATCGTGAATCTCTGCCCTCC
TGCGGTATTGGTAAGAGAATAAAATTGGGCAGACCAAAGATGATATCTCACACTAACGGC
TAGCTGAGAAACTCCAAGCTGTCTCGATTTGATACGATAACGTTCTATCCCGTCCCCGAG
GTTTCGAGCACAAAATTGGTGGCCCTACGTGGTATCATCGGGACCTGTTCCTTATGAATA
CCAGTGTCGTAAGCGCATACTCCGACTGAGAACCTACTCCCGACCCGAAGCCAATAGCTG
TCTGGACAACGTTATA
"""

# Parse the FASTA input
dna_string = parse_fasta(fasta_input)

# Find reverse palindromes
reverse_palindromes = find_reverse_palindromes(dna_string)

# Print the results
for pos, length in reverse_palindromes:
    print(f"{pos} {length}")
