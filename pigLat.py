print("Enter the English message to translate into pig latin:")
words = input().split()
vowels = "aeiouyAEIOUY"

latin_words = []
for word in words:
    if not word.isalpha():
        latin_words.append(word)
        continue
    latin_word = ""
    if word[0] in vowels:
        latin_word = word
        if len(word) > 1 and word[-1].isupper():
            latin_word += "YAY"
        else:
            latin_word += "yay"
    else:
        start_ind = 1
        for i, char in enumerate(word[1:]):
            if char in vowels:
                start_ind = i + 1
                break
        if word[0].isupper():
            latin_word = word[start_ind].upper() + word[start_ind+1:]
        else:    
            latin_word = word[start_ind].lower() + word[start_ind+1:]
        if word[-1].isupper():
            latin_word += word[:start_ind].upper() + "AY"
        else:
            latin_word += word[:start_ind].lower() + "ay"
    latin_words.append(latin_word)


print(" ".join(latin_words))

