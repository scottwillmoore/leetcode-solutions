{
  inputs = {
    nix-foundations.url = "github:scottwillmoore/nix-foundations";
  };

  outputs = inputs @ {nix-foundations, ...}:
    nix-foundations.mkFlake inputs {
      perSystem = {packages, ...}: {
        devShells.default = packages.mkShellNoCC {
          name = "leetcode-solutions";
          packages = [
            (packages.python3.withPackages (pythonPackages: [
              pythonPackages.aiodns
              pythonPackages.aiohttp
              pythonPackages.black
              pythonPackages.gql
            ]))
          ];
        };
      };
    };
}
