#!/usr/bin/env python3
from collections import defaultdict
import re
import subprocess
import sys

line_trans = str.maketrans("–’", "-'")
words_split_re = re.compile(r"[^\w\-\"]")
is_word_re = re.compile(r"^\w.*\w$")
number = re.compile("[0-9\-]*")

words = set()

with open("enwiki-20190801-pages-articles.txt") as txt:
    for i, line in enumerate(txt):
        if line.startswith("<"): # wikiextractor puts files in xml tags
                print(f"(processed lines, processed words) = ({i}, {len(words)})", file=sys.stderr)
                continue
        for word in filter(None, words_split_re.split(line.translate(line_trans).lower())):
            if is_word_re.match(word) and not number.fullmatch(word):
                words.add(word)
                
print(f"(processed lines, processed words) = ({i}, {len(words)})", file=sys.stderr)

# write in case something goes wrong
with open("words1.txt", "wt") as words_txt:
    for i, word in enumerate(sorted(words)):
        if (i % 10000 == 0):
            print(f"(written lines, word) = ({i}, {word})", file=sys.stderr)
        words_txt.write("%s\n" % word)

subs = [
    ("ate", "8"),
    ("for", "4"),
    
    ("o", "0"),
    ("i", "1"),
    ("l", "1"),
    ("s", "5"),
    ("t", "7"),
    ("g", "9"), # or 6 for capital
]

hex_word = re.compile("[a-f0-9]*")

hexwords = set()

# create hexwords list
with open("hexwords1.txt", "wt") as hexwords_txt:
    for word in sorted(words):
        w = word
        for old, new in subs:
            w = str.replace(w, old, new)
        if hex_word.fullmatch(w):
            hexwords.add(word)
            print(f"(found hexwords, hexword) = ({len(hexwords)}, {word})", file=sys.stderr)
            hexwords_txt.write(f"{word}\n")