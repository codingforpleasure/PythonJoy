from __future__ import unicode_literals
import HspellPy # Python wrapper for Hspell
import itertools
import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

speller = HspellPy.Hspell(linguistics=True)

input = 'כנות צחוק חיבה גומות פיקניק שמש'
words = input.split()
tokens = [word[0].lower() for word in words]

print("[INFO] - Generating acronyms")

for i in range(1, len(tokens) + 1, 1):
    permutations = itertools.permutations(tokens, i)
    for permutation in permutations:
        acronymn = ''.join(permutation) # Pay attention in case of hebrew the output in shell might be
                                        #  presented in reverse order
        if (speller.check_word(acronymn)): #acronymn
            print("Found aronymn: " + acronymn)
