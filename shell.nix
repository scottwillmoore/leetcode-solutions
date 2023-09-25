let
  packages = import <packages> {};
in
  packages.mkShellNoCC {
    name = "leetcode-solutions";
    packages = [
      (packages.python3.withPackages (pythonPackages: [
        pythonPackages.aiodns
        pythonPackages.aiohttp
        pythonPackages.black
        pythonPackages.gql
        pythonPackages.mypy
      ]))
    ];
  }
