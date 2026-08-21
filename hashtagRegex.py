import re

def get_hastags(sentence: str) -> list[str]:
    hashtagRe = re.compile(r"#\w+")
    return hashtagRe.findall(sentence)

print("Enter a sentence")
sentence = input()

hashtags = get_hastags(sentence)
print(*hashtags, sep="\n")
