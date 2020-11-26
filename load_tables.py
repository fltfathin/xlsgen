from toml import load
from pathlib import Path

# this file is not really working now


tables = load(Path("tables.toml").open("r"))
print(tables)
