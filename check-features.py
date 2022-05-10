#!/usr/bin/python3
from pathlib import Path
import frontmatter

with open('template.md', "rt") as f:
    metadata, content = frontmatter.parse(f.read())
    acceptable_features = set(metadata['features'])

failed = False
for filename in Path('_board').glob("*.md"):
    with open(filename, "rt") as f:
        metadata, content = frontmatter.parse(f.read())
    features = metadata.get('features') or ()
    for feature in sorted(set(features) - acceptable_features):
        print(f"{filename}:0: Non-standard feature: {feature}")
        failed = True

raise SystemExit(failed)
