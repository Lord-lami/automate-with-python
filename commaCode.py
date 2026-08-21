def comma_code(l: list[str]) -> str:
    strlist = ""
    if len(l) > 0:
        strlist = l[0]
        for item in l[1:-1]:
            strlist += ", " + item
        if len(l) > 1:
            strlist += " and " + l[-1]
    return strlist

print(comma_code([]))