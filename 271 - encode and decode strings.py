# class Codec:
#     def encode(self, strs):
#         ''' Encodes a list of strings into a single string. '''
#         long_string = ""
#         strs = ['Hello', 'World']
#         for i in range(len(strs)-1):
#             long_string += strs[i] + "."
#         long_string += strs[-1]
#         return long_string

#     def decode(self, s):
#         ''' Decodes a single string into a list of strings. '''
#         s = list(map(str, s.split(".")))
#         return s


class Codec:

    def encode(self, strs):
        return ''.join('%d:' % len(s) + s for s in strs)

    def decode(self, s):
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j+1:i])
        return strs


codec = Codec()
codec.decode(codec.encode(['Hello', 'World']))
