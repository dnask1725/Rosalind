def hamming_distance(s1, s2):
    """
    Calculates the Hamming distance between two strings.
    """
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def correct_reads(reads):
    """
    Finds corrections for reads with single-nucleotide errors.
    """
    correct_set = set()
    corrections = []

    # Find correct reads
    for read in reads:
        if read in correct_set or read[::-1] in correct_set:
            correct_set.add(read)
        else:
            for correct_read in correct_set:
                if hamming_distance(read, correct_read) == 1:
                    corrections.append(f"{correct_read}->{read}")
                    break
            else:
                correct_set.add(read)

    return corrections

# Sample dataset
dataset = {
    'Rosalind_52': 'TCATC',
    'Rosalind_44': 'TTCAT',
    'Rosalind_68': 'TCATC',
    'Rosalind_28': 'TGAAA',
    'Rosalind_95': 'GAGGA',
    'Rosalind_66': 'TTTCA',
    'Rosalind_33': 'ATCAA',
    'Rosalind_21': 'TTGAT',
    'Rosalind_18': 'TTTCC'
}

reads = list(dataset.values())
corrections = correct_reads(reads)
# Output corrections
for correction in corrections:
    print(correction)
