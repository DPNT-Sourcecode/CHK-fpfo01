# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter

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
    skus_counter = Counter(list(skus))
    sum = 0
    for code in skus_counter.keys():
        occurance = skus_counter.get(code)
        if occurance > 1:
            promo = offers.get(code)
            # if promo and occurance % promo[0] == 0:
            #     sum += promo[1]
            if promo:
                sum += promo[1]
        else:
            sum += items.get(code)
    return sum
