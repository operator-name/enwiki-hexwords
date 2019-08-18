with import <nixpkgs> {};

stdenv.mkDerivation rec {
    name = "enwiki-hexwords";

    buildInputs = [ python3 aria2 ];
}