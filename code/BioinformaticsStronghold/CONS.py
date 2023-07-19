def parse_fasta(fasta_text):
    sequences = {}
    lines = fasta_text.strip().split('\n')
    current_label = None
    current_sequence = ''
    for line in lines:
        if line.startswith('>'):
            if current_label is not None:
                sequences[current_label] = current_sequence
            current_label = line[1:]
            current_sequence = ''
        else:
            current_sequence += line
    if current_label is not None:
        sequences[current_label] = current_sequence
    return sequences

def generate_profile_matrix(sequences):
    profile_matrix = {'A': [], 'C': [], 'G': [], 'T': []}
    sequence_length = len(sequences[list(sequences.keys())[0]])

    for i in range(sequence_length):
        column = [seq[i] for seq in sequences.values()]
        for nucleotide in profile_matrix:
            profile_matrix[nucleotide].append(column.count(nucleotide))

    return profile_matrix

def generate_consensus_string(profile_matrix):
    consensus_string = ''
    sequence_length = len(profile_matrix['A'])

    for i in range(sequence_length):
        max_count = 0
        consensus_nucleotide = None
        for nucleotide in profile_matrix:
            count = profile_matrix[nucleotide][i]
            if count > max_count:
                max_count = count
                consensus_nucleotide = nucleotide
        consensus_string += consensus_nucleotide

    return consensus_string

if __name__ == "__main__":
    # Example usage
    fasta_input = '''>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT'''

    sequences = parse_fasta(fasta_input)
    profile_matrix = generate_profile_matrix(sequences)
    consensus_string = generate_consensus_string(profile_matrix)

    print("Consensus string:")
    print(consensus_string)
    print("Profile matrix:")
    for nucleotide, counts in profile_matrix.items():
        print(f"{nucleotide}: {' '.join(map(str, counts))}")
