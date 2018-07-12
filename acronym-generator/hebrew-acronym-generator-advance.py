import itertools
import HspellPy
import sys
from datetime import datetime

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

print("[INFO] - Started on: " + str(datetime.now()))

speller = HspellPy.Hspell(linguistics=True)

input_not_grouped = 'כנות צחוק חיבה גומות פיקניק שמש'
words_not_grouped = input_not_grouped.split()
tokens_not_grouped = [word[0].lower() for word in words_not_grouped]

input_grouped = 'לא עוד'
words_grouped = input_grouped.split()
tokens_grouped = [''.join([word[0].lower() for word in words_grouped])]
#tokens_grouped = []

total_tokens = tokens_grouped + tokens_not_grouped;

print("[INFO] - Generating acronyms")

for i in range(2, len(total_tokens) + 1, 1):
    permutations = itertools.permutations(total_tokens, i)
    for permutation in permutations:
        acronymn = ''.join(permutation) # Pay attention in case of hebrew the output in shell might be
                                        #  presented in reverse order
        if (speller.check_word(acronymn)): #acronymn
            print("Found acronym: " + acronymn)

print("[INFO] - Ended on: " + str(datetime.now()))
