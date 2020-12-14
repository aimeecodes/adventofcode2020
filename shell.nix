with import <nixpkgs> {};
stdenv.mkDerivation {
  name = "python-environment";
  buildInputs = with python38Packages;
    [
    pandas
    scikitlearn
    numpy
    matplotlib
    ]; 

  # Put stuff to auto-run here
#   shellHook = ''
#   '';
}
