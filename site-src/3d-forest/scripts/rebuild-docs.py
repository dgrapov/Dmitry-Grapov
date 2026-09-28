#!/usr/bin/env python3
"""Rebuild docs/index.html from `Dmitry Grapov Forest.dc.html` without the authoring tool.

docs/index.html is a self-contained bundle: a bootstrap script, a
`__bundler/manifest` of embedded resources (gzip+base64), and the page itself
as a JSON-encoded string in `__bundler/template`. This script keeps the
bundle's bootstrap and embedded resources, and replaces the page's own parts
with the current source:

  * <title>/<meta> tags     -> template <head> AND the outer shell <head>
                               (link-preview scrapers don't run JS, so the
                               outer shell is what LinkedIn/Slack/Google see)
  * page <style> in helmet  -> the source's helmet <style> block
  * markup + logic          -> everything from the page's root <div> through
                               the text/x-dc logic script
  * three.js                -> embedded from vendor/ (the import map points at
                               its manifest uuid, so no runtime unpkg request)

and re-serializes the template with "</" escaped as "<\\/" (see the README's
"sharp edge" section: without it the embedded </script> closes the outer tag).

Usage (from anywhere):  python3 site-src/3d-forest/scripts/rebuild-docs.py
Always load the result in a real browser afterwards.
"""
import base64
import gzip
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
FOREST = HERE.parent
REPO = FOREST.parents[1]
SRC = FOREST / "Dmitry Grapov Forest.dc.html"
OUT = REPO / "docs" / "index.html"
THREE = FOREST / "vendor" / "three-0.160.0.module.min.js"
THREE_UUID = "7f3c2a10-0160-4d1e-9a7e-7472ee000160"  # stable id for the embedded three.js
ROOT_DIV = '<div style="position:fixed;inset:0;background:#030706'


def once(hay, needle, what):
    n = hay.count(needle)
    if n != 1:
        raise SystemExit(f"expected exactly one {what}, found {n}")
    return hay.index(needle)


def encode_camel(html):
    # The bundle stores camelCase attributes the way the runtime's encodeCase() does
    # (onClick -> sc-camel-on-click), since DOMParser would otherwise lowercase them.
    def attr(m):
        name = m.group(1)
        return "sc-camel-" + re.sub(r"[A-Z]", lambda c: "-" + c.group(0).lower(), name) + "="
    return re.sub(r"(?<=\s)([a-z]+[A-Z][A-Za-z]*)=", attr, html)


def head_meta(src):
    head = src[: src.index("</head>")]
    return "\n".join(re.findall(r"<title>.*?</title>|<meta (?:name|property)=\"(?!viewport)[^>]*>", head))


def main():
    src = SRC.read_text()
    bundle = OUT.read_text()

    m = re.search(r'(<script type="__bundler/template">)(.*?)(</script>)', bundle, re.S)
    tpl = json.loads(m.group(2))

    # 1. page markup + logic
    s0 = once(src, ROOT_DIV, "root div in source")
    s1 = src.rindex("</script>")
    t0 = once(tpl, ROOT_DIV, "root div in template")
    t1 = tpl.rindex("</script>")
    logic_at = once(src, '<script type="text/x-dc"', "logic script")
    markup, logic = src[s0:logic_at], src[logic_at:s1]
    body = encode_camel(markup) + logic.replace("data-dc-script data-props", 'data-dc-script="" data-props', 1)
    tpl = tpl[:t0] + body + tpl[t1:]

    # 2. page-own <style> inside helmet (the last <style> before </helmet>)
    src_style = re.search(r"<style>\s*html,body\{.*?</style>", src, re.S).group(0)
    tpl_style = re.search(r"<style>\s*html,body\{.*?</style>", tpl, re.S)
    tpl = tpl[: tpl_style.start()] + src_style + tpl[tpl_style.end():]

    # 3. <title>/<meta> in the template head (drop any previous ones first)
    meta = head_meta(src)
    tpl = re.sub(r"\n?(<title>.*?</title>|<meta (?:name|property)=\"(?!viewport)[^>]*>)", "", tpl[: tpl.index("</head>")]) + tpl[tpl.index("</head>"):]
    vp = once(tpl, '<meta name="viewport" content="width=device-width, initial-scale=1">', "viewport meta")
    vp_end = vp + len('<meta name="viewport" content="width=device-width, initial-scale=1">')
    tpl = tpl[:vp_end] + "\n" + meta + tpl[vp_end:]

    # 4. three.js: embed and point the import map at it
    tpl = re.sub(r'"three":\s*"[^"]+"', f'"three": "{THREE_UUID}"', tpl)
    mm = re.search(r'(<script type="__bundler/manifest">)(.*?)(</script>)', bundle, re.S)
    manifest = json.loads(mm.group(2))
    manifest[THREE_UUID] = {
        "mime": "application/javascript",
        "compressed": True,
        "data": base64.b64encode(gzip.compress(THREE.read_bytes(), mtime=0)).decode(),
    }
    bundle = bundle[: mm.start(2)] + json.dumps(manifest, separators=(",", ":")) + bundle[mm.end(2):]

    # 5. re-serialize the template ("</" must never appear raw inside the outer <script>)
    m = re.search(r'(<script type="__bundler/template">)(.*?)(</script>)', bundle, re.S)
    enc = json.dumps(tpl, ensure_ascii=False).replace("</", "<\\/")
    bundle = bundle[: m.start(2)] + enc + bundle[m.end(2):]

    # 6. outer shell head: real title + meta for crawlers and link previews
    shell_head_end = bundle.index("</head>")
    shell = bundle[:shell_head_end]
    shell = re.sub(r"\n?\s*(<title>.*?</title>|<meta (?:name|property)=\"(?!viewport)[^>]*>)", "", shell)
    shell = shell.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n  ' + meta.replace("\n", "\n  "), 1)
    bundle = shell + bundle[shell_head_end:]

    # the template must round-trip exactly, and must not contain a raw "</" that
    # would terminate the outer <script type="__bundler/template"> early
    back = re.search(r'<script type="__bundler/template">(.*?)</script>', bundle, re.S).group(1)
    assert json.loads(back) == tpl, "template did not round-trip"
    OUT.write_text(bundle)
    print(f"wrote {OUT.relative_to(REPO)} ({len(bundle) // 1024} KB)")


if __name__ == "__main__":
    main()
