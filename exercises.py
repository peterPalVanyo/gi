from collections import Counter
from operator import itemgetter
import csv


def display_inventory(inv):
    print("Inventory: ")
    for key, value in inv.items():
        print(str(value) + " " + key)
    print("Total number of items: {}".format(sum(inv.values())))


def add_to_inventory(inventory, added_items):
    total = dict(Counter(inventory)+Counter(added_items))
    return total


def print_table(inventory, order=None):
    maximum = []
    for key in inventory.keys():
        maximum.append(key)
    maximum.sort(key=len)
    print("Inventory:")
    print("count".rjust(len(maximum[-1])) + "   " + "item name".rjust(len(maximum[-1])))
    print("-" * (2 * len(maximum[-1])) + "---")
    print(order)
    if order is None:
        for key, value in inventory.items():
            print(str(value).rjust(len(maximum[-1])) + "   " + str(key).rjust(len(maximum[-1])))
    elif order == "count,desc":
        for key, value in sorted(inventory.items(), key=itemgetter(1), reverse=True):
            print(str(value).rjust(len(maximum[-1])) + "   " + str(key).rjust(len(maximum[-1])))
    else:
        for key, value in sorted(inventory.items(), key=itemgetter(1)):
            print(str(value).rjust(len(maximum[-1])) + "   " + str(key).rjust(len(maximum[-1])))
    print("-" * (2 * len(maximum[-1])) + "---")
    print("Total number of items: {}".format(sum(inventory.values())))


def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
    print(readCSV)
    

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
print_table(inv, "count,asc")
with open('test_inventory.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
