s~(Patch:.*)~\1\nSource99: patch1.py\nBuildRequires: python3\nBuildRequires: python3-toml~g;
s~(%cargo_prep)~python3       %{SOURCE99}\n\1~g;
