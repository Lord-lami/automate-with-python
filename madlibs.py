content = ""
with open("madlibs template.txt") as madlibs_template_file:
    content = madlibs_template_file.read()
    placeholders = ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]
    i = 0
    while placeholders:
        placeholder = placeholders[i]
        start_ind = content.find(placeholder)
        if start_ind == -1:
            del placeholders[i]
            if i >= len(placeholders):
                i = 0
            continue
        a_or_an = ""
        if placeholder[0].lower() in "aeiou":
            a_or_an = "an"
        else:
            a_or_an = "a"
        print(f"Enter {a_or_an} {placeholder.lower()}:")
        replacement = input()
        content = content[:start_ind] + replacement + content[start_ind+len(placeholder):]
        i += 1
        if i >= len(placeholders):
            i = 0

print(content)
with open("madlibs filled.txt", "w") as madlibs_filled_file:
    madlibs_filled_file.write(content)