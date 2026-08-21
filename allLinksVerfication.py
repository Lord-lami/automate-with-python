import sys, logging, time, requests
from playwright.sync_api import sync_playwright
from urllib.parse import urlparse, urljoin

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
# logging.disable(logging.CRITICAL)

# Parse website argument
if len(sys.argv) > 1:
    website = sys.argv[1]
else:
    print("""No link provided
Usage allLinksVerification.py [website to check]""", file=sys.stderr)
    sys.exit(1)

all_working_links = []
all_uncertain_links = []
all_broken_links = []

with sync_playwright() as playwright:
    browser = playwright.firefox.launch()
    page = browser.new_page()
    page.goto(website)

    links = page.locator('a')
    prev_links = set([website])
    broken_links = set([])
    uncertain_links = set([])
    print(f"Found {links.count()} links in {website}")
    print()
    for l in links.all():
        time.sleep(1)

        # Turn relative links into absolute urls
        href = l.get_attribute("href")
        if not urlparse(href).scheme:
            href = str(urljoin(website, href))
        
        link_info = {"href": href, "Link Text": l.inner_text()}

        # Store the link so it is not revisited
        if href in prev_links:
            if href in broken_links:
                all_broken_links.append(link_info)
            if href in uncertain_links:
                all_uncertain_links.append(link_info)
            else:
                all_working_links.append(link_info)
            logging.debug(f"Skipping {l.evaluate("element => element.outerHTML")}")
            continue
        else:
            prev_links.add(href)
            logging.debug(f"Checking {l.evaluate("element => element.outerHTML")}")

        # Test the link
        with requests.get(href) as resp:
            if resp.status_code == 404 or resp.status_code >= 500:
                all_broken_links.append(link_info)
                broken_links.add(href)
                logging.debug("Broken Link")
            elif resp.status_code >= 400 and resp.status_code < 500:
                all_uncertain_links.append(link_info)
                uncertain_links.add(href)
                logging.debug("Uncertain Link")
            else:
                all_working_links.append(link_info)
                logging.debug("Working Link")

print("Working Links:", *all_working_links, sep="\n")
print("-" * 30)
print("Uncertain Links:", *all_uncertain_links, sep="\n")
print("-" * 30)
print("Broken Links:", *all_broken_links, sep="\n")
print("-" * 30)
print(f"{len(all_working_links)} Working Links")
print(f"{len(all_uncertain_links)} Uncertain Links")
print(f"{len(all_broken_links)} Broken Links")

        
