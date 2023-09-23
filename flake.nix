{
  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nix-packages.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    nix-systems.url = "github:nix-systems/default";
  };
  outputs = inputs @ {
    flake-parts,
    nix-packages,
    nix-systems,
    ...
  }: let
    packagesModule = {
      perSystem = {system, ...}: {
        _module.args.packages = import nix-packages {
          inherit system;
        };
      };
    };

    systemsModule = {
      systems = import nix-systems;
    };
  in
    flake-parts.lib.mkFlake {inherit inputs;} {
      imports = [
        packagesModule
        systemsModule
      ];

      perSystem = {packages, ...}: let
        python3 = packages.python3.withPackages (pythonPackages: [
          pythonPackages.aiodns
          pythonPackages.aiohttp
          pythonPackages.gql
        ]);
      in {
        devShells.default = packages.mkShellNoCC {
          packages = [
            python3
          ];
        };

        packages.python3 = python3;
      };
    };
}
