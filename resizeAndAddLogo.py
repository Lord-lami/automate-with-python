from pathlib import Path
from PIL import Image


PNGS = Path().cwd().glob("*.png")
JPGS = Path().cwd().glob("*.jpg")

LOGO = Image.open('catlogo.png')
ASPECT_RATIO = LOGO.size[1] / LOGO.size[0]
# print("PNGS:", list(PNGS))
# print("JPGS:", list(JPGS))


def shrinkAndAddLogoAll(g: list[Path]):
    for p in g:
        if p.name == "catlogo.png":
            continue
        pic = Image.open(p).copy()
        width, height = pic.size
        if width > 300 and width > height:
            pic = pic.resize((300, int((height/width) * 300)))
        elif height > 300 and height > width:
            pic = pic.resize((int((width/height) * 300), 300))
        elif height > 300 and height == width:
            pic = pic.resize((300, 300))
        logo_width = int(pic.size[0] * 0.3)
        logo_height = int(logo_width * ASPECT_RATIO)
        current_logo = LOGO.resize((logo_width, logo_height))
        pic.paste(current_logo, (pic.size[0] - logo_width, pic.size[1] - logo_height), current_logo)
        pic.show("Test")

        

shrinkAndAddLogoAll(PNGS)