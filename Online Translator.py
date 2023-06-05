#Online Translator
#مترجم آنلاین

from collections import OrderedDict

n = int(input())
dictionary = OrderedDict()

for i in range(n):
    word1, word2 = input().split()
    dictionary[word1] = word2

sentence = input().split()
result = []

for word in sentence:
    result.append(dictionary.get(word, word))

print(" ".join(result))