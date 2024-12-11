import random


def get_numbers_ticket(min, max, quantity):
    new_set = set()
    new_set_2 = []
   
    try:
        a = min/max
        if min >= 1 and int(max) <=1000 and 1 < quantity <1000:
            while True:
                new_set.add(random.randint(min, max))
                if len(new_set) < quantity:
                    continue
                else:
                    new_set_2 = sorted(new_set)
                    break
    except TypeError:
        print(f"{min} or {max} is not a number")

    return new_set_2
print(get_numbers_ticket(1, 1000, 5))