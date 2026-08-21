import openpyxl

prod_2_new_cost = {}

print("Update Products in productSales3.xlsx")

# Ask for product cost updates
while True:
    print("What is the name of the product you want to update?")
    print("Press Enter to start update")
    prod = input()
    if prod == "":
        break
    print("What is the new cost per pound?")
    new_cost = input()
    if new_cost == "":
        break
    new_cost = round(float(new_cost), 2)
    prod_2_new_cost[prod.title()] = new_cost


print(prod_2_new_cost)

wb = openpyxl.load_workbook('produceSales3.xlsx')

sheet = wb.active
print("Updating...")
for r in sheet.rows:
    if str(r[0].value) in prod_2_new_cost.keys():
        sheet[r[1].coordinate] = prod_2_new_cost[str(r[0].value)]

wb.save("produceSales3_updated.xlsx")
print("Done")
