#!/usr/bin/env python3
"""Screenshot the scene at a battery of device sizes, for fast visual iteration.

Spins up a throwaway local static server (support.js's bootstrap uses fetch(),
which file:// URLs don't support), loads a target .dc.html or docs/index.html
in headless Chromium (software WebGL via SwiftShader, so it renders without a
real GPU), and saves one PNG per viewport + a contact sheet. Also surfaces any
pageerror/console-error per the repo's own "actually render it, don't just
parse it" verification rule.

Usage (run from anywhere):
  python3 preview-viewports.py [path-to-html] [--out DIR] [--wait MS]

  path-to-html   Repo-relative path. Default:
                 site-src/3d-forest/Dmitry Grapov Forest.dc.html

Examples:
  python3 preview-viewports.py
  python3 preview-viewports.py docs/index.html --out /tmp/after
"""
import argparse
import http.server
import socket
import sys
import threading
import time
from pathlib import Path
from urllib.parse import quote

from playwright.sync_api import sync_playwright

REPO_ROOT = Path(__file__).resolve().parents[3]  # scripts/ -> 3d-forest/ -> site-src/ -> repo root
DEFAULT_TARGET = "site-src/3d-forest/Dmitry Grapov Forest.dc.html"

# name -> (width, height)
VIEWPORTS = [
    ("iphone_se_portrait", 375, 667),
    ("iphone_14_portrait", 390, 844),
    ("iphone_14_landscape", 844, 390),
    ("pixel_7_portrait", 412, 915),
    ("ipad_mini_portrait", 744, 1133),
    ("desktop", 1280, 800),
]

LAUNCH_ARGS = ["--use-gl=angle", "--use-angle=swiftshader", "--enable-webgl", "--ignore-gpu-blocklist"]


def free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def serve(root, port):
    handler = lambda *a, **kw: http.server.SimpleHTTPRequestHandler(*a, directory=str(root), **kw)
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    return httpd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", nargs="?", default=DEFAULT_TARGET)
    ap.add_argument("--out", default=None)
    ap.add_argument("--wait", type=int, default=3000, help="ms to let the scene settle before screenshot")
    args = ap.parse_args()

    target_path = (REPO_ROOT / args.target).resolve()
    if not target_path.exists():
        sys.exit(f"Not found: {target_path}")

    out_dir = Path(args.out) if args.out else Path.cwd() / f"preview-{int(time.time())}"
    out_dir.mkdir(parents=True, exist_ok=True)

    port = free_port()
    httpd = serve(REPO_ROOT, port)
    url = f"http://127.0.0.1:{port}/{quote(str(target_path.relative_to(REPO_ROOT)))}"

    print(f"Target: {target_path.relative_to(REPO_ROOT)}")
    print(f"Serving repo root at http://127.0.0.1:{port}/  ->  {url}")
    print(f"Output: {out_dir}\n")

    results = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=LAUNCH_ARGS)
            for name, w, h in VIEWPORTS:
                page = browser.new_page(viewport={"width": w, "height": h})
                errs = []
                page.on("pageerror", lambda e: errs.append(f"pageerror: {e}"))
                page.on("console", lambda m: errs.append(f"console.{m.type}: {m.text}") if m.type == "error" else None)
                page.goto(url, wait_until="networkidle", timeout=30000)
                page.wait_for_timeout(args.wait)
                shot_path = out_dir / f"{name}_{w}x{h}.png"
                page.screenshot(path=str(shot_path))
                results.append((name, w, h, shot_path, errs))
                status = "OK" if not errs else f"{len(errs)} ERROR(S)"
                print(f"  [{status}] {name} ({w}x{h}) -> {shot_path.name}")
                for e in errs:
                    print(f"           {e}")
                page.close()
            browser.close()
    finally:
        httpd.shutdown()

    n_errors = sum(1 for *_, errs in results if errs)
    print(f"\n{len(results)} viewports captured, {n_errors} with errors. See {out_dir}")


if __name__ == "__main__":
    main()
