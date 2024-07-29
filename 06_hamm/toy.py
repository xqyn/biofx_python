def hamming(seq1, seq2: str) -> int:
    args = get_args()
    seq1, seq2 = args.seq1, args.seq2

    l1, l2 = len(seq1), len(seq1)
    distance = abs(l1 - l2)
    
    for i in range(min(l1, l2)):
        if seq1[i] != seq2[i]:
            distance += 1
        print(distance)

l1, l2 = len(seq1), len(seq2)
print(seq1, seq2)
distance = abs(l1 - l2)

for i in range(min(l1, l2)):
    if seq1[i] != seq2[i]:
        distance += 1

print(distance)