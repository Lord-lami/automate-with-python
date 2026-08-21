import re

def twist_words(sentence: str) -> str:
    wordSplitRe = re.compile(r"(\w+)(\w)")
    return wordSplitRe.subn(r"\g<2>\g<1>", sentence)[0]

print(twist_words('Hello world! How are you? I am fine.'))