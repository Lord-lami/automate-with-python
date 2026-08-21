import sys, ezsheets, shelve
from pathlib import Path
from auditBoringcoin import updateAccounts

if not Path("boringcoinAccounts").exists():
    ss = ezsheets.Spreadsheet("https://autbor.com/boringcoin")
    updateAccounts(ss)

accounts = {}
with shelve.open("boringcoinAccounts") as bcAccs:
    accounts = bcAccs["data"]

print("Who is the Sender?")
sender = input()

print("Who is the Receiver?")
receiver = input()

print("What is the Amount?")
amount = int(input())


if sender not in accounts.keys():
    print(f"Invalid Transaction: The Sender {sender} doesn't have an Boring Coin account"\
            , file=sys.stderr)
    sys.exit(1)
elif accounts[sender] < amount:
    print(f"Invalid Transaction: The Sender {sender} doesn't have enough Boring Coins for this transaction"\
            , file=sys.stderr)
    sys.exit(1)
else:
    ss = ezsheets.Spreadsheet("https://autbor.com/boringcoin")
    sheet = ss.sheets[0]
    assert type(sheet) == ezsheets.Sheet
    rows = sheet.getRows()
    rows.append([sender, receiver, str(amount)])
    sheet.updateRows(rows)
    updateAccounts(ss)

