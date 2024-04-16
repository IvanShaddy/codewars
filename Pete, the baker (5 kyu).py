# Write a function cakes(), which takes the recipe (object) and the available ingredients
# (also an object) and returns the maximum number of cakes Pete can bake (integer).

def cakes(recipe, available):
    # если ингридиент в наличии есть в рецепте, то добавить в список с текущим значением
    # если нет то добавить в список со значением 0

    for ingridient in recipe:
        if ingridient not in available:
            available[ingridient] = 0
    # если ингридиент в наличии есть в рецепте,
    # то поделить без остатка кол-во ингридиента в наличии на кол-во ингридиента в рецепте
    available_count = dict()
    for ingridient in available:
        if ingridient in recipe:
            available_count[ingridient] = available[ingridient]//recipe[ingridient]
    count = available_count.values()
    return min(count)


print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))
