# What is this?

An attempt to extract all words from Wikipedia and match those which can be used as hexwords. Unfortunatly the script isn't that smart so the data isn't that clean. Currently words are sorted by frequency of apperance, then lexographically. Hexwords are defined as the following regex: `(for|o|i|l|s|t|g|a|b|c|d|e|f|0|1|2|3|4|5|6|7|8|9)*`. 


# Usage

Install Git submodules:

    git submodule init && git submodule update

Download the current Wikipedia dumps:

    aria2c --auto-file-renaming=false -x 8 -j 16 https://dumps.wikimedia.org/enwiki/20190801/enwiki-20190801-pages-articles-multistream.xml.bz2

Extract text:
    
    bzcat enwiki-20190801-pages-articles-multistream.xml.bz2 | wikiextractor/WikiExtractor.py --no-templates -o - - > enwiki-20190801-pages-articles.txt

Collect data:
    
    python3 -i hexwords.py 

This should create `words.txt` and `hexwords.txt`. Afterwards it is a simple as `grep -E "^.{8}," hexwords.txt` to list all hexwords of 8 letters or `grep -vE "g" hexwords.txt` to remove the substitution for `g -> 9`/`G -> 6`.