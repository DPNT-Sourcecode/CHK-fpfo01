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
    return items.get(skus_list[0])
