import sys, requests, bs4, webbrowser, logging
from urllib.parse import quote

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
# logging.disable(logging.CRITICAL)

# Read the command line arguments from sys.argv.
if len(sys.argv) > 1:
    search_query_raw = " ".join(sys.argv[1:])
else:
    print("""No search query provided to searchpypi command
Usage: searchpypi [query]""", file=sys.stderr)
    sys.exit()
logging.debug("Loaded Search Query: " + search_query_raw)

# Fetch the search results page with the requests module.
search_res = requests.get(f"https://pypi.org/search/?q={quote(search_query_raw)}")
search_res.raise_for_status()
logging.debug("Got Search Page: " + f"https://pypi.org/search/?q={quote(search_query_raw)}")
logging.debug(search_res.text)

# Find the links to each search result.
search_soup = bs4.BeautifulSoup(search_res.text, "html.parser")
nbr_of_links = 3
links = search_soup.select("a .package-snippet")[:nbr_of_links]
logging.debug("Found links:")
logging.debug(links)

# Call the webbrowser.open() function to open the web browser.
for l in links:
    logging.debug("Opening " + str(l.get("href")))
    webbrowser.open_new_tab(str(l.get("href")))
