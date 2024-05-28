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
}

offers = {
    "A": [(3, 130), (5, 200)],
    "B": [(2, 45)],
}

special_offers = {
    "E": (2, "B"),
    "F": (2, "F"),
}

def checkout(skus):
    skus_counter = Counter(list(skus))
    sum = 0
    for code, (needed, free_item) in special_offers.items():
        if skus_counter.get(code):
            iterations = skus_counter.get(code) // needed
            while iterations > 0:
                print('no items ', skus_counter.get(code))
                num_free_items = skus_counter.get(code) // needed
                print('no free items ', num_free_items)
                if num_free_items > 0 and free_item in skus_counter:
                    skus_counter[free_item] = max(0, skus_counter[free_item] - 1)
                    iterations -= 1

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





