from decorators import decorator, parameterized_decorator


@decorator
def get_cook_book1():
    with open('recipes.txt', encoding='utf-8') as file_object:
        cook_book = {}
        for line in file_object:
            dish_name = line.strip()
            ingredients_list = []
            ingredients_quantity = file_object.readline()
            for _ in range(int(ingredients_quantity)):
                ingredient_name, quantity, measure = file_object.readline().split(' | ')
                ingredients_list.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()})
            cook_book[dish_name] = ingredients_list
            file_object.readline()
    return cook_book

@parameterized_decorator(path_to_file='logs.txt')
def get_cook_book2():
    with open('recipes.txt', encoding='utf-8') as file_object:
        cook_book = {}
        for line in file_object:
            dish_name = line.strip()
            ingredients_list = []
            ingredients_quantity = file_object.readline()
            for _ in range(int(ingredients_quantity)):
                ingredient_name, quantity, measure = file_object.readline().split(' | ')
                ingredients_list.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()})
            cook_book[dish_name] = ingredients_list
            file_object.readline()
    return cook_book


@decorator
def multiplier1(a, b, c):
    return a * b * c

@parameterized_decorator(path_to_file='logs.txt')
def multiplier2(a, b, c):
    return a * b * c


if __name__ == "__main__":

    get_cook_book1()
    get_cook_book2()
    multiplier1(1, 2, c=3)
    multiplier2(1, b=1, c=1)