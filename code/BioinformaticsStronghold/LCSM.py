def longest_common_substring(strings):
    def find_common_substring(s1, s2):
        max_len = 0
        end_index = 0
        for i in range(len(s1)):
            for j in range(len(s2)):
                length = 0
                while i + length < len(s1) and j + length < len(s2) and s1[i + length] == s2[j + length]:
                    length += 1
                if length > max_len:
                    max_len = length
                    end_index = i + length
        return s1[end_index - max_len:end_index]

    longest_substring = strings[0]
    for i in range(1, len(strings)):
        longest_substring = find_common_substring(longest_substring, strings[i])

    return longest_substring


if __name__ == "__main__":
    fasta_data = '''>Rosalind_1
    GATTACA
    >Rosalind_2
    TAGACCA
    >Rosalind_3
    ATACA'''

    sequences = []
    for line in fasta_data.split('\n'):
        line = line.strip()
        if line.startswith('>'):
            sequences.append("")
        else:
            sequences[-1] += line

    result = longest_common_substring(sequences)
    print(result)
