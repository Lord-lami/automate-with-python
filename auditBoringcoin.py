import ezsheets, shelve

def updateAccounts(ss: ezsheets.Spreadsheet):
    sheet = ss.sheets[0]
    assert type(sheet) == ezsheets.Sheet
    # print(ss.sheets)

    accounts = {}

    for row in sheet.getRows():
        sender = row[0]
        receiver = row[1]
        amount = int(row[2])
        if sender != "PRE-MINE":
            accounts.setdefault(sender, 0)
            accounts[sender] -= amount

        if receiver != "PRE-MINE":
            accounts.setdefault(receiver, 0)
            accounts[receiver] += amount

    with shelve.open("boringcoinAccounts") as bcAccs:
        bcAccs["data"] = accounts
    # print(accounts)


