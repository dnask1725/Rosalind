def overlap(a, b):
    """
    Returns the length of the longest overlap between two strings.
    """
    start = 0
    while True:
        start = a.find(b[:start + len(a) // 2], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1

def shortest_superstring(strings):
    """
    Returns the shortest superstring containing all the given strings.
    """
    while len(strings) > 1:
        max_overlap = float('-inf')
        pair_to_merge = None

        for i in range(len(strings)):
            for j in range(len(strings)):
                if i != j:
                    overlap_len = overlap(strings[i], strings[j])
                    if overlap_len > max_overlap:
                        max_overlap = overlap_len
                        pair_to_merge = (i, j)

        i, j = pair_to_merge
        strings[i] += strings[j][max_overlap:]
        strings.pop(j)

    return strings[0]

# Sample dataset
dataset = {
    'Rosalind_56': 'ATTAGACCTG',
    'Rosalind_57': 'CCTGCCGGAA',
    'Rosalind_58': 'AGACCTGCCG',
    'Rosalind_59': 'GCCGGAATAC'
}
strings = list(dataset.values())
result = shortest_superstring(strings)
print(result)
