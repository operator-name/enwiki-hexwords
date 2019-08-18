with import <nixpkgs> {};

let
    enwiki-dl = pkgs.writeShellScriptBin "enwiki-dl" ''
        ${pkgs.wget}/bin/wget -np -r --accept-regex 'https://dumps.wikimedia.org/enwiki/20190801/enwiki-20190801-pages-articles-multistream[1-27].*' https://dumps.wikimedia.org/enwiki/20190801/
    '';
in stdenv.mkDerivation rec {
    name = "enwiki-hexwords";

    buildInputs = [ python enwiki-dl ];
}