# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter

items = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}

offers = {
    "A": (3, 130),
    "B": (2, 45),
}

special_offers = {
    "E": (2, "B")
}

def checkout(skus):
    skus_counter = Counter(list(skus))
    sum = 0
    for code in skus_counter.keys():
        if not items.get(code):
            return -1
        occurance = skus_counter.get(code)
        if occurance > 1:
            promo = offers.get(code)
            if promo:
                quot = occurance // promo[0]
                remainder = occurance % promo[0]
                sum += (promo[1] * quot) + (items.get(code) * remainder)
            else:
                sum += occurance * items.get(code)
        else:
            sum += items.get(code)
    return sum
