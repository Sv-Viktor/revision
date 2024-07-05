def generate_pairs_string(n):
    pairs = []
    used_pairs = set()
    for i in range(1, 21):
        j = n - i
        if j > 0 and j <= 20 and j != i:
            pair = tuple(sorted((i, j)))
            if pair not in used_pairs:
                pairs.append(pair)
                used_pairs.add(pair)
    result = ''.join(str(pair[0]) + str(pair[1]) for pair in pairs)
    return result


n = 9
output = generate_pairs_string(n)
print(output)
