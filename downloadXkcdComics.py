# downloadXkcdComics.py - Downloads XKCD comics

import requests, logging, bs4, sys
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

max_download_limit = 5
if len(sys.argv) > 1:
    max_download_limit = int(sys.argv[1])

xkcd_page_link = "https://xkcd.com"
filename = ""

for _ in range(max_download_limit):
    # Download pages with the requests module.
    res = requests.get(xkcd_page_link)
    res.raise_for_status()
    logging.debug("Recieved page: " + xkcd_page_link)

    # Find the URL of the comic image for a page using Beautiful Soup.
    comic_soup = bs4.BeautifulSoup(res.text, "html.parser")
    image_link = comic_soup.select_one("div #comic").select_one("img").get("src")
    image_link = "http:" + str(image_link)
    logging.debug("Image Link: " + image_link)

    # Find the URL of the Previous Comic link.
    prev_link_path = comic_soup.select_one('a[rel="prev"]').get("href")
    prev_link = "https://xkcd.com" + prev_link_path
    logging.debug("Previous Comic Link: " + prev_link)

    # Stop at the first comic
    if prev_link == xkcd_page_link + "#":
        break

    # Setup the XKCD Comics folder
    img_res = requests.get(image_link, stream=True)
    img_res.raise_for_status()
    comics_dir = Path("XKCD Comics")
    if not comics_dir.exists():
        comics_dir.mkdir()
        logging.debug("Created XKCD Comics Folder")

    # Determine the filename
    if not filename:
        filename = str(int(prev_link_path.strip("/")) + 1)
    else:
        filename = prev_link_path.strip("/")
    filename += ".png"

    # Skip if the filename alread exists in the XKCD Comics folder
    filepath = comics_dir / filename
    if filepath.exists():
        logging.debug("Skipped Writing to " + filename)
        continue
    else:
        logging.debug("Writing to " + filename + "...")
    

    # Download and save the comic image to the hard drive with iter_content().
    with open(filepath, "wb") as img_file:
        print(f"Downloading {filename}: ", end="")
        for chunk in img_res.iter_content(1024):
            img_file.write(chunk)
            print("|", end="")
        print(" Done")
        logging.debug("Written " + filename)

    # Go to the previous comic
    xkcd_page_link = prev_link
