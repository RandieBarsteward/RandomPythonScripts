
from collections import Counter

Vowel= ['a', 'e', 'i', 'o', 'u']
#text = "oihavrpouhvaravprhebpoiuFNPyefblkHLPHVHphapghpnaeiouaeiouaeiouaohwebrveeeee"
text = input("Input text here:")
vowellist = []

print(text)
print(Vowel)

cl = Counter(text)
print(cl)

for i in text:
    if i in Vowel:
        vowellist.append(i)

print(Counter(vowellist))




                               