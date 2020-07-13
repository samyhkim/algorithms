def to_goat_latin(S):
    words = S.split()

    for i in range(len(words)):
        if words[i][0].lower() in ['a', 'e', 'i', 'o', 'u']:
            words[i] += 'ma' + (i + 1) * "a"
        else:  # consonant
            words[i] = words[i][1:] + words[i][0] + "ma" + (i + 1) * "a"

    return " ".join(words)
