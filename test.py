import random

def get_numbers_ticket(min_numb, max_numb, quantity):
    if min_numb < 1 or max_numb > 1000 or min_numb > max_numb:
        print("Your numbers are wrong")
        return []
    
    possible_numbers = max_numb - min_numb + 1
    if quantity > possible_numbers:
        return []
    
    list_numbers = set()
    while quantity != len(list_numbers):
        list_numbers.add(random.randint(min_numb, max_numb))
    
    return sorted(list_numbers)

print(get_numbers_ticket(10,40,5))