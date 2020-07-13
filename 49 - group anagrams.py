'''
sort each word
if exists in lookup
    add to key's value
else
    add to lookup
return lookup's values
'''


def groupAnagrams(strs):
    anagrams = []
    lookup = {}

    for word in strs:
        sorted_word = tuple(sorted(word))

        if sorted_word not in lookup:
            lookup[sorted_word] = [word]
        else:
            lookup[sorted_word].append(word)

    anagrams = list(lookup.values())
    return anagrams


strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
output = [
    ['ate', 'eat', 'tea'],
    ['nat', 'tan'],
    ['bat']
]

print(groupAnagrams(strs))
