# noinspection PyUnusedLocal
# skus = unicode string

items = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

offers = {
    "A": (3, 130),
    "B": (2, 45),
}

def checkout(skus):
    skus_list = list(skus)
    sum = 0
    for code in skus_list:
        sum += items.get(code)
    return sum
