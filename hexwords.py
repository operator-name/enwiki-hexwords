#!/usr/bin/env python3
from collections import defaultdict
import re
import subprocess
import sys

line_trans = str.maketrans("–’", "-'")
words_split_re = re.compile(r"[^\w\-\"]")
is_word_re = re.compile(r"^\w.*\w$")
number = re.compile("[0-9\-]*")

words = defaultdict(int)

with open("enwiki-20190801-pages-articles.txt") as txt:
    for i, line in enumerate(txt):
        if (i % 10000 == 0): # wikiextractor puts files in xml tags
                print(f"(processed lines, processed words) = ({i}, {len(words)})", file=sys.stderr)
                continue
        for word in filter(None, words_split_re.split(line.translate(line_trans).lower())):
            if is_word_re.match(word) and not number.fullmatch(word):
                words[word] += 1
                
print(f"(processed lines, processed words) = ({i}, {len(words)})", file=sys.stderr)

words_by_freq = sorted(words.items(), key=lambda t: (-t[1], t[0]))

# write in case something goes wrong
with open("words.txt", "wt") as words_txt:
    for i, word_freq in enumerate(words_by_freq): # print by frequency
        if (i % 10000 == 0):
            print(f"(written words, word_freq) = ({i}, {word_freq})", file=sys.stderr)
        words_txt.write(f"{word_freq[0]}, {word_freq[1]}\n")

hex_word = re.compile("(for|o|i|l|s|t|g|a|b|c|d|e|f|0|1|2|3|4|5|6|7|8|9)*")
hexwords = defaultdict(int)

# create hexwords list
with open("hexwords.txt", "wt") as hexwords_txt:
    for i, word_freq in enumerate(words_by_freq):
        if hex_word.fullmatch(word_freq[0]):
            hexwords[word_freq[0]] = word_freq[1]
            print(f"(written hexwords, hexword_freq) = ({i}, {word_freq})", file=sys.stderr)
            hexwords_txt.write(f"{word_freq[0]}, {word_freq[1]}\n")