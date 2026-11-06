#!/usr/bin/env python3
"""Count Cloudflare Web Analytics script elements in saved HTML (Python 3).

Usage: python3 check-analytics-html.py page.html
Reads a local file only. Does not execute JavaScript or send network requests.
Beacon tokens and other script contents are never printed.
"""

import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


class BeaconParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.configured = 0
        self.inert = []

    def handle_starttag(self, tag, attrs):
        if self.inert:
            if tag == "template" and self.inert[-1] == "template":
                self.inert.append(tag)
            return
        if tag in {"template", "noscript", "textarea", "title"}:
            self.inert.append(tag)
            return
        if tag != "script":
            return
        attributes = dict(attrs)
        source = urlsplit(attributes.get("src") or "")
        if (source.hostname == "static.cloudflareinsights.com"
                and (source.path == "/beacon.min.js"
                     or source.path.startswith("/beacon.min.js/"))):
            self.count += 1
            self.configured += bool(attributes.get("data-cf-beacon"))

    def handle_endtag(self, tag):
        if self.inert and tag == self.inert[-1]:
            self.inert.pop()


def inspect_html(html):
    parser = BeaconParser()
    parser.feed(html)
    parser.close()
    return {
        "beacon_script_count": parser.count,
        "with_data_cf_beacon": parser.configured,
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 check-analytics-html.py page.html")
    try:
        result = inspect_html(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as error:
        sys.exit(f"Could not inspect HTML: {error}")
    print(json.dumps(result, ensure_ascii=False, indent=2))
