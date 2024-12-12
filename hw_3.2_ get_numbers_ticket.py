import random


def get_numbers_ticket(min, max, quantity):
    new_set = set()
    new_set_2 = []
        
    if min >= 1 and max <=1000 and quantity <= (max-min):
        while True:
            new_set.add(random.randint(min, max))
            if len(new_set) >= quantity:
                new_set_2 = sorted(new_set)
                break
    

    return new_set_2
print(get_numbers_ticket(10, 4, 2))