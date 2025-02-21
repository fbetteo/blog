#!/usr/bin/env python
import os
import xml.etree.ElementTree as ET
import datetime

# Configuration
BASE_URL = "https://fbetteo.github.io/blog/"
SITE_DIR = "site"  # MkDocs build output directory
OUTPUT_FILE = os.path.join(SITE_DIR, "sitemap.xml")
EXCLUDE_DIRS = {
    "overrides",
    "about",
    "user_manual",
    "github-site",
}  # directories to skip
EXCLUDE_FILES = {
    "404.html",
}  # individual files to skip (if desired)

# Create the root XML element for the sitemap
urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
today = datetime.date.today().isoformat()

# Walk through the SITE_DIR to find .html files
for root, dirs, files in os.walk(SITE_DIR):
    # Remove directories we want to exclude from the walk
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

    for file in files:
        if not file.endswith(".html"):
            continue
        if file in EXCLUDE_FILES:
            continue
        # Optionally, skip sitemap.xml itself
        if file == "sitemap.xml":
            continue

        file_path = os.path.join(root, file)
        # Compute the relative URL path
        relative_path = os.path.relpath(file_path, SITE_DIR)
        # Normalize to forward slashes
        relative_path = relative_path.replace(os.path.sep, "/")
        # Map index.html to directory URL
        if relative_path.endswith("index.html"):
            url_path = relative_path[: -len("index.html")]
        else:
            url_path = relative_path

        full_url = BASE_URL.rstrip("/") + "/" + url_path.lstrip("/")
        url_el = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url_el, "loc")
        loc.text = full_url
        lastmod = ET.SubElement(url_el, "lastmod")
        lastmod.text = today

# Write the XML tree to OUTPUT_FILE
tree = ET.ElementTree(urlset)
tree.write(OUTPUT_FILE, encoding="utf-8", xml_declaration=True)
print(f"Sitemap generated at: {OUTPUT_FILE}")
