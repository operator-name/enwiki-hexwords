# Usage

Install Git submodules:

    git submodule init && git submodule update

Download the current Wikipedia dumps:

    aria2c --auto-file-renaming=false -x 8 -j 16 https://dumps.wikimedia.org/enwiki/20190801/enwiki-20190801-pages-articles-multistream.xml.bz2

Extract text:
    
    bzcat enwiki-20190801-pages-articles-multistream.xml.bz2 | wikiextractor/WikiExtractor.py --no-templates -o - - > enwiki-20190801-pages-articles.txt

Collect data:
    
    python3 -i hexwords.py 
