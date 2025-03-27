#!/usr/bin/env python
import os
import xml.etree.ElementTree as ET
import datetime
import xml.dom.minidom

# Configuration
BASE_URL = "https://fbetteo.github.io/blog"  # Removed trailing slash
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
# Use simple YYYY-MM-DD format
now = datetime.datetime.now().strftime("%Y-%m-%d")

# Walk through the SITE_DIR to find .html files
urls_added = set()  # Track URLs to avoid duplicates
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
            url_path = relative_path[: -len(".html")]  # Remove .html extension

        # Add trailing slash to directory URLs
        if url_path == "" or url_path.endswith("/"):
            full_url = BASE_URL + "/" + url_path
        else:
            full_url = BASE_URL + "/" + url_path

        # Skip if we've already added this URL
        if full_url in urls_added:
            continue
        urls_added.add(full_url)

        url_el = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url_el, "loc")
        loc.text = full_url
        lastmod = ET.SubElement(url_el, "lastmod")
        lastmod.text = now

# # Generate pretty-printed XML
# rough_string = ET.tostring(urlset, encoding="utf-8")
# reparsed = xml.dom.minidom.parseString(rough_string)
# pretty_xml = reparsed.toprettyxml(indent="  ", encoding="utf-8")

# # Write the XML to OUTPUT_FILE
# with open(OUTPUT_FILE, "wb") as f:
#     f.write(pretty_xml)

# Write the XML to OUTPUT_FILE using ElementTree's write method (adds XML declaration automatically)
tree = ET.ElementTree(urlset)
tree.write(OUTPUT_FILE, encoding="utf-8", xml_declaration=True)


print(f"Sitemap generated at: {OUTPUT_FILE}")
print(f"Total URLs: {len(urls_added)}")
