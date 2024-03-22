import argparse
import sys
import xml.etree.ElementTree as ET

def main():
    args = parse_args()
    sitemap_path = args.sitemap

    # Set to store unique URLs
    unique_urls = set()

    # Parse the XML file
    tree = ET.parse(sitemap_path)
    root = tree.getroot()

    # Namespace handling
    # Sitemaps use the namespace http://www.sitemaps.org/schemas/sitemap/0.9
    namespace = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    # Extract and store all URLs
    for url in root.findall('sitemap:url/sitemap:loc', namespace):
        unique_urls.add(url.text)

    print(f"[+] Unique URLs found from {sitemap_path}")
    for url in unique_urls:
        print(url)


def parse_args():
    print("----   SiteMap Parser - v0.1 ----")
    parser = argparse.ArgumentParser(
        add_help=True,
        description="Extract unique URLs from sitemap.xml file"
    )

    parser.add_argument("-s", "--sitemap", type=str, required=True, help="Sitemap XML file (path)")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()

if __name__ == "__main__":
    main()
