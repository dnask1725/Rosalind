import itertools


def kmer_composition(dna_string, k=4):
    """
    Returns the k-mer composition of the given DNA string.
    """
    kmer_counts = {}
    alphabet = ['A', 'C', 'G', 'T']

    # Initialize counts for all possible 4-mers to 0
    for kmer in itertools.product(alphabet, repeat=k):
        kmer_counts[''.join(kmer)] = 0

    # Count occurrences of each 4-mer in the DNA string
    for i in range(len(dna_string) - k + 1):
        kmer = dna_string[i:i + k]
        kmer_counts[kmer] += 1

    return kmer_counts


# Sample dataset
dna_string = ("CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG"
              "CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT"
              "TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA"
              "AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG"
              "GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA"
              "CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA"
              "CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG")

# Get k-mer composition
composition = kmer_composition(dna_string)

# Output the counts in lexicographic order
alphabet = ['A', 'C', 'G', 'T']
for kmer in itertools.product(alphabet, repeat=4):
    kmer_str = ''.join(kmer)
    print(composition[kmer_str], end=' ')
