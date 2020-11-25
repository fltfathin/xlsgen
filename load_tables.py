from toml import load
from pathlib import Path

tables = load(Path("tables.toml").open("r"))

print(tables)