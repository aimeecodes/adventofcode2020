with (import <nixpkgs> {});
let
  env = buildEnv {
    name = "python-environment";
    inherit python;
  };

in stdenv.mkDerivation {
  name = "python-environment";
  buildInputs = [python-environment python];
}
