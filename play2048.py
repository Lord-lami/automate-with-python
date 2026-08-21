import logging, random, time
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto("https://play2048.co/", wait_until='domcontentloaded')
    logging.debug("Loaded!")
    closePopupButton = page.locator('button[class="bg-near-black absolute right-0 top-0 flex h-6 w-6 -translate-y-1/2 translate-x-1/2 items-center justify-center rounded-full"]')
    closePopupButton.click()
    game = page.locator('html')
    MOVES = ["ArrowUp", "ArrowDown", "ArrowRight", "ArrowLeft"]
    for _ in range(50):
        time.sleep(1)
        current_move = random.choice(MOVES)
        logging.debug("Current Move: " + current_move)
        game.press(current_move)
