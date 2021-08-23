import requests

dishes = {}

with open('data.txt', 'r', encoding='utf-8') as data_file:
    strings_from_file = data_file.readlines()
    # print(strings_from_file)

    strings_cutted = [s[:-1] for s in strings_from_file]

    # strings_cutted = []
    # for s in strings_from_file:
    #     strings_cutted.append(s[:-1])
    # print(strings_cutted)

    list_of_elements = []
    element = []

    for s in strings_cutted:
        if s == '':
            list_of_elements.append(element)
            element = []
        else:
            # print(s)
            element.append(s)

    list_of_elements.append(element)
    # print(list_of_elements)

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
        # print(dish)


# print(dishes)


def get_shop_list_by_dishes(dishes, persons):
    ingredients = {
        # 'ingredient_name':
        #     {
        #         'quantity': 123,
        #         'measure': 'pts'
        #     }
    }

    for dish in dishes.values():
        # ...
        # print(dish)
        for ingredient in dish:
            if ingredient['ingredient_name'] in ingredients:
                ingredients[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
            else:

                ingredients[ingredient['ingredient_name']] = {
                    'quantity': ingredient['quantity'],
                    'measure': ingredient['measure'],
                }

    for ingredient in ingredients:
        ingredients[ingredient]['quantity'] = ingredients[ingredient]['quantity'] * persons

        # for ingredient in dish:
        #     if ingredients[ingredient['ingredient_name']]:
        #
        #         ingredient['quantity'] *= persons
        #         ingredients[ingredient['ingredient_name']['quantity']] = ingredient['quantity']

    print(ingredients)


get_shop_list_by_dishes(dishes, 2)
get_shop_list_by_dishes(dishes, 12)



