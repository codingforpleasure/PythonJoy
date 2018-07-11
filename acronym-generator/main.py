import itertools
import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

dictionaryFile = "wordsEn.txt"

input = 'Self contained underwater breathing apparatus'
words = input.split()
tokens = [word[0].lower() for word in words]

print("[INFO] - Loading dictionary")
with open(dictionaryFile) as word_file:
    dictionary = set(word.strip().lower() for word in word_file)

print("[INFO] - Generating acronyms")

for i in range(2, len(tokens) + 1, 1):
    permutations = itertools.permutations(tokens, i)
    for permutation in permutations:
        acronymn = ''.join(permutation)
        if (acronymn in dictionary):
            print("Found acronymn: " + acronymn)
