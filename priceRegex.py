import re

def get_price(sentence: str) -> list[str]:
    priceRe = re.compile(r"\$\d+(?:\.\d\d)?")
    return priceRe.findall(sentence)

print("Enter a sentence")
sentence = input()

prices = get_price(sentence)
print(*prices, sep="\n")
