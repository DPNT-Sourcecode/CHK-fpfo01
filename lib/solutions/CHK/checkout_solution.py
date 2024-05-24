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
    "A": [(3, 130), (5, 200)],
    "B": [(2, 45)],
}

special_offers = {
    "E": (2, "B")
}

def checkout(skus):
    skus_counter = Counter(list(skus))
    sum = 0
    for code, (needed, free_item) in special_offers.items():
        if skus_counter.get(code):
            num_free_items = skus_counter.get(code) // needed
            if free_item in skus_counter:
                skus_counter[free_item] = max(0, skus_counter[free_item] - num_free_items)

    for code in skus_counter.keys():
        if not items.get(code):
            return -1
        occurance = skus_counter.get(code)
        if occurance > 0:
            promo_list = offers.get(code, [])
            promo_list.sort(reverse=True, key=lambda x: x[0])       
            # promo = offers.get(code)
            # if promo_list:
            for promo in promo_list:
                if occurance >= promo[0]:
                    quot = occurance // promo[0]
                    remainder = occurance % promo[0]
                    sum += (promo[1] * quot) + (items.get(code) * remainder)
                    occurance = remainder
                else:
                    sum += items.get(code) * occurance
                    occurance = 0
            if occurance > 0:
                sum += occurance * items.get(code)
        # else:
        #     sum += items.get(code) * skus_counter.get(code)
    return sum





