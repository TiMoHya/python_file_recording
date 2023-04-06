from pprint import pprint
from typing import Dict

with open('recipes.txt', 'rt', encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        food_name = line.strip()
        number_ingredients = int(file.readline().strip())
        ingredients = []
        for _ in range(number_ingredients):
            ingridient_name, quantity, measure = file.readline().strip().split(" | ")
            ingredients.append({
                "ingridient_name": ingridient_name,
                "quantity": int(quantity),
                "measure": measure

            })
        file.readline()
        cook_book[food_name] = ingredients

    #pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count

            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']

    return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

