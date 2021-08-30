import requests

dishes = {}
dish_list = []

with open('data.txt', 'r', encoding = 'utf-8') as data_file:
    strings_from_file = data_file.readlines()


    strings_cutted = [s[:-1] for s in strings_from_file]

    list_of_elements = []
    element = []

    for s in strings_cutted:
        if s == '':
            list_of_elements.append(element)
            element = []
        else:
            element.append(s)

    list_of_elements.append(element)


    for element in list_of_elements:
        dish = {element[0]: []}

        count = int(element[1])
        position = 2
        while count:
            ingredient_name, quantity, measure = element[position].split(' | ')
            ingredient = {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure}
            dish[element[0]].append(ingredient)
            position += 1
            count -= 1
        dishes[element[0]] = dish[element[0]]


dish_list = list(dishes.keys())

def get_shop_list_by_dishes(dish_lst, persons):
    ingredients = {}

    for dish in dish_lst:

        dish_ingredients = dishes[dish]

        for ingredient in dish_ingredients:
            if ingredient['ingredient_name'] in ingredients:
                ingredients[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
            else:

                ingredients[ingredient['ingredient_name']] = {
                    'quantity': ingredient['quantity'],
                    'measure': ingredient['measure'],
                }

    for ingredient in ingredients:
        ingredients[ingredient]['quantity'] = ingredients[ingredient]['quantity'] * persons

    print(ingredients)

print(dishes)
get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
get_shop_list_by_dishes(['Утка по-пекински', 'Запеченный картофель' ], 12)


