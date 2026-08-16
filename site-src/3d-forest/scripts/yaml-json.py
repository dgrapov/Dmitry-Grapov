#!/usr/bin/env python3
"""Convert between sections.json (array) and sections.yml (editor-friendly template).

Usage:
  python3 yaml-json.py to-yaml sections.json sections.yml
  python3 yaml-json.py to-json sections.yml sections.json
"""
import sys
import json
import yaml

SCENE_NAMES = [
    "mushroom ring (front left) — Origin / about",
    "hollow in the right redwood — Code & science",
    "slime mold on the floor — Teaching",
    "the crow (perched, flies between branches) — Writing & art",
    "the spring pool (right) — Contact",
]

HEADER = """\
# Digital Food Forest — site content template
#
# Edit this file, then regenerate the site with:
#   scripts/sync-sections.sh apply
#
# Order matters: index 0-4 map to fixed objects in the 3D scene (see README.md).
# `index` and `scene` below are for your reference only and are ignored on import
# (order in this file is what counts) — do not reorder entries.
"""


class LiteralStr(str):
    """Marker so PyYAML dumps long body text as a block scalar (|-)."""


def literal_presenter(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


yaml.add_representer(LiteralStr, literal_presenter)


def to_yaml(json_path, yaml_path):
    with open(json_path, encoding="utf-8") as f:
        sections = json.load(f)

    template = []
    for idx, s in enumerate(sections):
        template.append({
            "index": idx,
            "scene": SCENE_NAMES[idx] if idx < len(SCENE_NAMES) else "",
            "kicker": s["kicker"],
            "title": s["title"],
            "body": LiteralStr(s["body"]),
            "chips": s["chips"],
            "links": s["links"],
        })

    with open(yaml_path, "w", encoding="utf-8") as f:
        f.write(HEADER)
        f.write("\n")
        yaml.dump(
            template, f,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=100,
        )
    print(f"Wrote {yaml_path} ({len(template)} sections).")


def to_json(yaml_path, json_path):
    with open(yaml_path, encoding="utf-8") as f:
        template = yaml.safe_load(f)

    if not isinstance(template, list):
        raise SystemExit("Expected a top-level YAML list of sections.")

    sections = []
    for i, entry in enumerate(template):
        for key in ("kicker", "title", "body", "chips", "links"):
            if key not in entry:
                raise SystemExit(f"Entry {i} is missing '{key}'")
        sections.append({
            "kicker": entry["kicker"],
            "title": entry["title"],
            "body": " ".join(entry["body"].split()),  # collapse block-scalar line wraps
            "chips": entry["chips"],
            "links": entry["links"],
        })

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(sections, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Wrote {json_path} ({len(sections)} sections).")


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in ("to-yaml", "to-json"):
        print(__doc__)
        sys.exit(1)
    mode, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    (to_yaml if mode == "to-yaml" else to_json)(src, dst)


if __name__ == "__main__":
    main()
