def is_alien_sorted(words, order):
    lookup = {char: idx for idx, char in enumerate(order)}
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i + 1]
        # "apple", "app"
        if len(word1) > len(word2) and word1[:len(word2)] == word2:
            return False
        for j in range(len(word1)):
            if lookup[word1[j]] < lookup[word2[j]]:  # if equal, should keep checking
                break
            elif lookup[word1[j]] > lookup[word2[j]]:
                return False
    return True


print(is_alien_sorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
