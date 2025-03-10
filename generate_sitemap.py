#!/usr/bin/env python
import os
import xml.etree.ElementTree as ET
import datetime
import xml.dom.minidom

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
# Use full ISO 8601 datetime with timezone
now = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()

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
        # Remove trailing slash if present, except for root URL
        if full_url != BASE_URL.rstrip("/") + "/":
            full_url = full_url.rstrip("/")
        url_el = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url_el, "loc")
        loc.text = full_url
        lastmod = ET.SubElement(url_el, "lastmod")
        lastmod.text = now

# Generate pretty-printed XML
rough_string = ET.tostring(urlset, encoding="utf-8")
reparsed = xml.dom.minidom.parseString(rough_string)
pretty_xml = reparsed.toprettyxml(indent="  ", encoding="utf-8")

# Write the XML to OUTPUT_FILE
with open(OUTPUT_FILE, "wb") as f:
    f.write(pretty_xml)

print(f"Sitemap generated at: {OUTPUT_FILE}")
