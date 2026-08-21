import logging, pyperclip, requests, bs4, sys
from pathlib import Path
from urllib.parse import urlparse

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
# logging.disable(logging.CRITICAL)

website = pyperclip.paste()
logging.debug(f"Downloading {website}...")

downloadPath = Path().home() / "Downloads"
name = urlparse(website).hostname
downloadPath /= name
downloadPath.mkdir(exist_ok=True)
logging.debug(f"To {downloadPath}")

# templatesPath = downloadPath / "templates"
# templatesPath.mkdir(exist_ok=True)

# staticPath = downloadPath / "static"
# staticPath.mkdir(exist_ok=True)

refresh = False
if len(sys.argv) > 1:
    refresh = sys.argv[1][0:2] == "-r"

def download(urlOrPath: str) -> None:
    is_path = not bool(urlparse(urlOrPath).scheme)
    filename = str(urlparse(urlOrPath).path.rstrip("/").split("/")[-1])
    downloadLink = ""
    if is_path:
        parts = website.rstrip("/").split("/")
        if len(parts) > 1:
            downloadLink += "/".join(parts[0:-1])
        else:
            downloadLink += parts[0]
        downloadLink += "/" + urlOrPath
        folder = downloadPath / Path(urlOrPath).parent
    else:
        downloadLink = urlOrPath
        folder = downloadPath / "external-resources"

    filepath = folder / filename
    
    if refresh or not filepath.exists():
        folder.mkdir(parents=True, exist_ok=True)
        with open(filepath, "wb") as file:
            with requests.get(downloadLink, stream=True) as resp:
                resp.raise_for_status()
                logging.debug(f"Downloading {downloadLink}...")
                logging.debug(f"To {filepath}")
                for chunk in resp.iter_content(1024):
                    file.write(chunk)
                logging.debug("Download Complete")


with requests.get(website, stream=True) as resp:
    resp.raise_for_status()
    filename = urlparse(website).path.rstrip("/").split("/")[-1]
    if filename[-5:] != ".html":
        filename += ".html"
    if urlparse(website).path == "/":
        filename = "index.html"
    with open(downloadPath / filename, "wb") as file:
        logging.debug(f"Downloading {filename}...")
        logging.debug(f"To {downloadPath / filename}")
        for chunk in resp.iter_content(1024):
            file.write(chunk)
        logging.debug(f"Download Complete")
    with open(downloadPath / filename) as file:
        websoup = bs4.BeautifulSoup(file, 'html.parser')
        styleSheets = websoup.select("link[rel=stylesheet]")
        for ss in styleSheets:
            download(ss.get("href"))
        sources = websoup.select("[src]")
        for s in sources:
            download(s.get("src"))
