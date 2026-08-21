def display_inventory(inventory: dict[str, int]) -> None:
    total = 0
    print("Inventory:")
    for name, count in inventory.items():
        total += count
        print(count, name)
    print("Total number of items:", total)

def add_to_inventory(inventory: dict[str, int], added_items: list[str]) -> dict[str, int]:
    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)