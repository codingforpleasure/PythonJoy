import itertools
import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

dictionaryFile = "wordsEn.txt"

input_not_grouped = 'Self contained underwater breathing apparatus'
words_not_grouped = input_not_grouped.split()
tokens_not_grouped = [word[0].lower() for word in words_not_grouped]

input_grouped = 'animation information relax'
words_grouped = input_grouped.split()
tokens_grouped = [''.join([word[0].lower() for word in words_grouped])]
tokens_grouped=[]

total_tokens_grouped = tokens_grouped + tokens_not_grouped;

print("[INFO] - Loading dictionary")
with open(dictionaryFile) as word_file:
    dictionary = set(word.strip().lower() for word in word_file)

print("[INFO] - Generating acronyms")

for i in range(2, len(total_tokens_grouped) + 1, 1):
    permutations = itertools.permutations(total_tokens_grouped, i)
    for permutation in permutations:
        acronymn = ''.join(permutation)
        if (acronymn in dictionary):
            print("Found acronymn: " + acronymn)
