#!/usr/bin/env bash
# Two-way sync between sections.yml (what you edit) and the .dc.html source's
# `sections` array (what the scene actually reads).
#
#   sync-sections.sh export   html -> sections.yml   (pull current copy into the template)
#   sync-sections.sh apply    sections.yml -> html   (push your edits back into the source)
#
# Run from anywhere; paths below are relative to this script's location.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."   # site-src/3d-forest/

SRC_HTML="Dmitry Grapov Forest.dc.html"
YML="sections.yml"
JSON_TMP="$(mktemp -t sections-XXXXXX.json)"
trap 'rm -f "$JSON_TMP"' EXIT

cmd="${1:-}"
case "$cmd" in
  export)
    node scripts/extract-sections.js "$SRC_HTML" > "$JSON_TMP"
    python3 scripts/yaml-json.py to-yaml "$JSON_TMP" "$YML"
    echo "Edit $YML, then run: scripts/sync-sections.sh apply"
    ;;
  apply)
    python3 scripts/yaml-json.py to-json "$YML" "$JSON_TMP"
    node scripts/inject-sections.js "$SRC_HTML" "$JSON_TMP"
    echo "Now re-export/rebuild docs/index.html per README.md before deploying."
    ;;
  *)
    echo "Usage: $0 {export|apply}" >&2
    exit 1
    ;;
esac
