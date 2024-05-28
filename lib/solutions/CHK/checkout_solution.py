# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter

items = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 10,
    "Z": 50,
}

offers = {
    "A": [(3, 130), (5, 200)],
    "B": [(2, 45)],
    "H": [(5, 45), (10, 80)],
    "K": [(2, 120)],
    "P": [(5, 200)],
    "Q": [(3, 80)],
    "V": [(2, 90), (3, 130)],
}

special_offers = {
    "E": (2, "B"),
    "F": (2, "F"),
    "N": (3, "M"),
    "R": (3, "Q"),
    "U": (3, "U"),
}

group_items = {"S", "T", "X", "Y", "Z"}

group_offer = (3, 45)


def checkout(skus):
    skus_counter = Counter(list(skus))
    sum = 0
    
    group_promo = []
    for code in group_items:
        if code in skus_counter and skus_counter.get(code) > 0:
            group_promo += [(items.get(code), code)] * skus_counter.get(code)
    group_promo.sort(key=lambda x: x[0])
    while len(group_promo) >= group_offer[0]:
        apply_to_codes = group_promo[-3:]
        del group_promo[-3:]
        for _, code in apply_to_codes:
            skus_counter[code] = skus_counter[code] - 1
        sum += group_offer[1]          
    
    for code, (needed, free_item) in special_offers.items():
        if skus_counter.get(code) and free_item in skus_counter:
            applied = 0
            while True:
                num_free_items = (skus_counter.get(code) // needed) - applied
                if num_free_items > 0:
                    if code == free_item and skus_counter.get(code) <= needed:
                        break
                    skus_counter[free_item] = max(0, skus_counter[free_item] - 1)
                    applied += 1
                else:
                    break

    for code in skus_counter.keys():
        if not items.get(code):
            return -1
        occurance = skus_counter.get(code)
        if occurance > 0:
            promo_list = offers.get(code, [])
            promo_list.sort(reverse=True, key=lambda x: x[0])       

            for promo in promo_list:
                if occurance >= promo[0]:
                    quot = occurance // promo[0]
                    remainder = occurance % promo[0]
                    sum += (promo[1] * quot)
                    occurance = remainder
            if occurance > 0:
                sum += occurance * items.get(code)
    return sum





