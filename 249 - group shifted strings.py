'''
Map each string in strings to a key in a hashmap. We then return hashmap.values():
{
     (1, 1): ['abc', 'bcd', 'xyz'],  
  (2, 2, 1): ['acef'],   
      (25,): ['az', 'ba'],   
         (): ['a', 'z']
}

The key can be represented as a tuple of the differences between adjacent characters.
Characters map to integers - ord('a') = 97; 'abc' maps to (1, 1)

We need to watch for the "wraparound" case - 'az' and 'ba' should map to the same
"shift group" as a + 1 = b and z + 1 = a.
The respective tuples should be (25) (122 - 97) and (-1) (79 - 80) and 'az' and 'ba'
would map to different groups. This is incorrect.

To account for this case, we add 26 to the difference between letters (smallest
difference possible is -25, 'za') and mod by 26. So, (26 + 122 - 97) % 26 and
(26 + 79 - 80) % 26 both equal 25.

Time: O(ab), a is the number of strings and b is the length of the longest string
Space: O(n)
'''


def group_strings(strings):
    lookup = {}

    for string in strings:
        key = ()
        for i in range(len(string) - 1):
            # get difference of char in front and current char
            circular_difference = 26 + ord(string[i + 1]) - ord(string[i])
            key += (circular_difference % 26,)

        lookup[key] = lookup.get(key, []) + [string]

    return list(lookup.values())


strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print(group_strings(strings))
